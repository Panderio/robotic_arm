class Gripper:
    def __init__(self):
        # Initialize the gripper here
        self.active = False

    def activate(self):
        # Activate the gripper
        self.active = True

    def deactivate(self):
        # Deactivate the gripper
        self.active = False
