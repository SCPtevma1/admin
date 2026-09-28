class Employee: #การสร้าง class
    #class varoablw
    minsalary = 12000
    maxSalary = 50000
    companyname = "ชื้อ opo"
       
    def __init__(self,name,salasry,departme):
       #instance variable
       self.__name = name
       self.__salasry = salasry
       self._departme = departme

       
    def _showData(self):
        print("ชื้อพนักงาน = "+self.__name)
        print("เงิเเดีอน = ",format(self.__salasry) )
        print("ตำหน็อง = "+self._departme)

#3 class เป็จการจัดการขข้อมูลของพนักงานตตามพระแนก
class Account(Employee):
    __departmename = "บัญชี"
    def __init__(self):
        pass

class programmer(Employee):
    __departmename = "โปรแกรมเมอร์"
    def __init__(self):
        pass

class sales(Employee):
    __departmename = "ขาย"
    def __init__(self):
        pass

Account = Account()
print(Account.companyname)

programmer = programmer()
# print(programmer._Employee__maxSalary) # Employee อ่างถึงตัว class แม่ก่อน

sales = sales()