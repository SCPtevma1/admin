# super
class Employee: #การสร้าง class
    #class varoablw
    minsalary = 12000
    maxSalary = 50000
    companyname = "ชื้อ opo"
       
    def __init__(self,name,salary,departme):
       #instance variable
       self.__name = name
       self.__salary = salary
       self._departme = departme

       
    def _showData(self):
        print("ชื้อพนักงาน = "+self.__name)
        print("เงิเเดีอน = ",self.__salary)
        print("ตำหน็อง = "+self._departme)

#3 class เป็จการจัดการขข้อมูลของพนักงานตตามพระแนก
class Account(Employee):
    __departmename = "บัญชี"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename)  #Super ไปเรียกใช้พาลามิตเตอร์จาก class แม่มาใช้
        super()._showData() # super ไปเรียกใช้ method จาก class แม่มาใช้

class programmer(Employee):
    __departmename = "โปรแกรมเมอร์"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename)  #Super ไปเรียกใช้พาลามิตเตอร์จาก class แม่มาใช้
        super()._showData()

class sales(Employee):
    __departmename = "ขาย"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename) 
        super()._showData()

Account = Account("เมฆ" ,20000)
programmer = programmer("ออย",30000)
sales = sales("ต้า",25000)
