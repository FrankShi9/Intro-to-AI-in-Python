class Person:
    name = ''
    age = 0
    #private attri which can not be accessed outside this class
    __weight = 0
    #constructor
    def __init__(self,n,a,w:int=50):
        self.name=n
        self.age=a
        self.__weight=w
    def __str__(self):
        print("name:{} age:{} weight:{}".format(self.name,self.age,self.__weight))

    def speak(self):
        print('my name is {}, and I am {} years old'.format(self.name,self.age))

class Student(Person):
    grade = 0
    def __init__(self, n:str, a:int,  g:int, w:int=50):
        #call super constructor
        Person.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print('my name is {}, and I am {} years old, I am in the {}th grade'.format(self.name,self.age,self.grade))

class v_logger:
    weisite = ''

Zhu = Person('Zhu', 35)
Zhu.speak()
ming = Student('ming',20,60, 12)
ming.speak()
print(ming)

listOfPeople = [Zhu, ming]
#sort people by their ages:)
print(sorted(listOfPeople, key=lambda person: person.age, reverse=True))

del ming
print(ming)