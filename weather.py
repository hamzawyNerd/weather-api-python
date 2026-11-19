class Weather:

    def __init__(self, city, temperature, condition, humidity):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def display_summary(self):
        print("Weather Summary")
        print("City:", self.city)
        print("Temperature:", self.temperature)
        print("Condition:", self.condition)
        print("Humidity:", self.humidity)