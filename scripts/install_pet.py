#!/usr/bin/env python3
import json
import os
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
DEST = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex")) / "pets" / "catfish"

manifest = json.loads((ASSETS / "pet.json").read_text(encoding="utf-8"))
if manifest.get("spriteVersionNumber") != 2:
    raise SystemExit("catfish-pet: pet.json must declare spriteVersionNumber 2")

try:
    from PIL import Image
except ImportError as exc:
    raise SystemExit("catfish-pet: Pillow is required for atlas verification") from exc

with Image.open(ASSETS / "spritesheet.webp") as sheet:
    if sheet.size != (1536, 2288):
        raise SystemExit(f"catfish-pet: expected 1536x2288 atlas, got {sheet.size}")

DEST.mkdir(parents=True, exist_ok=True)
shutil.copy2(ASSETS / "spritesheet.webp", DEST / "spritesheet.webp")
shutil.copy2(ASSETS / "pet.json", DEST / "pet.json")
print(f"Installed 猫猫鱼 to {DEST}")
