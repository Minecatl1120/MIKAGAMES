import sys
from PyQt5.QtWidgets import QApplication
from ui import GameLauncherUI
from game_fetcher import fetch_installed_games

class MIKAGAMES:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui = GameLauncherUI()
        self.load_games()

    def load_games(self):
        """Fetch installed games and populate UI"""
        games = fetch_installed_games()
        self.ui.populate_game_list(games)

    def run(self):
        """Run the game launcher"""
        self.ui.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    launcher = MIKAGAMES()
    launcher.run()
