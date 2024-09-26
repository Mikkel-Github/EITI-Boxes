from kivy.lang import Builder
from kivymd.app import MDApp  # type: ignore
from kivymd.uix.screen import MDScreen


class BoxOptimizerApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.screen = Builder.load_file("./gui.kv")

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        return self.screen


if __name__ == "__main__":
    BoxOptimizerApp().run()
