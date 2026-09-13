import os
import PyInstaller.__main__

# Application name
APP_NAME = "RoadCraft_SaveEditor_Multilang"

MAIN_SCRIPT = "main.py"
current_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir, "images", "ui", "icon.ico")
version_file = os.path.join(current_dir, "version_info.txt")

if not os.path.exists(icon_path):
    print(f"WARNING: Icon not found at: {icon_path}")
    print("Continuing without icon...")
    icon_path = None

args = [
    MAIN_SCRIPT,
    '--name=' + APP_NAME,
    '--onefile',
    '--windowed',
    '--clean',
    '--noconfirm',
    '--distpath=' + os.path.join(current_dir, 'Release'),
    '--workpath=' + os.path.join(current_dir, 'build'),
    '--specpath=' + os.path.join(current_dir, 'build'),
    '--add-data=' + os.path.join(current_dir, 'images') + ';images',
    '--add-data=' + os.path.join(current_dir, 'Lang') + ';Lang',
    '--add-data=' + os.path.join(current_dir, 'font') + ';font',
]

if os.path.exists(version_file):
    args.append('--version-file=' + version_file)

if icon_path:
    args.append(f'--icon={icon_path}')

print("Starting PyInstaller build...")
PyInstaller.__main__.run(args)
print("Build complete!")