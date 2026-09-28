# การprimt
"""
x,y= 10,3
print("x =",x)
print("y =",y)
x%=y # x = x-y
print("ผลลับ",x)
""" ""

# ตัวดำนเินการเผรียบเทียบ
"""''
x,y = 100,50
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
""" ""
# --------------------------------------คำสั่งเงื่อนไข if elif else---------------------------------------------------#
# คำสั่งเงื่อนไข
# if: เงื่อนไขแรกสุดที่โปรแกรมจะตรวจสอบเสมอ
# elif: ย่อมาจาก "else if" ใช้เช็คเงื่อนไขเพิ่มในกรณีที่เงื่อนไขก่อนหน้าเป็นเท็จ สามารถมีกี่ตัวก็ได้
# else: เงื่อนไขสุดท้าย ทำงานเมื่อทุกเงื่อนไขด้านบนเป็นเท็จทั้งหมด (ไม่ต้องใส่เงื่อนไขต่อท้าย)
"""''
score = int(input("ป่อนตะแนนสอบ:"))
print("คะนแนสอบของคุณ=",score)

if score<0:
    print("คะแนนไม่ถูกต้อง")
if score>=50:
    print("สอบผ่าน")
else:
    print("สอบไม่ผ่าน")
""" ""
# กำหนดเงื้อนใข 2 เงื้อนใข
"""''
number = int(input("ป้อนตัวเลขของคุณ"))
print("ตัวเลขของคุณ ตือ ",number)
print("คู่") if number%2==0 else print("คี")
""" ""

# ตัวดำเนินการทางตรรกศาสตร์
"""
USERNAME = input("ป้อนชื่อผู้ใช้:")
password = input("ป้อนรหัสผ่าน:")

if USERNAME =="admin" or password =="1234": # ถ้าเงื้อนใขใดเงื้อนใขหนึ่งเป็นจริงจะทำงาน
       print("ยินดีต้อนรับเข้าสู่ระบบ")    
else:
        print ("ข้อมูลไม่ถูกต้อง")
"""
# not จะเป็นการปฏิเสธเงื้อนใข
"""
USERNAME = input("ป้อนชื่อผู้ใช้:")

if not USERNAME =="admin": # ใช้ != ได้
       print("ยินดีต้อนรับเข้าสู่ระบบ")    
else:
        print ("ข้อมูลไม่ถูกต้อง")
"""

# ตัดเกรด
"""

score = int(input("ป้อนคะแนนสอบ:"))
print("คะแนนสอบของคุณ=",score)
grade = None

if score >= 80 and score<=100:
    grade = "a"
elif score>=70 and score<=79:
    grade = "b" 
elif score>=0 and score<=69:
    grade = "f"
else:
    print("คะแนนไม่ถูกต้อง")   

print("เกรดของคุณ=",grade)
"""

