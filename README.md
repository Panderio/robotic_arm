# Robotic Arm Project

This is a Python project that simulates a robotic arm and performs pick-and-place tasks. It uses the BluePy library for Bluetooth Low Energy (BLE) communication with temperature and pressure sensors, and also incorporates object detection using a machine learning model.

## Project Structure

The project has the following file structure:

```
robotic_arm_project/
├── main.py
├── robotic_arm/
│   ├── __init__.py
│   ├── arm.py
│   ├── gripper.py
│   ├── sensors.py
│   ├── temperature_sensor.py
│   └── pressure_sensor.py
│   └── camera.py
├── tasks/
│   ├── __init__.py
│   └── pick_and_place.py
│   └── object_detection.py
└── utils/
    ├── __init__.py
    └── math_utils.py
```

- `main.py`: The entry point of the project that initializes the robotic arm, temperature sensor, pressure sensor, and performs the pick-and-place task with object detection.
- `robotic_arm/`: The package containing the classes for the robotic arm and gripper.
  - `__init__.py`: An empty file to mark the directory as a Python package.
  - `arm.py`: Contains the `RoboticArm` class that represents the robotic arm and its movements.
  - `gripper.py`: Contains the `Gripper` class that represents the gripper mechanism of the robotic arm.
  - `sensors.py`: Contains the abstract base class `Sensor` for sensor functionality.
  - `temperature_sensor.py`: Contains the `TemperatureSensor` class that represents the temperature sensor and implements the BLE communication and temperature reading logic.
  - `pressure_sensor.py`: Contains the `PressureSensor` class that represents the pressure sensor and implements the BLE communication and pressure reading logic.
  - `camera.py`: Contains the `Camera` class that handles the object detection functionality.
- `tasks/`: The package containing the classes for performing specific tasks.
  - `__init__.py`: An empty file to mark the directory as a Python package.
  - `pick_and_place.py`: Contains the `PickAndPlaceTask` class that performs the pick-and-place task using the robotic arm and object detection.
  - `object_detection.py`: Contains the `ObjectDetection` class that handles the object detection using a machine learning model.
- `utils/`: The package containing utility functions and classes.
  - `__init__.py`: An empty file to mark the directory as a Python package.
  - `math_utils.py`: Contains utility math functions (placeholder for potential future utility functions).


## UML Diagrams

- Structure Diagram: [Link to UML/StructureDiagram.png](UML/Robotic%20Arm%20Project.png)
- Use Case Diagram: [Link to UML/UseCaseDiagram.png](UML/UML/Use_Case_%20Robotic%20Arm.png)
- Class Diagram: [Link to UML/ClassDiagram.png](UML/Class_Diagram%20Robotic%20Arm.png)
- Sequence Diagram: [Link to UML/SequenceDiagram.png](UML/Sequence_Diagram%20Robotic%20Arm.png)
- Package Diagram: [Link to UML/PackageDiagram.png](UML/Package%20Diagram%20Robotic%20Arm.png)

## Usage

To run the project, make sure you have Python 3.x installed. Then, follow these steps:

1. Install the required dependencies:

   ```bash
   pip install bluepy tensorflow  # Replace `tensorflow` with the appropriate package for your object detection model
   ```

2. Clone this repository or download the source code.

3. Navigate to the project directory:

   ```bash
   cd robotic_arm_project
   ```

4. Run the `main.py` script:

   ```bash
   python main.py
   ```

   This will initialize the robotic arm, temperature sensor, pressure sensor, and perform the pick-and-place task with object detection.

## Contributing

Contributions to this project are welcome. Feel free to submit bug reports, feature requests, or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
