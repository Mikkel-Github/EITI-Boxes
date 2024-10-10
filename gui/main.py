import subprocess

from kivy.lang import Builder
from kivymd.app import MDApp  # type: ignore
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager

# TODO : Uncomment this to use the client to communicate with the box spawner service (wont work if you dont have ROS installed)
# from box_spawner_client import reset_gazebo, delete_model, start_simulation

class BoxSpecificationWindow(MDScreen):
    pass

class SimulationWindow(MDScreen):
    pass

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

        box_screen = self.root.get_screen('box_specification_window')

        height = box_screen.ids.height_input.text
        width = box_screen.ids.width_input.text
        depth = box_screen.ids.depth_input.text

        if(height == "" or width == "" or depth == ""):
            return

        subprocess.run(
            ["python3", "./gui/box_renderer.py", str(height), str(width), str(depth)]
        )

        image_widget = box_screen.ids.rendered_image
        image_widget.source = "../rendered_image.png"
        image_widget.reload()  # Force reload of the image

    def run_simulation(self):
        box_screen = self.root.get_screen('box_specification_window')

        amount = box_screen.ids.amount_input.text
        mass = box_screen.ids.mass_input.text
        height = box_screen.ids.height_input.text
        width = box_screen.ids.width_input.text
        depth = box_screen.ids.depth_input.text

        if(amount == "" or mass == "" or height == "" or width == "" or depth == ""):
            print("Missing values")
            return

        print("Run simulation")

        self.root.current = 'simulation_window'
        # TODO : Uncomment this and the comment in imports, to start simulation (wont work if you dont have ROS installed)
        #start_simulation(amount, mass, height, width, length)

    def delete_boxes(self):
        print("Deleting boxes")
        # TODO : Provide box ids to be deleted
        # delete_model

    def stop_simulation(self):
        print("Stopping simulation")
        # TODO : No stop simulation function in box_spawner_client (maybe just use reset_gazebo unless if it starts the simulation again)
        self.root.current = 'box_specification_window'

if __name__ == "__main__":
    BoxOptimizerApp().run()