# nested-if
"""
name = input("ป้อนชื่อของคุณ:")
password = input("ป้อนรหัสผ่าน:")

if name == "membr" and password == "1234":  # if หลัก
    print("เข้าสู่ระบบสำเร็จ")
    service = input("คุณต้องการใช้บริการอะไร:")
    if service == "1":  # if ซ้อน
        print("ถอนเงิน")
    elif service == "2":
        print("ฝากเงิน")
    else:
        print("บริการไม่ถูกต้อง")
else:
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
"""
# ----------------------------------------------------------------การใช้ if แบบย่อ----------------------------------------------------------#
# Match Statement match-case
"""

service = input("ป้อนบริการที่ต้องการใช้(1-3):")

match service:
    case "1":
        print("ถอนเงิน")
    case "2":
        print("ฝากเงิน")
    case "3":
        print("สอบถามยอดเงินคงเหลือ")
    case "":
        print("บริการไม่ถูกต้อง")
"""
# คำสั่งทำซ้ำ while loop
"""
counter = 0
while counter < 3:
    counter += 1
    print("ตัวนับ =", counter)
print("จบการทำงาน")
"""
# คำสั่งทำซ้ำ for loop
"""
for i in range(10, 0, -1):
    print(i)
"""
# loop
# break / continue
"""
for i in range(1, 11):
    # if i == 5:
    #    continue  # ข้ามการทำงานในรอบนั้นๆ และไปทำงานในรอบถัดไป
    print(i)
print("จบงาน")
"""
# แม่สูดคูณ
"""
number = int(input("ป้อนตัวเลขที่ต้องการดูแม่สูตรคูณ:"))
for i in range(1, 13):
    print(number, "x", i, "=", number * i)
"""
# หารผลรวมของตังเชย 5 จำนวน
"""
total = 0
for i in range(1, 6):
    number = int(input("ลำดับที่" + str(i) + ": "))
    total += number

print("ผลรวม =", total)
"""
# หาผลรวมของตัวเลขไมม่กำจัดจำนวน
"""
total = 0
while True:
    nmeber = int(input("ป่อนตัวเลข"))
    if nmeber <= 0:  # ถ้าพิมเลข 0 จะจบการทำงาน print ("จบการทำงาน")
        break  # เบก
    total += nmeber
print("ผลรวม = ", total)
"""
# Nested-loop ลูปซ้อนลูป
"""
for i in range(2):  # loop ลูปนอก
    print(i)
    for j in range(3):  # loop ลูปใน
        print(j)
"""
# แม่สูคคูณแบบกำหนดช่วง
"""
start = int(input("แม่าสูตรคูณเรื้มต้น"))
end = int(input("แม่าสูตรคูณสุดท้าย"))

for numcer in range(start, end + 1):  # 2-5
    print("แม่อะไร = ", numcer)
    print("-----------------------")
    for i in range(1, 13):
        print(numcer, "x", i, "=", numcer * i)
        #       9      x   10  =     90
"""
# ----------------------------------------การเจาะลึกการใช้ String----------------------------------------------------------#

