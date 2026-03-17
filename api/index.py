from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Accumulator | Live Market</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #0B0E11; color: #EAECEF; min-height: 100vh; font-family: 'Inter', sans-serif; }
        .binance-yellow { color: #FCD535; }
        .binance-bg-yellow { background-color: #FCD535; }
        .glass { background: #181A20; border: 1px solid #2B3139; border-radius: 8px; }
        .terminal-input { background: transparent; border: none; outline: none; width: 100%; color: #FCD535; font-family: monospace; }
        .price-up { color: #0ecb81; }
        .price-down { color: #f6465d; }
    </style>
</head>
<body class="p-4 md:p-8">
    <div class="max-w-4xl mx-auto">
        <div class="flex gap-4 mb-6 overflow-x-auto pb-2 no-scrollbar">
            <div class="glass px-4 py-2 flex gap-3 items-center min-w-fit">
                <span class="text-[10px] font-bold text-gray-500">BTC/USDT</span>
                <span id="btc-price" class="font-mono font-bold tracking-tight">Loading...</span>
            </div>
            <div class="glass px-4 py-2 flex gap-3 items-center min-w-fit">
                <span class="text-[10px] font-bold text-gray-500">ETH/USDT</span>
                <span id="eth-price" class="font-mono font-bold tracking-tight text-gray-400">Loading...</span>
            </div>
            <div class="glass px-4 py-2 flex gap-3 items-center min-w-fit">
                <span class="text-[10px] font-bold text-gray-500">BNB/USDT</span>
                <span id="bnb-price" class="font-mono font-bold tracking-tight text-gray-400">Loading...</span>
            </div>
        </div>

        <header class="flex justify-between items-center mb-8 pb-6 border-b border-gray-800">
            <div class="flex items-center gap-3">
                <div class="binance-bg-yellow p-1.5 rounded">
                    <svg class="w-5 h-5 text-black" viewBox="0 0 24 24" fill="currentColor"><path d="M16.624 13.9202l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm-9.504 0l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624z"/></svg>
                </div>
                <h1 class="text-xl font-bold tracking-tighter uppercase">Apex <span class="binance-yellow">Accumulator</span></h1>
            </div>
            <a href="https://t.me/ApexTradeBot" target="_blank" class="binance-bg-yellow px-4 py-2 text-xs text-black font-bold rounded uppercase hover:opacity-80 transition-all">Launch Bot</a>
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
            <div class="text-gray-600 text-[10px] mb-4 font-mono uppercase tracking-[0.3em]">-- System Log: Connection Established --</div>
            <div class="text-white text-sm mb-3 font-mono leading-relaxed">
                <span class="binance-yellow font-bold">Apex:</span> "Dashboard initialized. Streaming live price data from Binance WebSocket. Analyzing RSI for potential entries..."
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
            const price = parseFloat(data.c).toFixed(2);
            const el = document.getElementById(symbol.split('usdt')[0] + '-price');
            
            if (el) {
                const oldPrice = parseFloat(el.innerText);
                el.innerText = price;
                el.className = 'font-mono font-bold tracking-tight ' + (price > oldPrice ? 'price-up' : 'price-down');
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
