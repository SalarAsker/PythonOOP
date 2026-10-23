
class Notebook:
    def __init__(self):
        self.__note =[]

    # Add notes
    def add_notes(self, note:str):
        self.__note.append(note)

    # Retrieve note
    def retrieve_note(self, index):
        return self.__note[index]

    def all_notes(self):
        return ",".join(self.__note)


class NotebookPro(Notebook):
       """ A better Notebook with search functionality """
       def __init__(self):
          super().__init__()

       # Find note
       def find_notes(self, search_term):
           found = []

           for note in self.__note: # This one will cause en error
               if search_term in note:
                   found.append(note)

           return found



n = NotebookPro()
n.add_notes("This is note number one")
n.add_notes("This is note number two")
print(n.all_notes())
print(n.find_notes("one"))


