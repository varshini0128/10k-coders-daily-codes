class myclass:
    __hiddenvariable = 0

    def add(self, increment):
        self.__hiddenvariable += increment
        print(self.__hiddenvariable)



objectone = myclass()
objectone.add(5)
print(objectone.__hiddenvariable)