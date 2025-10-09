class students:

    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print('accepting data')
        self.name = input("enter name")
        self.contact = input("enter contact")

    def putdata(self):
        print('the name is:'+self.name,'this is the contact:'+self.contact)

class  sciencestudent(students):

    def __init__(self,age):
        self.age = age
    def science(self):
        print('I am a science student')

rob = sciencestudent(20)
rob.science()
rob.getdata()
rob.putdata()