from robotic_arm import RoboticArm
from tasks.pick_and_place import PickAndPlaceTask

if __name__ == "__main__":
    robotic_arm = RoboticArm()
    pick_and_place_task = PickAndPlaceTask(robotic_arm)

    pick_and_place_task.perform_task()
