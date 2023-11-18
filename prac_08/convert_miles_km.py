"""
Miles to Kilometres app
Benjamin Bowden

est. time: 1 hour
actual time:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_KM_CONVERSION = 1.60934

class ConvertMilesKmApp(App):
    """ create app"""

    def build(self):
        """ build the app from the kv file """
        self.title = "Convert Miles to Kilometres"  # App window title
        self.root = Builder.load_file("convert_miles_km.kv")    # Build app using .kv file
        return self.root

    def handle_calculation(self):
        """ handle the calculation"""
        try:
            miles_input = float(self.root.ids.input_miles.text)
            converted_input = miles_input * MILES_KM_CONVERSION
            self.root.ids.output_kilometre.text = str(converted_input)
        except ValueError:  # won't action if number isn't entered
            pass



ConvertMilesKmApp().run()
