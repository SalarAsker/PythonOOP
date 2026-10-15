class Diary:
    def __init__(self, owner: str):
        self.owner = owner
        self.__entries = []  # Internal list completely hidden from client

    @property
    def owner(self) -> str:
        return self.__owner

    @owner.setter
    def owner(self, owner: str):
        if owner != "":
            self.__owner = owner
        else:
            raise ValueError("The owner may not be an empty string")

    # Domain method: Controlled interaction with private list
    def add_entry(self, entry: str):
        self.__entries.append(entry)

    # Domain method: Formatted view of internal data
    def print_entries(self):
        print("A total of", len(self.__entries), "entries")
        for entry in self.__entries:
            print("- " + entry)

diary = Diary("Peter")
diary.add_entry("Today I ate porridge")
diary.add_entry("Today I learned object oriented programming")
diary.add_entry("Today I went to bed early")

diary.print_entries()
