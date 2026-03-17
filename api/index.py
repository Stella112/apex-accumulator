from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Accumulator | Terminal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #0a0a12; color: white; min-height: 100vh; font-family: 'Courier New', Courier, monospace; }
        .glass { background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; }
        .terminal-input { background: transparent; border: none; outline: none; width: 100%; color: #4ade80; }
        .btn-glow:hover { box-shadow: 0 0 15px rgba(59, 130, 246, 0.5); transform: translateY(-1px); transition: 0.2s; }
    </style>
</head>
<body class="p-6">
    <div class="max-w-4xl mx-auto">
        <header class="flex justify-between items-center mb-8">
            <h1 class="text-2xl font-bold tracking-tighter text-blue-400">APEX_CORE > <span class="text-white text-lg">v1.0.4</span></h1>
            <a href="https://t.me/ApexTradeBot" target="_blank" class="glass px-4 py-2 text-xs text-blue-400 btn-glow uppercase tracking-widest flex items-center gap-2">
                <span>Connect via Telegram</span>
                <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm4.467 8.216l-1.76 8.273c-.131.58-.474.724-.96.451l-2.686-1.979-1.296 1.246c-.143.143-.263.263-.538.263l.193-2.738 4.983-4.501c.216-.193-.047-.3-.333-.11l-6.16 3.878-2.652-.828c-.577-.18-.589-.577.12-.857l10.363-3.992c.48-.18.9.108.729.883z"/></svg>
            </a>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
            <div class="glass p-5">
                <h3 class="text-gray-500 text-xs mb-1">YIELD_SWEEPER</h3>
                <p class="text-xl">IDLE_SCAN: [COMPLETE]</p>
            </div>
            <div class="glass p-5">
                <h3 class="text-gray-500 text-xs mb-1">DCA_ENGINE</h3>
                <p class="text-xl">MARKET: [WAITING_FOR_DIP]</p>
            </div>
        </div>

        <div class="glass p-6 min-h-[350px] flex flex-col justify-end">
            <div class="text-gray-500 text-sm mb-4">-- System Initialization Complete --</div>
            <div class="text-blue-300 text-sm mb-2">Apex: "Maris, the system is live. I'm currently monitoring Binance Spot for idle assets. Use the Telegram link above to issue high-level commands."</div>
            
            <div class="flex items-center gap-2 text-green-400">
                <span>$</span>
                <input type="text" class="terminal-input" placeholder="Enter command..." autofocus>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run()
