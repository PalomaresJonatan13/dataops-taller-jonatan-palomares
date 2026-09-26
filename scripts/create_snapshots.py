from datetime import datetime
from pathlib import Path
import shutil

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SOURCE_DB = PROJECT_ROOT / "data" / "database.db"
SNAPSHOT_DIR = PROJECT_ROOT / "data" / "snapshots"

SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)

date_str = datetime.now().strftime("%Y%m%d")
snapshot_path = SNAPSHOT_DIR / f"ventas_{date_str}.db"

shutil.copy2(SOURCE_DB, snapshot_path)

print(f"Snapshot created: {snapshot_path}")