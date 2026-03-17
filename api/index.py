from flask import Flask, render_template_string
import os

app = Flask(__name__)

# A clean, Dark-Mode Glassmorphism template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex Accumulator | Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: radial-gradient(circle at top left, #1a1a2e, #16213e); color: white; min-height: 100vh; font-family: sans-serif; }
        .glass { background: rgba(255, 255, 255, 0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; }
        .glow { box-shadow: 0 0 20px rgba(0, 150, 255, 0.3); }
    </style>
</head>
<body class="p-8">
    <div class="max-w-4xl mx-auto">
        <header class="flex justify-between items-center mb-12">
            <h1 class="text-3xl font-bold tracking-tighter text-blue-400">APEX <span class="text-white">ACCUMULATOR</span></h1>
            <div class="glass px-4 py-2 text-sm text-green-400 animate-pulse">● AGENT LIVE</div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="glass p-6 glow">
                <h3 class="text-gray-400 uppercase text-xs font-semibold mb-2">Yield Sweeper Status</h3>
                <p class="text-2xl font-mono">Active</p>
                <p class="text-sm text-gray-500 mt-4 italic">Next sweep scheduled via VPS Cron.</p>
            </div>
            <div class="glass p-6 glow">
                <h3 class="text-gray-400 uppercase text-xs font-semibold mb-2">DCA Strategy</h3>
                <p class="text-2xl font-mono">RSI-14 / 3% Dip</p>
                <p class="text-sm text-gray-500 mt-4 italic">Monitoring BTC/USDT hourly.</p>
            </div>
        </div>

        <div class="glass mt-8 p-6 overflow-hidden">
            <h3 class="text-gray-400 uppercase text-xs font-semibold mb-4">Architecture Identity</h3>
            <p class="text-sm leading-relaxed text-gray-300">
                Apex is an autonomous agent operating via OpenClaw. Its core soul is designed to optimize Binance yield while maintaining strict risk management through algorithmic DCA triggers.
            </p>
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
