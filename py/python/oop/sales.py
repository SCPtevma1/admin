from Employee import Employee 
class sales(Employee):
    __departmename = "ขายสิงค้า"
    def __init__(self,name,salary,area):
        super().__init__(name,salary,self.__departmename) 
        self.__area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = "+self.__area)
        print("-------------------------------")
def __str__(self):
        return (super().__str__()+" , พื้นที่รับผิดชอบ = {} " .format(self.__area) )