from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("awd")
root.geometry("500x500")

#สร้างหน้าต่างใหม่ เป็นหน้าจอย่อย
def showwindow():
    winow = Tk()
    winow.title("233x233")
    winow.mainloop()

# สร้างเมนู
myMenu = Menu()
root.config(menu=myMenu)
#MessageBox
def aboutpRo():
     tkinter.messagebox.showinfo("รายละเอียนโปรแกรม","com")

def exitprogram():
     confirm = tkinter.messagebox.askquestion("ยืนยัน","คุณต้องการปิดหรือไม") #เป็นการตัดสินใจ
     if confirm == "yes":
          root.deiconify()
#เพื่มเมนูย่อย
menuitem = Menu()
menuitem.add_command(label="New File",command= showwindow)
menuitem.add_command(label="open File")
menuitem.add_command(label="save File")
menuitem.add_command(label="File",command=aboutpRo)
menuitem.add_command(label="exit",command=exitprogram) #ถ้าใส่ exit ตลงๆเลยจะเป็นการออกจากโปรแกรมเลย
#เพื่มเมนู
myMenu.add_cascade(label="ไฟล์",menu=menuitem)
myMenu.add_cascade(label="ไฟล์อะไร")
myMenu.add_cascade(label="ไฟล์คือ")

root.mainloop()