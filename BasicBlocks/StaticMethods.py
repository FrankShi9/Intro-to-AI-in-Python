class StaticMethods:
    var1 = 'value 1'
    #constructor
    def __init__(self):#self means applied on an instance
        self.var2='value 2'

    @staticmethod
    def staticmd():
        print ('静态方法，无法访问var1和var2')

    @classmethod
    def classmd(cls): #cls means applied on the class
        print ('类方法，类：' + str(cls) + '，val1：' + cls.var1 + '，无法访问an instance 中 var2的值')

#access way for a static or class method
StaticMethods.staticmd()
StaticMethods.classmd()
