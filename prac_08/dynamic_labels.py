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