# การเจาะลึกการใช้ String
"""
ya = "เมฆ "
yy = "ธานินทร์ คำพิทูล"
fav = ya + yy + "อายุ 20" 

print(fav)
"""
# String แบบหลายบรรทััด
"""
fname = "เมฆ "
lname = "ธานินทร์ คำพิทูล "

fullname = (
    fname + lname + "CEO"
)  # fullname ใช้เป็นตัวแปล ของ fname + lname ที่เอามาบกต่อกัน 
# 
print(fullname)
"""
# จัดรูปแบบ String (Format String)
"""
year = 2548
salar = 22223300
mesas = f"เกินหมือปี พ.ศ{year}"
age = f"ปี่นี่คูณอายุเท่าไร{2569-year} ปี่"
ga = f"เงินเดียน = {salar: .2f}"
print(ga)
"""
# การเข้าถึงตัวอักษณใน String (Slice)
"""
text = "HalloPython"
print(text[-8:-4])
"""
# ฟังชั้นจัดการ Stying
"""
name = input("ป้อนเดีอน")

if name.encode("คม"):
    print("เดียนนี่มี 31 วัน")
elif name.encode("ยน"):
    print("เดือนนี่มี 30 วัน")
"""
# ฟังชั้นจัดการ String
"""
text = "ฉันชื้อ {} อายุ {} ปี".format(
    "เมฆ",
    20,
)
print(text)
"""
# ------------------------------ชนินข้อมูลแบบ Data Type----------------------------------------------------------#
"""
product = ["กางเกง", "เสื้อ", "กางเกง", "เสื้อ", "กางเกง", 23.32, True]

product[0] = "กางเกง"
product[1] = 543
# การเข้าถึงสมาชิก
for i in product:
    print(i)
"""
"""
color = ["แดง", "red", "เขียว", "green", "น้ำเงิน", "blue"]
colors = list(("ข้าว", "ฟ่า", "ส้ม"))

data = color + colors
print(type(data))
"""
"""
color = ["แดง", "เขียว", "น้ำเงิน", "blue"]
print(color[:3] )  # 0-2 การำหนดช้วงของการเข้าถึงสมาชิก
"""
# --------------------------------ฟังชั้นจัดการลัสต์ (List)----------------------------------------------------------#
"""
colors = [
    13,
    3,
    2,
    43,
    24,
    30,
    20,
    34,
    33,
]
colors.sort()
colors.reverse()
print(colors)
"""
# ----------------------------------------ทูเพิล (Tuple)----------------------------------------------------------#
"""
product = (
    "กางเกง",
    "เสื้อ",
    23.32,
)
for i in product:
    print(i)
"""
"""
colors1 = ("แดง","เขียว","น้ำเงิน",)
colors2 = tuple(("ข้าว", "ฟ้า", "ส้ม"))
data = colors1 + colors2
print(data * 2)
"""
"""
colors1 = ("แดง","เขียว","น้ำเงิน","ฟ้า","ส้ม")
print(colors1.count("แดง"))
"""
# ----------------------------------------เซ็ต (Set)----------------------------------------------------------#
"""
scole = {"บ้าน", "บ้าน", "โรงเรียน", "ที่ทำงาน", "บ้าน", "โรงเรียน"}
scole.add("สวนสาธารณะ")
scole.update(("ที่ทำงาน",))

pets = set(("แมว", "สุนัข", "กระต่าย","บ้าน", "บ้าน",))
print(scole)
print(pets) 

data = scole.intersection(pets)  # รวมเซ็ต
print(data)
"""
#----------------------------------------Dictionary----------------------------------------------------------#
"""
borel ={
    "name": "เมฆ",
    "age": 20,
    "job": "นักศึกษา",
}
confirm={
    True:"ตกลง",
    False:"ลงเล็ก"
} 
moubth={
    1:"มกราคม",
    2:"กุมภาพันธ์",
    3:"มีนาคม",
}
numbcre={
    "เลขคู่":[2,4,6,8],
    "เลขคี่":[1,3,5,7,9],
}
print(numbcre["เลขคู่"])
"""
#----------------------------------------ฟังชั้นจัดการ Dictionary----------------------------------------------------------#
"""
colors={
    "red":"สีแดง",
    "green":"สีเขียว",
    "blue":"สีน้ำเงิน",
}
maincolor = colors.copy(  )
colors.update({"dw":"สัม"})
colors.update({"red":"แดงเข็ม"})
print (colors)
# for key,values  in colors.items():
#    print(values, "=", values)
"""
#---------------------------------------ตัวดำเนินการเอกลักษณ์-----------------------------------------------------------#
"""
colorA=["สีแดง","ฟ้า","ขาว"]
colorB=["สีแดง","ฟ้า","ขาว"]
data= colorA

print(colorA is not data)
print(colorA is not colorB)
"""
"""
coloree=["1","2","2","3","4"]
print("1" in coloree)
print("0" not in coloree)
"""
#--------------------------------------Pattern Matching-------------------------------------------------------------#
"""
servl=3
match servl:
    case 1:
        print("ฟากเงิน")
    case 2:
        print("ถอน")
    case 3:
        print("สอบถามการบริการเพื่มเต็ม")
    case servl:
        print("ไม่มีบริการ{servl} ในระบบกรุณาทำรายการใหม่มีครัง")
"""
#Guard
"""
sfe= int(input("ป้อนคะแนนของคุณ (0-100):"))
print("คะแนนของคุณ คือ",sfe)
match sfe:
    case 100:
        print("สอบได้คะแนนเต็ม")
    case sfe if sfe >=50 and sfe<100:
        print("ผ่านกเ็นการสอบ")
    case _  :
        print("คะแนนไม่อยู่ในเกรดที่กำหนด")
"""
#OR Pattern
"""
data =input("ป้อนคำนำหน้าชื้ออของคูณ")

match data:
    case "เด็กชาย" | "นาย":
        print("เป็นเด็กผู้ชาย")
    case "เด็กหณิง" | "นาง":
        print("เป็นเด็กผู้หณิง")
    case _:
        print("ไม่ผบข้อมูล")
"""
#Sequence Pattern
"""
data=[1,2,3]
match data:
    case ():
        print("ไม่ม้อมูยในdata")
    case (1,2):
        print("มีข้อมูล 2 คือ 1 และ 2")
    case (1,2,3):
        print("มีข้อมูล 3 คือ 1 , 2 และ 3")
"""
#Mapping Pattern
"""
custome=[
    {"name":"ก้อง","type":"general"},
    {"name":"โก้อ","type":"membre"},
    {"name":"ก้มด","type":"general"}
]
id=int(input("ป่อนรหัสลูกต้า"))
print(f"สวัสกีลูกค้า {id} :{custome[id] ["name"]}")

data={"name":"ก้อง","type":"general"}
match custome [id]:
    case {"type":"membre"}:
        print("เป็นสมาชิกได้รับสวนลด 40%")
    case _:
        print("ไม่ได้รับสวดลด")
"""
#--------------------------------------#การสร้างฟังก์ชั่น (Function)-------------------------------------------------------------#
"""
def sayHello():
    print("สวัสดีครับ")

def showTable():
    print("--------------")
    for i in range(1,13):
            print(f"2 x {i} = {2*i}")

# เรียกใช้งาน def ให้แสดงออกมา
sayHello()
showTable()
"""
# ฟังก์ชั่นแบบกำหนดค่าเริ่มต้น------------------------------------------#
"""
def sayHello(time,username,age):#parametes
    print("สวัสดีครับ ",time,username)
    print("ปีนี่คูณมีอายุ",age ,"ปี")

def saveEmployee(name,depatment,salary):
        print(f"ชื้อ {name}, แผง {depatment}")
        print(f"เงินเดียน {salary} บาท")
        print("------------------")

def showTable(num):
    print(f"-------แม่ {num}-------")
    for i in range(1,13):
            print(f"{num} x {i} = {2*i}")


# เรียกใช้งาน def ให้แสดงออกมา        
# mytime="ตอนเช้า"
# sayHello(mytime,"เมฆ",23)#arguments
# sayHello(mytime,"ddde",42)
# showTable(2)
# showTable(3)
# howTable(5)
# saveEmployee("เมฆ","ไอที","300000")
"""
#ฟังก์ชั่นแบบกำหนดค่าเริ่มต้น------------------------------------------#

