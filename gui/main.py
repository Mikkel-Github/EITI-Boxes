import subprocess

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

        height = self.root.ids.height_input.text
        width = self.root.ids.width_input.text
        depth = self.root.ids.depth_input.text

        subprocess.run(
            ["python3", "./gui/box_renderer.py", str(height), str(width), str(depth)]
        )

        image_widget = self.root.ids.rendered_image
        image_widget.source = "../rendered_image.png"
        # image_widget.source = "./logo-kivymd.webp"
        image_widget.reload()  # Force reload of the image


if __name__ == "__main__":
    BoxOptimizerApp().run()
