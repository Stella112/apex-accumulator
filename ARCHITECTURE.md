# Dual-Threat Architecture (Apex → Maris)

## 1. Zero-Idle Yield Sweeper
- **Trigger:** Daily (default 08:00 UTC; configurable once Maris confirms preferred cutover)
- **Inputs:**
  - `/api/v3/account` (Spot balances via Binance API — requires read-only key)
  - `/api/v3/ticker/price` for USDT, BNB, and USD conversion pairs (no auth)
  - Binance Earn product catalog (Simple Earn Flexible/Locked) for current APYs
- **Logic:**
  1. Pull free balances for USDT + BNB.
  2. Convert BNB to USD value using `BNBUSDT` mid-price.
  3. If either idle bucket exceeds $50, fetch the highest-yield matching Earn product (flexible first unless Maris prefers locked terms).
  4. Generate alert summarizing idle size, recommended product, APY, lock duration, and est. daily earnings.
- **State:**
  - `state/zero_idle.json` to store last sweep timestamp, idle amounts, and recommended product to avoid duplicate nudges.
- **Delivery:** Main chat (this thread) unless Maris specifies another channel.

## 2. Smart “Dip-Only” DCA Bot
- **Trigger:** Hourly scan aligned to Binance 1h klines (run at HH:05) + optional 5m backstop for sudden 3% dumps.
- **Inputs:**
  - `/api/v3/klines` for BTCUSDT + ETHUSDT (1h interval)
  - Derived RSI-14 calculation on closing prices
- **Logic:**
  1. Maintain rolling closing-price buffer (>=200 points) per asset for RSI.
  2. Signal if either condition hits:
     - RSI-14 < 30 on the latest closed 1h candle.
     - Price drops ≥3% vs previous 1h close (or vs 24h VWAP — configurable).
  3. When triggered, allocate from a $100 weekly virtual budget:
     - Track `state/dca_budget.json` with week number, remaining budget, and fills.
     - Default split: $50 BTC / $50 ETH unless Maris specifies dynamic weighting.
  4. Emit alert detailing trigger, suggested paper-trade size, reference price, RSI, and YTD hit count.
- **State:**
  - Candle cache (`data/klines/*.json`)
  - Weekly budget ledger + reset every Monday 00:00 UTC (configurable).
- **Delivery:** Same as sweeper; include explicit “paper trade” phrasing.

## Automation Plan
1. **Credentials** — need Binance API key/secret with read-only Spot + Earn scope to unlock sweeper + Earn APY endpoints.
2. **Scripts** — implement Python utilities under `bin/` (`zero_idle.py`, `dca_bot.py`).
3. **Cron** —
   - `zero_idle.py` daily 08:00 UTC
   - `dca_bot.py --mode hourly` every hour at HH:05 UTC
   - `dca_bot.py --mode monitor` every 5 minutes for fast 3% moves (optional, lightweight)
4. **Alert templates** — Markdown summaries piped into this chat; optionally extend to Telegram/Email later.

_Recorded: 2026-03-17_
