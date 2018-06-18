#Data Hiding
#You need to name attributes with a double underscore prefix, and those attributes
#then are not be directly visible to outsiders.

class JustCounter:
    __secretCount = 10

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
#counter.__secretCount  Invalid access