"""
def saveEmployee(name,depatment,salary=30000):
        print(f"ชื้อ {name}, แผง {depatment}")
        print(f"เงินเดียน {salary} บาท")
        print("------------------")

# เรียกใช้งาน def ให้แสดงออกมา    
saveEmployee("เมฆ","ไอที")
saveEmployee("เมฆ","ความมังคง","350000")
saveEmployee("เมฆ","ไอที","320400")
"""
#-------------------------------------------------Arguments (args & kwargs)--------------------------#
# ข้อมูลแบบลำดีบ *args
# ข้อมูลแบบกำหนดขื้อ **kwargd
"""
def saveEmployee(**kwargd): #tuple
        print(f"ชื้อ {kwargd["name"]}, แผง {kwargd["department"]}")
        print(f"เงินเดียน {kwargd["salsry"]} บาท")
        print(f"ที่อยู่ {kwargd["conutry"]}")
        print("------------------")


# เรียกใช้งาน def ให้แสดงออกมา    
saveEmployee(name="เมฆ", department="ไอที",salsry= "1323", conutry="us")
saveEmployee(name="เมฆ",department="ความมังคง",salsry= "350000",conutry="sc")
saveEmployee(name="เมฆ",department="ไอที",salsry= "320400",conutry="scawd")
"""
#------------------------------------------------- ฟังชั้นแบบมีค่าส่งกลับ --------------------------#
#retuyn function
"""
def getCapital():
    return "กรุงเทพมหานคร"
def getPI():
    return 3.14

# area = PI * retuturn ^ 2
radius = 5
getPI()*radius**2
print("พื้นที่วงกลอม =",getPI,"ตาลองเมต") 
"""
# myData = getCapital()
# print("เมืองหลวงของฉัน", myData)
#----------------------------------------------------------ฟังก์ชั่นแบบรับและส่งค่า-------------------#
"""
def checknuber(number):
    if number%2==0:
        return "เลขคู่"
    else:
        return "เลขคี่"

def summation(*data):    
    total=0
    for item in data:
        total+=item
    return total
"""
# result = checknuber(10)
# print("ผลลัพ = ",result)
# print(summation(10,20))
# print(summation(10,20,30))
# print(summation(10,20,30,40,50,60))

