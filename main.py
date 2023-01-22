from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static


class SnakeGame(App):
    """
    A Textual app to play Snake on the terminal.
    """

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """
        Create the child widgets for the app.
        """

        yield Header()
        yield Footer()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
