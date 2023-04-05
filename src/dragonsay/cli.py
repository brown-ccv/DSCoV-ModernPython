"""Main project entry"""

import cowsay
import typer

app = typer.Typer()

@app.command()
def say(text: str) -> None:
    """Prints an ascii art of a dragon.

    Parameters
    ----------
    text
        The text to be printed.
    """
    cowsay.dragon(text)

if __name__ == "__main__":
    app()
