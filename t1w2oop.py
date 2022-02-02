
class Animal:
    def __init__(self, s, n):
        self._state = s
        self._size = n
    
    def feed(self):
        self._size += 1
        print(self._state, "fed")

    def getstate(self):
        return self._state
    
    def getsize(self):
        return self._size

a = Animal("little a", 3)
print(a.getsize())
a.feed()
print(a.getsize())
a.feed()
a.feed()
a.feed()
print(a.getsize())
#gjughjj