from Employee import Employee 
class programmer(Employee):
    __departmename = "โปรแกรมเมอร์"
    def __init__(self,name,salary,experience,skill):
        super().__init__(name,salary,self.__departmename)
        self.__exp= experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = "+str(self.__exp))
        print("ทักษะ = "+self.__skill)
        print("-------------------------------")
def __str__(self):
        return (super().__str__()+" , ประสบการณ์ = {} ปี , ทักษะ = {} " .format(self.__exp,self.__skill) ) #ส่งค่ามา 2 ค่า
