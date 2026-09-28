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

       #แสดงรายละเอียดของพนักงาน
    def _showData(self):
        print("ชื้อพนักงาน = "+self.__name)
        print("เงิเเดีอน = ",self.__salary)
        print("ตำหน็อง = "+self._departme)

    # รานได้ต่อปี
    def _getYearSalary(self):
        return self.__salary * 12
    #แปลงเป็น string เป็นชุดข้อความ
    def __str__(self):
        return ("ชื้อพนักงาน  = {} , แผนก = {} , เงินเดือน ={} , รายได้ต่อปี  ={} " .format(self.__name,self._departme,self.__salary,self._getYearSalary()) )

#3 class เป็จการจัดการขข้อมูลของพนักงานตตามพระแนก
class Account(Employee):
    __departmename = "บัญชี"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename)  #Super ไปเรียกใช้พาลามิตเตอร์จาก class แม่มาใช้

class programmer(Employee):
    __departmename = "โปรแกรมเมอร์"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename)  #Super ไปเรียกใช้พาลามิตเตอร์จาก class แม่มาใช้


class sales(Employee):
    __departmename = "ขาย"
    def __init__(self,name,salary,):
        super().__init__(name,salary,self.__departmename) 


Account = Account("เมฆ" ,20000)
print(Account.__str__())
programmer = programmer("ออย",30000)
print(programmer.__str__())
sales = sales("ต้า",25000)
print(sales.__str__())