import bluepy.btle as btle

class Sensor:
    def __init__(self, name):
        self.name = name

    def read_data(self):
        raise NotImplementedError("Subclasses must implement the read_data() method")

class TemperatureSensor(Sensor):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
        self.device = btle.Peripheral()

    def connect(self):
        # Connect to the temperature sensor using BLE
        self.device.connect(self.address)

    def disconnect(self):
        # Disconnect from the temperature sensor
        self.device.disconnect()

    def read_data(self):
        # Read temperature data from the sensor
        temperature = None
        try:
            # Connect to the temperature sensor
            self.connect()

            # Read the temperature characteristic from the sensor
            temperature_characteristic = self.device.getCharacteristics(uuid='00002a6e-0000-1000-8000-00805f9b34fb')[0]
            temperature_bytes = temperature_characteristic.read()
            temperature = self.parse_temperature(temperature_bytes)

        except btle.BTLEException as e:
            print(f"Error reading temperature: {e}")

        finally:
            # Disconnect from the temperature sensor
            self.disconnect()

        return temperature

    def parse_temperature(self, temperature_bytes):
        # Parse the temperature value from the raw bytes
        temperature = int.from_bytes(temperature_bytes, byteorder='little', signed=True) / 100.0
        return temperature

class PressureSensor(Sensor):
    def __init__(self, name, address):
        super().__init__(name)
        self.address = address
        self.device = btle.Peripheral()

    def connect(self):
        # Connect to the pressure sensor using BLE
        self.device.connect(self.address)

    def disconnect(self):
        # Disconnect from the pressure sensor
        self.device.disconnect()

    def read_data(self):
        # Read pressure data from the sensor
        pressure = None
        try:
            # Connect to the pressure sensor
            self.connect()

            # Read the pressure characteristic from the sensor
            pressure_characteristic = self.device.getCharacteristics(uuid='00002a6d-0000-1000-8000-00805f9b34fb')[0]
            pressure_bytes = pressure_characteristic.read()
            pressure = self.parse_pressure(pressure_bytes)

        except btle.BTLEException as e:
            print(f"Error reading pressure: {e}")

        finally:
            # Disconnect from the pressure sensor
            self.disconnect()

        return pressure

    def parse_pressure(self, pressure_bytes):
        # Parse the pressure value from the raw bytes
        pressure = int.from_bytes(pressure_bytes, byteorder='little', signed=False) / 1000.0
        return pressure
