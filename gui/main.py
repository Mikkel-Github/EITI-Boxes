import box_renderer
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

    def render_box(self):
        print("Rendering box")
        box_renderer.Panda3DApp()


if __name__ == "__main__":
    BoxOptimizerApp().run()
