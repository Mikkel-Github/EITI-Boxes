import sys

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Filename, PNMImage, Point3, Texture


class Panda3DApp(ShowBase):
    def __init__(self):
        super().__init__()

        # Disable the default camera movement
        self.disableMouse()

        # Set the camera position
        self.camera.setPos(5, -10, 5)
        self.camera.lookAt(Point3(0, 0, 0))

        # Create a square box
        self.box = self.loader.loadModel("models/box")

        # Scale the box
        self.box.setScale(1, 1, 1)

        # Set the box's position
        self.box.setPos(-0.5, -0.5, -0.5)

        self.box.setTextureOff(1)
        self.box.setColor(0.94, 0.74, 0.24, 1.0)

        # Reparent the box to render
        self.box.reparentTo(self.render)

        # Add a task to take a screenshot and exit
        self.taskMgr.add(self.take_screenshot_and_exit, "take_screenshot_and_exit")

    def take_screenshot_and_exit(self, task):
        # Render one frame, otherwise, the screenshot will be empty
        self.graphicsEngine.renderFrame()
        # Take the screenshot
        self.screenshot("rendered_image.png", False)
        print("Image saved as rendered_image.png")

        # Exit the application
        # sys.exit()
        return task.done


# if __name__ == "__main__":
#     # Initialize the Panda3D application
#     app = Panda3DApp()
#     app.run()
