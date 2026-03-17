from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Accumulator | Binance Builder Edition</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #0B0E11; color: #EAECEF; min-height: 100vh; font-family: 'Inter', sans-serif; }
        .binance-yellow { color: #FCD535; }
        .binance-bg-yellow { background-color: #FCD535; }
        .glass { background: #1E2329; border: 1px solid #474D57; border-radius: 8px; }
        .terminal-input { background: transparent; border: none; outline: none; width: 100%; color: #FCD535; font-family: monospace; }
        .btn-binance:hover { opacity: 0.9; transform: translateY(-1px); transition: 0.2s; }
    </style>
</head>
<body class="p-6">
    <div class="max-w-4xl mx-auto">
        <header class="flex justify-between items-center mb-8 border-b border-gray-800 pb-6">
            <div class="flex items-center gap-3">
                <div class="binance-bg-yellow w-8 h-8 rounded flex items-center justify-center">
                    <svg class="w-5 h-5 text-black" viewBox="0 0 24 24" fill="currentColor"><path d="M16.624 13.9202l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm-9.504 0l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zM11.872 21.3122l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm-9.504 0l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624zm4.752-4.752l-2.624 2.624-2.624-2.624 2.624-2.624 2.624 2.624z"/></svg>
                </div>
                <h1 class="text-xl font-bold tracking-tight uppercase">Apex <span class="binance-yellow">Accumulator</span></h1>
            </div>
            <a href="https://t.me/ApexTradeBot" target="_blank" class="binance-bg-yellow px-4 py-2 text-xs text-black font-bold rounded btn-binance uppercase tracking-wide flex items-center gap-2">
                Launch Bot
            </a>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            <div class="glass p-5">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold">SPOT_BALANCE</h3>
                <p class="text-xl font-semibold">5.88 <span class="text-xs text-gray-400">USDT</span></p>
            </div>
            <div class="glass p-5">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold">YIELD_STATUS</h3>
                <p class="text-xl font-semibold text-green-400">OPTIMIZED</p>
            </div>
            <div class="glass p-5">
                <h3 class="text-gray-500 text-[10px] mb-1 font-bold">DCA_ENGINE</h3>
                <p class="text-xl font-semibold">WAITING_DIP</p>
            </div>
        </div>

        <div class="glass p-6 min-h-[350px] flex flex-col justify-end bg-[#181A20]">
            <div class="text-gray-500 text-xs mb-4 opacity-50 font-mono">-- Apex v1.0.4 Terminal Ready --</div>
            <div class="text-white text-sm mb-2 font-mono">
                <span class="binance-yellow">Apex:</span> "Identity confirmed. Monitoring Binance Simple Earn for yield gaps..."
            </div>
            
            <div class="flex items-center gap-2 text-[#FCD535] font-mono">
                <span>></span>
                <input type="text" class="terminal-input" placeholder="Scan market..." autofocus>
            </div>
        </div>
        
        <footer class="mt-8 flex justify-center opacity-30">
            <p class="text-[9px] uppercase tracking-[0.2em]">Powered by OpenClaw Architecture | Built for Binance 2026</p>
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run()
