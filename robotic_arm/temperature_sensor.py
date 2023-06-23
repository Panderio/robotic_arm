class TemperatureSensor:
    def __init__(self):
        # Initialize the temperature sensor here
        self.value = 0

    def measure(self):
        # Simulate measuring the temperature
        self.value = 25
        return self.value
