class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        # Add 1 second
        self.seconds += 1
        
        # Check if seconds roll over to 60
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            
            # Check if minutes roll over to 60
            if self.minutes == 60:
                self.minutes = 0

    def __str__(self):
        # :02d formats integers to be at least 2 digits long, padding with leading zeros
        return f"{self.minutes:02d}:{self.seconds:02d}"


# Testing the class
if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3600):
        print(watch)
        watch.tick()