#--------------------------------------Lambda Function---------------------------------------#
#Lambda Function 2^3
# def power(base,n):
#   return base**n
"""
result = lambda base,n : base*n
print("ผลลับ = ",result(2,4))
print("ผลลับ = ",result(5,2))
"""
#----------------------------------------ขอบเขตตัวแปร------------------------------------------#
"""
balance=1000 #global
def displayBalance():
    print("ยอดเงินคงเหลือในบัณชี",balance,"บาท")

def deposit(value):
    global balance
    money=value #local
    print("ฝากเเงินจำนวน",money,"บาท")
    balance+=money

def withdaraw(value):
    global balance
    amount=value
    print("ถอนเงินจำนวน",amount,"บาท")
    balance-=amount
"""
# displayBalance()
# deposit(200)
# withdaraw(900)
# displayBalance()

#Return = ลีเทน Keyword----------------------------------#
"""
balance=1000 #global
def displayBalance():
    print("ยอดเงินคงเหลือในบัณชี",balance,"บาท")

def deposit(value):
    global balance
    money=value #local
    print("ฝากเเงินจำนวน",money,"บาท")
    if(money<=0):
        print("ไม่สามารถฟากเงินได้")
        return
    balance+=money

def withdaraw(value):
    global balance
    amount=value
    print("ถอนเงินจำนวน",amount,"บาท")
    if amount<=0 or amount>balance:
        print("ERROR ไม่สามารถถอนเงินได้")
        return
    balance-=amount
"""
# displayBalance()
# withdaraw(1000)
# displayBalance()
#-------------------------------------------------------------Exception-----------------------------------#
#try:
#except ประเถทException:
#finally #คำสั่งต่างๆ
"""
try:
 number1=int(input("ป้อานตัวเลข 1:"))
 number2=int(input("ป้อานตัวเลข 2:"))
 result = number1/number2
 print("ผลลับ = ", result)

except ValueError:
     print("ข้อมูลไม่าถูกต้อง กรุณาป้อนข้อูลดเฉพาะตัวเลขเท้านั้น!")
except ZeroDivisionError:
      print("หารด้วยศูนไม่ได้! เนื้องจากไม่ถูกนิยามในทางคณิตศาสตร์")
finally:
     print("-----------------")
     print("End program")
     print("-----------------")
"""
"""
try:
 number1=int(input("ป้อานตัวเลข 1:"))
 number2=int(input("ป้อานตัวเลข 2:"))
 if number1<0 or number2<0:
     raise Exception ("ข้อมูลตัวเลขต้องเป็นค่าบวกเท่าทั้น")
 result = number1/number2
 print("ผลลับ = ", result)

except ValueError:
     print("ข้อมูลไม่าถูกต้อง กรุณาป้อนข้อูลดเฉพาะตัวเลขเท้านั้น!")
except ZeroDivisionError:
      print("หารด้วยศูนไม่ได้! เนื้องจากไม่ถูกนิยามในทางคณิตศาสตร์")

finally:
     print("-----------------")
     print("End program")
     print("-----------------")
"""