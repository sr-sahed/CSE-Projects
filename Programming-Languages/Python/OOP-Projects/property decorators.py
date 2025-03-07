class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    def temperature(self):  
        return self._temperature

    @temperature.setter
    def temperature(self, value):  
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

obj = Celsius(25)
obj.temperature = 30  # Setter works here
print(obj.temperature)  # Getter works here
