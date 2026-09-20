# 🚛 roadcraft save editor

RoadCraft save editor is a modern save file editor for RoadCraft, the infrastructure construction and logistics simulation game by Saber Interactive. Built with PyQt6, this tool allows you to modify your game progress, unlock vehicles and maps, and manage in-game resources. This release features **multilanguage support** (English + Russian with pluggable custom language packs), **own UI settings** — accent color, bundled Roboto Flex font and adjustable font size (default 9), fully configurable in-app, and a **Fog of War editor**.

**Current version: 1.2.9**

![RoadCraft Save Editor](screenshot/1.png)
![RoadCraft Save Editor](screenshot/2.png)
![RoadCraft Save Editor](screenshot/3.png)
![RoadCraft Save Editor](screenshot/4.png)

## ✨ Features

### 🧩 Updated for the RoadCraft Reclaim Expansion
- Added the two Reclaim Expansion maps to the editor (based on the work by [TXC/roadcraft-save-editor](https://github.com/TXC/roadcraft-save-editor)):
  - Autumn Finds (Reclaim Expansion)
  - Summer Drought (Reclaim Expansion)

### 🌍 Multilanguage Support
- Built-in **English** and **Russian** language packs
- Switch languages on the fly in **Settings → Language**
- Easily add your own language: copy any file from the `Lang` folder, translate it and it will appear in the settings automatically
- Custom languages are stored in simple, human-readable JSON files next to the app (`Lang/*.json`)

### 🎨 Customizable Appearance
- Pick any accent color in **Settings → Accent color** — the whole UI restyles instantly
- Color choice is remembered in the app config file (`.roadcraft_editor/config.json` in your user folder)
- UI font: **Roboto Flex** (bundled, no system font required)
- Adjustable UI font size (default **9**, range 8–18) in **Settings → Font size**

### 🌫️ Fog of War Management
- Per-map **Fog of War** switch in the Levels table with three states:
  - **0% (left)** — fully cover the map in fog
  - **middle** — keep the current value (shows the original explored percentage)
  - **100% (right)** — fully reveal the whole map
- The active position is color-coded (red = covered, yellow = revealed) and labelled with the resulting percentage
- Operates directly on each map's `_fog_of_war` file next to the save; maps without a fog file show a disabled switch
- **The game must be closed** while changing Fog of War, and you can also edit it whenever you want from the save file directly — Fog of War files are modified in place, no extra files are created

### 🚚 Vehicle Management
- Unlock or lock individual trucks
- Bulk unlock/lock all trucks

### 📊 Player Statistics
- Modify in-game currency (money)
- Adjust experience points (XP)
- Change your company name

### 🗺️ Map Management
- Set level completion percentage
- Unlock or mark levels as completed:
  - Storm Preparation
  - Storm Aftermath
  - Incommunicado
  - Salt Mines
  - Dam Break
  - Sinkholes
  - Contamination
  - Washout
  - Sand Storm
  - Geothermal
  - Autumn Finds (Reclaim Expansion)
  - Summer Drought (Reclaim Expansion)
- Edit level-specific resources (logs, steel beams, concrete slabs, steel pipes)
- Modify fuel and recovery coins

### 🛡️ Data Safety & Backups
- Automatic timestamped backups before saving changes

## 💻 Installation

### Option 1: Download Release
1. Grab the latest build from the **Release** folder
2. Run `RoadCraft_SaveEditor_Multilang.exe`

### Option 2: Run from Source

#### Requirements
- Python 3.12+
- PyQt6 (GUI framework)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the editor
python main.py
```

### Option 3: Build Your Own Executable

```bash
# Make sure requirements are installed
pip install -r requirements.txt

# Build executable (output: Release/RoadCraft_SaveEditor_Multilang.exe)
python build_exe.py
```

## 🎮 How to Use

1. **Launch the RoadCraft Save Editor** (either the executable or from source)
2. **Close the game first!** Always edit the save file while **RoadCraft is not running** — otherwise the game may overwrite your edits or the save may be corrupted.
3. **Open your save file**:
   - Click the "Open Save File" button
   - Navigate to your RoadCraft save file location:
     - `C:\Users\[YourUsername]\AppData\Local\Saber\RoadCraftGame\storage\steam\user\[SteamID]\Main\save\SLOT_[number]\CompleteSave`
4. **Make your desired changes** to vehicles, resources, or player stats (and, optionally, Fog of War)
5. **Save your changes** by clicking the "Save" button
6. **Launch RoadCraft** to see your modifications in-game
7. **Watch out for Steam Cloud synchronization**: when Steam starts after editing, it may ask to synchronize the cloud save with the local copy. Choose **"Keep local files"** so your edited save is uploaded and not overwritten by the old cloud one.

## 🎮 Editing Fog of War (step by step)

The **Fog of War** column in the Levels table contains a 3-position switch for each map:

| Position | Result |
|----------|--------|
| `0%` (left)  | The whole map is covered in fog |
| middle       | Fog file is left unchanged (the original explored % is shown) |
| `100%` (right) | The whole map is fully revealed |

1. Open the save file (game must be **closed**).
2. In the **Levels** tab, find the map and move its Fog of War switch to the desired position.
3. Click **Save**. The map's `_fog_of_war` file is rewritten in place — no extra files are created.
4. Close the editor, then start the game.
5. If Steam asks to synchronize the cloud — choose **"Keep local files"** so nothing overwrites your edit.

> **ВАЖНО / IMPORTANT**
>
> - **The game must be completely closed** while you edit Fog of War.
> - After changing a map's Fog of War, **returning to the intermediate value is impossible**. A 100% revealing of the map means the whole cloud of war is opened, and the previous explored/unexplored pattern can no longer be reconstructed.
> - **You cannot restore the Fog of War back** — once a map is revealed, the game cannot "re-fog" it. There is no way to know which exact areas of the map were explored before, so the original partial state is lost forever.
> - Making changes is safe only for maps that already have a fog file next to the save; the editor never creates or fabricates save-file pieces (no synthetic files that could break on a game update).

## 🌍 Creating Your Own Language File

1. Go to the `Lang` folder next to the executable
2. Copy `en.json` and rename it, e.g. `de.json`
3. Edit `lang_name` / `native_name` (this is how it appears in the language list)
4. Translate the `strings` section
5. Start the editor — your new language now appears in **Settings → Language**

`Lang` files are automatically created next to the executable on first run.

## ⚠️ Usage Notes

- The game must be **fully closed** while editing (especially the Fog of War) — edits made while the game is running can be silently overwritten.
- After editing, if Steam offers to synchronize the cloud save, **choose "Keep local files"** so the edited save is kept.
- **Fog of War is one-way**: revealing a map cannot be undone and the Fog of War cannot be brought back — the original partial explore state is lost permanently.
- While automatic backups are created, manual backups are still recommended.
- Use at your own risk – modifying game files may affect gameplay or stability.

## 🗂️ Project Structure

```bash
├── main.py              # Application entry point
├── trucks.py            # Truck definitions and logic
├── style.py             # UI styling, fonts and accent-color themes
├── constants.py         # Configuration and constants
├── lang.py              # Language manager (reads Lang/*.json)
├── build_exe.py         # PyInstaller build script
├── version_info.txt     # Windows executable version metadata
├── images/
│   ├── trucks/          # Truck images
│   └── ui/              # UI graphics
├── Lang/                # Translation files (en.json, ru.json, ...)
├── font/                # Bundled Roboto Flex font
├── screenshot/          # Screenshots for documentation
└── README.md            # This file
```

## 💾 Save File Format

- Proprietary RoadCraft format
- 53-byte header with metadata
- Zlib-compressed JSON payload
- MD5 hash for integrity verification
- Timestamped backups created automatically

## 🙏 Credits & Attribution

This project is heavily based on the excellent work from the original:

- Original project: [roadcraft-completesave](https://github.com/NakedDevA/roadcraft-completesave)

Key features adapted:
- Save file decompression/compression logic
- Proprietary format handling
- Base64 and zlib operations

Original GUI project: [RifaiV/roadcraft-save-editor](https://github.com/RifaiV/roadcraft-save-editor)

RoadCraft Reclaim Expansion support (autumn and summer maps): [TXC/roadcraft-save-editor](https://github.com/TXC/roadcraft-save-editor)

- **Russian translation:** Dunottrue

## 🪄 About This Fork

Current home: [dunottrue/roadcraft-save-editor](https://github.com/dunottrue/roadcraft-save-editor) — downloads the latest release from that page.

This is a modern, GUI-based fork offering significant enhancements:

- Full PyQt6 GUI
- Visual truck gallery with images and stats
- Bulk actions for vehicles and maps
- Fog of War editor (per-map 3-position switch)
- Improved backup and save validation
- Multilanguage support with custom language packs
- Customizable accent color
- Roboto Flex UI font with adjustable size (default 9)