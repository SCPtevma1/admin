# overloading
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
    def _getYearSalary(self,bonus = 0,overtime = 0):
        return (self.__salary * 12) + bonus + overtime #คำนวณรายได้ต่อปีรวมโบนัสและphet
    
    #แปลงเป็น string เป็นชุดข้อความ
    def __str__(self):
        return ("ชื้อพนักงาน  = {} , แผนก = {} , เงินเดือน ={} , รายได้ต่อปี  ={} " .format(self.__name,self._departme,self.__salary,self._getYearSalary()) )
