class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__observations = []  # Private list storing weather observations

    def add_observation(self, observation: str):
        """Adds a new observation to the end of the list."""
        if observation != "":
            self.__observations.append(observation)

    def latest_observation(self) -> str:
        """Returns the last observation added, or empty string if none exist."""
        if len(self.__observations) == 0:
            return ""
        return self.__observations[-1]

    def number_of_observations(self) -> int:
        """Returns the total number of observations recorded."""
        return len(self.__observations)

    def __str__(self) -> str:
        """Returns station summary string."""
        return f"{self.__name}, {self.number_of_observations()} observations"


# Testing the implementation
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())  # Output: Sunny

station.add_observation("Thunderstorm")
print(station.latest_observation())  # Output: Thunderstorm
print(station.number_of_observations())  # Output: 3
print(station)  # Output: Houston, 3 observations