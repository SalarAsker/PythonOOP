
class Notebook:
    def __init__(self):
        self._note =[]

    # Add notes
    def add_notes(self, note:str):
        self._note.append(note)

    # Retrieve note
    def retrieve_note(self, index):
        return self._note[index]

    def all_notes(self):
        return ",".join(self._note)


class NotebookPro(Notebook):
       """ A better Notebook with search functionality """
       def __init__(self):
          super().__init__()

       # Find note
       def find_notes(self, search_term):
           found = []

           for note in self._note: # This one will cause en error
               if search_term in note:
                   found.append(note)

           return found



n = NotebookPro()
n.add_notes("This is note number one")
n.add_notes("This is note number two")
print(n.all_notes())
print(n.find_notes("one"))


