"""Configuração. Segredos vêm do arquivo .env (nunca versionado)."""
import os
from dotenv import load_dotenv

load_dotenv()


def _bool(name: str, default: str) -> bool:
    return os.getenv(name, default).strip().lower() in ("1", "true", "yes", "sim")


# --- Conta ---------------------------------------------------------------
# Endereço PÚBLICO da carteira principal (a que tem o saldo).
ACCOUNT_ADDRESS = os.getenv("HL_ACCOUNT_ADDRESS", "")
# Chave privada da API WALLET (só opera, não saca). Gerada em app.hyperliquid.xyz/API
API_SECRET = os.getenv("HL_API_SECRET", "")
TESTNET = _bool("HL_TESTNET", "false")
# DRY_RUN=true: só registra o que faria, não envia ordens. Comece SEMPRE assim.
DRY_RUN = _bool("DRY_RUN", "true")

# --- Mercado / estratégia ------------------------------------------------
COIN = os.getenv("COIN", "BTC")
INTERVAL = os.getenv("INTERVAL", "4h")  # 4h teve resultado melhor no backtest
EMA_FAST = int(os.getenv("EMA_FAST", "20"))
EMA_SLOW = int(os.getenv("EMA_SLOW", "50"))
ATR_PERIOD = 14
SL_ATR_MULT = float(os.getenv("SL_ATR_MULT", "1.5"))   # stop = 1,5 x ATR
RR = float(os.getenv("RR", "2.0"))                     # alvo = 2 x distância do stop

# --- Risco (perfil conservador) ------------------------------------------
MAX_LEVERAGE = int(os.getenv("MAX_LEVERAGE", "3"))
RISK_PER_TRADE = float(os.getenv("RISK_PER_TRADE", "0.02"))   # 2% do capital
DAILY_LOSS_LIMIT = float(os.getenv("DAILY_LOSS_LIMIT", "0.05"))  # para no dia em -5%
MIN_NOTIONAL_USD = 11.0   # Hyperliquid exige >= US$10 por ordem
SLIPPAGE = 0.01

POLL_SECONDS = 60
STATE_FILE = os.getenv("STATE_FILE", "state.json")
