from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Accumulator | Live Terminal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #0B0E11; color: #EAECEF; min-height: 100vh; font-family: 'Inter', sans-serif; }
        .binance-yellow { color: #FCD535; }
        .binance-bg-yellow { background-color: #FCD535; }
        .glass { background: #181A20; border: 1px solid #2B3139; border-radius: 8px; }
        .terminal-input { background: transparent; border: none; outline: none; width: 100%; color: #FCD535; font-family: monospace; }
        .price-up { color: #0ecb81; text-shadow: 0 0 8px rgba(14, 203, 129, 0.4); }
        .price-down { color: #f6465d; text-shadow: 0 0 8px rgba(246, 70, 93, 0.4); }
        .no-scrollbar::-webkit-scrollbar { display: none; }
    </style>
</head>
<body class="p-4 md:p-8">
    <div class="max-w-4xl mx-auto">
        <header class="mb-8 pb-6 border-b border-gray-800">
            <div class="flex justify-between items-start mb-6">
                <div class="flex items-center gap-3">
                    <div class="binance-bg-yellow p-1.5 rounded">
                        <svg class="w-5 h-5 text-black" viewBox="0 0 24 24" fill="currentColor"><path d="M16.624 13.9202l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm-9.504 0l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624z"/></svg>
                    </div>
                    <h1 class="text-xl font-bold tracking-tighter uppercase text-white">Apex <span class="binance-yellow">Accumulator</span></h1>
                </div>
                <a href="https://t.me/ApexTradeBot" target="_blank" class="binance-bg-yellow px-4 py-2 text-[10px] text-black font-bold rounded uppercase hover:opacity-80 transition-all">Launch Bot</a>
            </div>

            <div class="flex gap-6 overflow-x-auto no-scrollbar">
                <div class="flex flex-col">
                    <span class="text-[9px] font-bold text-gray-500 uppercase tracking-widest">BTC / USDT</span>
                    <span id="btc-price" data-last="0" class="text-sm font-mono font-bold transition-colors duration-300">---</span>
                </div>
                <div class="flex flex-col border-l border-gray-800 pl-6">
                    <span class="text-[9px] font-bold text-gray-500 uppercase tracking-widest">ETH / USDT</span>
                    <span id="eth-price" data-last="0" class="text-sm font-mono font-bold text-gray-400 transition-colors duration-300">---</span>
                </div>
                <div class="flex flex-col border-l border-gray-800 pl-6">
                    <span class="text-[9px] font-bold text-gray-500 uppercase tracking-widest">BNB / USDT</span>
                    <span id="bnb-price" data-last="0" class="text-sm font-mono font-bold text-gray-400 transition-colors duration-300">---</span>
                </div>
            </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            <div class="glass p-5">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold tracking-widest">SPOT_BALANCE</h3>
                <p class="text-xl font-semibold">5.88 <span class="text-[10px] text-gray-500 font-normal">USDT</span></p>
            </div>
            <div class="glass p-5 border-l-2 border-l-[#0ecb81]">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold tracking-widest">YIELD_STATUS</h3>
                <p class="text-xl font-semibold text-[#0ecb81]">OPTIMIZED</p>
            </div>
            <div class="glass p-5">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold tracking-widest">DCA_ENGINE</h3>
                <p class="text-xl font-semibold">WAITING_DIP</p>
            </div>
        </div>

        <div class="glass p-6 min-h-[300px] flex flex-col justify-end bg-[#111419]">
            <div class="text-gray-600 text-[10px] mb-4 font-mono uppercase tracking-[0.3em]">-- Live Market Feed: Connected --</div>
            <div class="text-white text-sm mb-3 font-mono leading-relaxed">
                <span class="binance-yellow font-bold">Apex:</span> "Dashboard sync active. Real-time tickers enabled. Listening for market volatility..."
            </div>
            <div class="flex items-center gap-2 text-[#FCD535] font-mono">
                <span class="animate-pulse">></span>
                <input type="text" class="terminal-input" placeholder="Enter command..." autofocus>
            </div>
        </div>
    </div>

    <script>
        const symbols = ['btcusdt', 'ethusdt', 'bnbusdt'];
        const ws = new WebSocket('wss://stream.binance.com:9443/ws/' + symbols.map(s => s + '@ticker').join('/'));
        
        ws.onmessage = (event) => {
            const data = JSON.parse(event.data);
            const symbol = data.s.toLowerCase();
            const newPrice = parseFloat(data.c);
            const id = symbol.split('usdt')[0] + '-price';
            const el = document.getElementById(id);
            
            if (el) {
                const lastPrice = parseFloat(el.getAttribute('data-last'));
                
                if (lastPrice !== 0) {
                    if (newPrice > lastPrice) {
                        el.className = 'text-sm font-mono font-bold price-up';
                    } else if (newPrice < lastPrice) {
                        el.className = 'text-sm font-mono font-bold price-down';
                    }
                }
                
                el.innerText = newPrice.toLocaleString(undefined, {minimumFractionDigits: 2});
                el.setAttribute('data-last', newPrice);
            }
        };
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run()
