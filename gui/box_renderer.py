import sys

from direct.showbase.ShowBase import ShowBase
from panda3d.core import Point3, loadPrcFileData, DirectionalLight, FrameBufferProperties, WindowProperties, GraphicsPipe


class Panda3DApp(ShowBase):
    def __init__(self, height, width, depth):
        # headless mode
        loadPrcFileData("", "window-type offscreen")
        # Enable transparency support
        loadPrcFileData("", "framebuffer-alpha true")

        super().__init__()

        minimum_camera_zoom = 1.5
        highest_value = max([height, width, depth, minimum_camera_zoom])

        # Disable the default camera movement
        self.disableMouse()

        # Set the camera position
        self.camera.setPos(highest_value, highest_value * -2, highest_value)
        self.camera.lookAt(Point3(0, 0, 0))

        # Create a square box
        self.box = self.loader.loadModel("models/box")

        # Scale the box
        self.box.setScale(width, depth, height)

        # Set the box's position
        self.box.setPos(width / 2 * -1, depth / 2 * -1, height / 2 * -1)

        self.box.setTextureOff(1)
        self.box.setColor(156/255, 134/255, 100/255, 1.0)

        # Reparent the box to render
        self.box.reparentTo(self.render)

        # Light acting as a sun
        self.dlight = DirectionalLight('dlight')
        self.dlight.setColor((1, 1, 1, 1))
        self.dlnp = self.render.attachNewNode(self.dlight)
        self.dlnp.setHpr(30, -60, 0)
        self.render.setLight(self.dlnp)

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
        # self.destroy()
        self.taskMgr.stop()  # Stop the task manager
        self.graphicsEngine.removeAllWindows()
        return task.done


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 panda_render.py <height> <width> <depth>")
        sys.exit(1)

    # Retrieve command-line arguments
    height = float(sys.argv[1])
    width = float(sys.argv[2])
    depth = float(sys.argv[3])

    # Initialize and run the Panda3D application
    app = Panda3DApp(height, width, depth)
    app.run()
