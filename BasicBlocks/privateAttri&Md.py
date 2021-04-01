class ladies:

    def __init__(self,name:str, age:int=18):
        '''
        :param name: <str>
        '''
        self.name = name
        #age is always private for ladies
        self.__age = age


    def __secret(self)->bool:
        print('my age is '+f'{self.__age}')
        return True

    # 注意：函数的命名方式，get函数，
    # 函数的命名并不是固定的，只要是一个合法的标识符即可，
    # 但是，一般情况下，使用变量名命名，方便区分
    @property # a getter
    def age(self)->int:
        return self.__age

    @age.setter #which should not return a value
    def age(self, age:int):
        self.__age = age


Alice = ladies('Alice')
Elizabeth = ladies('Elizabeth', 22)
#print(Alice.__secret())
print(Elizabeth.age)
Elizabeth.age = 18
print(Elizabeth.age)