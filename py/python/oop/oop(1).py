    # oop
# คุณสมบัติ (Attribute)
# พฤติกรรม (Method/Behavior)
#ชื้อ , เงินเดีอน
"""
class Employee: #การสร้าง class
      #สร้าง method
      def detail(self):
           self.name = "เมฆ"
           self.salasry = 50000
           print("กำหนดคุณสมบัติเรียบ = {}".format(self.name))
           print("เงิเเดีอน = {}".format(self.salasry))

     
#การสร้างวัตถุ 
emo1 = Employee()
emo1.detail()
"""
# กำหนดค่าให้ Attribute--------------------------------------------#
"""
class Employee: #การสร้าง class
      #สร้าง method
      def detail(self,name,salasry,departme):
           self.name = name
           self.salasry = salasry
           self.departme = departme

      def showData(self):
            print("ชื้อ = {}".format(self.name))
            print("เงิเเดีอน = {}".format(self.salasry)) 
            print("ตำหน็อง = {}".format(self.departme)) 


#การสร้างวัต ถุ
emo1 = Employee()
emo1.detail("เมฆ",2313," jojo")

emo2 = Employee()
emo2.detail("ออย",5000, "wdawd")

emo3 = Employee()
emo3.detail("ไม้",2313,"dwaawd*")

emo1.showData()
"""
#Constructor และ Destructor---------------------------------------#
#การสร้าง Constructor
"""
class Employee: #การสร้าง class

    def __init__(self,name,salasry,departme): # __init__ จัดให้ตรวง
       self.name = name
       self.salasry = salasry
       self.departme = departme

    def showData(self):
        print("ชื้อพนักงาน = {}".format(self.name))
        print("เงิเเดีอน = {}".format(self.salasry)) 
        print("ตำหน็อง = {}".format(self.departme))
    
#การสร้างวัตถุ  
emo1 = Employee("เมฆ",1000,"งาน") #พารามิเตอร์ emo1.showData()
emo1.name = "คน"
emo1.salasry = 33332
emo1.showData()      
emo2 = Employee("เมฆ",2000,"งาน")
emo1.name = "คน"
emo1.salasry = 33332
emo2.showData()
emo3 = Employee("เมฆ",3000,"งาน")
emo1.name = "คน"
emo1.salasry = 33332
emo3.showData()
"""
#---------------------------------------------------การห่อหุ้ม (Encapsulation)-----------------------------------------------------------#
#ไม่ใช้ __
"""
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # ตัวแปรธรรมดา ใครๆ ก็เข้าถึงได้

account = BankAccount(100)
account.balance = -9999999      # ❌ แย่แล้ว! อยู่ๆ มีคนนอกมาสั่งเปลี่ยนเงินในบัญชีติดลบได้ตรงๆ โปรแกรมพังแน่นอน
"""
# ใช้ __
"""
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # 🔒 กลายเป็น Private ด้วย __ คนนอกเข้าถึงตรงๆ ไม่ได้แล้ว

    # 1. Getter Method: ช่องทางสำหรับ "ขอดูเงิน" อย่างปลอดภัย
    def get_balance(self):
        return self.__balance

    # 2. Setter Method: ช่องทางสำหรับ "ฝาก/ถอนเงิน" แบบมีการตรวจสอบความถูกต้อง
    def deposit(self, amount):
        if amount > 0:            # ตรวจสอบก่อนว่าเงินที่ฝากต้องมากกว่า 0 บาทนะ
            self.__balance += amount
            print(f"ฝากเงินสำเร็จ! ยอดปัจจุบัน: {self.__balance}")
        else:
            print("❌ จำนวนเงินไม่ถูกต้อง!")

# --- นำไปใช้งาน ---
account = BankAccount(100)

# account.__balance = -5000  # ❌ ถ้าทำแบบนี้จะเออร์เรอร์ หรือค่าจะไม่เปลี่ยน เพราะระบบซ่อนไว้แล้ว

# ✅ วิธีใช้งานที่ถูกต้อง ต้องทำผ่านช่องทางที่เราเตรียมไว้ให้
account.deposit(500)         # ผลลัพธ์: ฝากเงินสำเร็จ! ยอดปัจจุบัน: 600
print(account.get_balance()) # ผลลัพธ์: 600
"""
