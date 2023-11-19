"""Box Layout Demo."""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App that contains for entering a name and responding with a greeting."""
    def build(self):
        """create teh main app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """activate greeting"""
        self.root.ids.button_label.text = f"Hello {self.root.ids.name.text}!"

    def handle_clear(self):
        """Reset fields"""
        self.root.ids.button_label.text = 'Enter your name here:'
        self.root.ids.name.text = ''


BoxLayoutDemo().run()