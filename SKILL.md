---
name: catfish-pet
description: Install, verify, and recreate the 猫猫鱼 (Catfish) Codex pixel pet from bundled assets. Use when a user asks to install this pet on another account or machine, restore its v2 spritesheet, or rebuild it using the bundled reference and hatch-pet workflow.
---

# 猫猫鱼 Pet

This skill ships the approved Codex v2 pet package for 猫猫鱼: a purple-haired cat with brown ears, cream body, burgundy scarf, black bow detail, and curled tail.

## Install

### 换账号安装

1. 将 `catfish-pet-skill.zip` 解压为 `catfish-pet` 文件夹，并放入新账号的 `$CODEX_HOME/skills/`。如果未设置 `CODEX_HOME`，默认目录是 `~/.codex/skills/`。
2. 在终端进入 skill 目录：

```bash
cd "${CODEX_HOME:-$HOME/.codex}/skills/catfish-pet"
```

3. 运行 bundled installer：

```bash
python3 scripts/install_pet.py
```

安装脚本会把 `assets/pet.json` 和 `assets/spritesheet.webp` 复制到 `${CODEX_HOME:-$HOME/.codex}/pets/catfish/`，并验证图集尺寸为 `1536x2288`、manifest 声明 `spriteVersionNumber: 2`。

如果 skill 文件夹不在 `$CODEX_HOME/skills/`，也可以直接从它所在目录运行 `python3 scripts/install_pet.py`；安装目标仍由 `CODEX_HOME` 决定。

After installation, restart Codex or switch to another pet and back so the client reloads the asset. The client owns state transitions; this skill cannot add new triggers or randomize animation playback.

## Recreate or modify

Use `assets/reference.png` as the canonical identity reference and invoke the `hatch-pet` skill for regenerated rows. Preserve the pixel style, palette, proportions, scarf, bow, curled tail, magenta chroma workflow, and the 8x11 v2 contract. Run `validate_atlas.py --require-v2` before replacing the installed sheet.

The current work row is a six-frame laptop-only loop. The approved standard rows are idle, running-right, running-left, waving, jumping, failed, waiting, running, and review; rows 9-10 contain the 16 look directions.

## Bundled files

- `assets/pet.json`: install manifest.
- `assets/spritesheet.webp`: approved `1536x2288` RGBA v2 atlas.
- `assets/reference.png`: canonical base reference for regeneration.
- `scripts/install_pet.py`: deterministic cross-account installer and sanity checker.
