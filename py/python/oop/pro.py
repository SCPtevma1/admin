# pro.py มีหน้าที่สั่งงาน
from Account import Account
from programmer import programmer
from sales import sales

Account = Account("เมฆ" ,20000 , 23)
print("แผนกบัญชี รายได้ต่อปี: " + str(Account._getYearSalary(2000,2333))) #bonus = 2000 รวม overtime = 2333

programmer = programmer("ออย",30000 , 2 , "สร้างเว็ปไซต์")
print("แผนกโปรแกรมเมอร์ รายได้ต่อปี: " + str(programmer._getYearSalary()))

sales = sales("ต้า",25000 ,  "ภาคเหนือ")
print("แผนกขายสินค้า รายได้ต่อปี: " + str(sales._getYearSalary()))