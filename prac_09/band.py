"""
Band Class
"""


class Band:
    """Create a Band Class."""

    def __init__(self, name):
        """Initialise Class"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician object to  band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string representation of a Band consisting of name and musician objects."""
        return f"{self.name} ({self.musicians})"

    def play(self):
        """Return a list of strings, of musician in a band playing their first instrument."""
        playing = ''
        for musician in self.musicians:
            playing = playing + musician.play() + '\n'
        return playing