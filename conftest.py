import sys
from pathlib import Path

# Make project root importable so `from src.text_stats import ...` works
sys.path.insert(0, str(Path(__file__).parent))
