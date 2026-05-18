from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path.cwd()

# Data Paths
DATA_RAW = BASE_DIR / "data/raw"
DATA_PROCESSED = BASE_DIR / "data/processed"
DATA_SAMPLE = BASE_DIR / "data/sample"

# Create directories
for path in [DATA_RAW, DATA_PROCESSED, DATA_SAMPLE]:
    path.mkdir(parents=True, exist_ok=True)

print("Configuration loaded successfully")
print(f"Project Root: {BASE_DIR.name}")
