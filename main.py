import sys
import random
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QMessageBox,
)
from PySide6.QtGui import QPalette, QColor, QFont
from PySide6.QtCore import Qt


class RockPaperScissorsGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0

    def initUI(self):
        self.setWindowTitle("Rock Paper Scissors Game")
        self.setGeometry(300, 300, 400, 400)

        # Set dark theme
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)

        self.layout = QVBoxLayout()

        self.title_label = QLabel("Rock Paper Scissors Game", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.layout.addWidget(self.title_label)

        self.score_label = QLabel("Player: 0 - Computer: 0", self)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.score_label)
        self.score_label.setStyleSheet("font-size: 18px;")
        self.score_label.setFont(QFont("Arial", 20))

        self.moves_label = QLabel("", self)
        self.moves_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.moves_label)
        self.moves_label.setStyleSheet("font-size: 18px;")
        self.moves_label.setFont(QFont("Arial", 20))

        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)
        self.result_label.setStyleSheet("font-size: 18px;")
        self.result_label.setFont(QFont("Arial", 20))

        self.image_layout = QHBoxLayout()
        self.rock_button = QPushButton("✊", self)
        self.rock_button.setStyleSheet(
            "font-size: 40px; background-color: #353535; color: white;"
        )
        self.rock_button.clicked.connect(lambda: self.play("Rock"))
        self.image_layout.addWidget(self.rock_button)

        self.paper_button = QPushButton("✋", self)
        self.paper_button.setStyleSheet(
            "font-size: 40px; background-color: #353535; color: white;"
        )
        self.paper_button.clicked.connect(lambda: self.play("Paper"))
        self.image_layout.addWidget(self.paper_button)

        self.scissors_button = QPushButton("✌️", self)
        self.scissors_button.setStyleSheet(
            "font-size: 40px; background-color: #353535; color: white;"
        )
        self.scissors_button.clicked.connect(lambda: self.play("Scissors"))
        self.image_layout.addWidget(self.scissors_button)

        self.layout.addLayout(self.image_layout)

        self.reset_button = QPushButton("Reset", self)
        self.reset_button.setStyleSheet("background-color: #353535; color: white;")
        self.reset_button.clicked.connect(self.reset)
        self.layout.addWidget(self.reset_button)

        self.exit_button = QPushButton("Exit (q)", self)
        self.exit_button.setStyleSheet("background-color: #353535; color: white;")
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

        self.setLayout(self.layout)

    def give_emoji(self, choice):
        if choice == "Rock":
            return "✊"
        elif choice == "Paper":
            return "✋"
        elif choice == "Scissors":
            return "✌️"

    def play(self, player_choice):
        if self.rounds_played >= 3:
            self.show_end_game_dialog()
            return

        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        self.moves_label.setText(
            f"You chose {player_choice} {self.give_emoji(player_choice)}, computer chose {computer_choice} {self.give_emoji(computer_choice)}"
        )
        result = ""

        if player_choice == computer_choice:
            result = f"Both players selected {player_choice}. It's a tie!"
            self.result_label.setStyleSheet("color: yellow;")
        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                result = "Rock smashes scissors! You win!"
                self.result_label.setStyleSheet("color: green;")
                self.player_score += 1
            else:
                result = "Paper covers rock! You lose."
                self.result_label.setStyleSheet("color: red;")
                self.computer_score += 1
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                result = "Paper covers rock! You win!"
                self.result_label.setStyleSheet("color: green;")
                self.player_score += 1
            else:
                result = "Scissors cuts paper! You lose."
                self.result_label.setStyleSheet("color: red;")
                self.computer_score += 1
        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                result = "Scissors cuts paper! You win!"
                self.result_label.setStyleSheet("color: green;")
                self.player_score += 1
            else:
                result = "Rock smashes scissors! You lose."
                self.result_label.setStyleSheet("color: red;")
                self.computer_score += 1

        self.result_label.setText(result)
        self.update_score()
        self.rounds_played += 1

        if self.rounds_played == 3:
            self.show_end_game_dialog()

    def reset(self):
        self.result_label.setText("")
        self.moves_label.setText("")
        self.result_label.setStyleSheet("")
        self.player_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.update_score()

    def update_score(self):
        self.score_label.setText(
            f"Player: {self.player_score} - Computer: {self.computer_score}"
        )

    def show_end_game_dialog(self):
        winner = ""
        if self.player_score > self.computer_score:
            winner = "You win the game!"
        elif self.computer_score > self.player_score:
            winner = "Computer wins the game!"
        else:
            winner = "The game is a tie!"

        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(f"{winner}\nDo you want to play again?")
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.buttonClicked.connect(self.handle_end_game_response)
        msg_box.exec()

    def handle_end_game_response(self, response):
        if response.text() == "&Yes":
            self.reset()
        else:
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RockPaperScissorsGame()
    window.show()
    sys.exit(app.exec())
