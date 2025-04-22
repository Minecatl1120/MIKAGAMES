import os
import platform
import subprocess

def launch_game(game_name):
    """Attempts to launch the selected game."""
    system = platform.system()

    # Example directories where games might be installed
    game_paths = {
        "Windows": rf"C:\Program Files (x86)\Steam\steamapps\common\{game_name}\{game_name}.exe",
        "Linux": f"~/.steam/steam/steamapps/common/{game_name}/{game_name}.sh",
        "Darwin": f"/Applications/{game_name}.app"
    }

    game_path = game_paths.get(system)
    
    if game_path and os.path.exists(game_path):
        if system == "Windows":
            subprocess.run(game_path, shell=True)
        else:
            subprocess.run(["open" if system == "Darwin" else "bash", game_path])
        print(f"Launching {game_name}...")
    else:
        print(f"Game '{game_name}' not found!")
