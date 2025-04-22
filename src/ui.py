from PyQt5.QtWidgets import QMainWindow, QListWidget, QVBoxLayout, QLineEdit, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class GameLauncherUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MIKAGAMES")
        self.setGeometry(200, 200, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search games...")
        layout.addWidget(self.search_bar)

        # Game List
        self.game_list = QListWidget(self)
        layout.addWidget(self.game_list)

        # Launch Button
        self.launch_button = QPushButton("Launch Selected Game")
        layout.addWidget(self.launch_button)

    def populate_game_list(self, games):
        """Load game names into the UI"""
        self.game_list.clear()
        for game in games:
            self.game_list.addItem(game)

    def get_selected_game(self):
        """Retrieve selected game from list"""
        selected_items = self.game_list.selectedItems()
        return selected_items[0].text() if selected_items else None
