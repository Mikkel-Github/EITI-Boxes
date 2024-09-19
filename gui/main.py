from kivymd.app import MDApp # type: ignore
from kivymd.uix.label import MDLabel  # type: ignore

class TestApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, KivyMD!", halign="center")

TestApp().run()