"""
Dynamic Labels exercise.
Benjamin Bowden

Estimated time: 30 min
actual time:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Gregory Peck", "Dr NoGrundles", "Lenny"]

class DynamicLabelsApp(App):
    """ Create dynamic labels in a GUI from a list of NAMES """

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        label = Label(text=NAMES, font_size='52')
        return self.root


DynamicLabelsApp().run()