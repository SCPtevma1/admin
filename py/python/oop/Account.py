
from Employee import Employee 
class Account(Employee):
    __departmename = "บัญชี"
    def __init__(self,name,salary,age):
        super().__init__(name,salary,self.__departmename)  #Super ไปเรียกใช้พาลามิตเตอร์จาก class แม่มาใช้
        self.__age = age

    def _showData(self):
        super()._showData() #ก่อนที่จะเรียกใช้ method ของ class แม่ต้องเรียก super ก่อน
        print("อายุ = "+str(self.__age))
        print("-------------------------------")
    def __str__(self):
            return (super().__str__()+" , อายุ  = {} " .format(self.__age) )
