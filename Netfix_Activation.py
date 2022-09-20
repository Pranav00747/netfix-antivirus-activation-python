import tkinter as tk
import webbrowser
class Netfix_Activation:
 @classmethod
 def create_main_page(self):
   t_active  = tk.Tk()
   t_active.geometry("800x600+120+60")
   t_active.title("Netfix Activition")
   t_active.overrideredirect(1)
   t_active.config(bg='#0aa0b7')
   return t_active


if __name__=="__main__":
  na = Netfix_Activation()
  t = na.create_main_page()
  mainc = tk.Canvas(t, width=800, height=600, bg='#001933')
  mainc.place(x=0, y=0)
  mainc.create_rectangle(0, 0, 800, 36, fill='#330000')
  mainc.create_rectangle(0, 540, 800, 600, fill='#330000')
  topl = tk.Label(mainc, text="Netfix Antivirus Activation", bg='#330000', fg='white', font=("Arial", 12))
  topl.place(x=10, y=10)
  closec= tk.Label(mainc, text="x", bg='#330000', fg='white', font=("New Times Roman", 10))
  closec.place(x=760, y=10)
  def c_e(e):
   closec.config(fg='yellow')
  def c_l(e):
   closec.config(fg='white')
  def c_c(e):
   t.destroy()

  closec.bind('<Enter>', c_e)
  closec.bind('<Leave>', c_l)
  closec.bind('<Button-1>', c_c)
  lab1 = tk.Label(mainc, text="Enter Activation Code :", fg='white', bg='#001933', font=("Arial", 16))
  lab1.place(x=50, y=100)
  lab2 = tk.Label(mainc, text="Activation code foramt : XXXXX-XXXXX-XXXXX-XXXXX", fg='white', bg='#001933', font=("Arial", 8))
  lab2.place(x=50, y=160)
  copyright = tk.Label(mainc, text="Copyright of Netfix @Pranav", fg='white', bg='#330000', font=("Arial", 8))
  copyright.place(x=300, y=560)
  def clk_(e):
      webbrowser.open("https://www.instagram.com/elcodificadorrr_._")
  copyright.bind('<Button-1>', clk_)
  var1 = tk.StringVar()
  var2 = tk.StringVar()
  var3 = tk.StringVar()
  var4 = tk.StringVar()
  txt1 = tk.Entry(mainc, textvariable=var1)
  txt1.place(x=50, y=200)
  txt2 = tk.Entry(mainc, textvariable=var2)
  txt2.place(x=200, y=200)
  txt3 = tk.Entry(mainc, textvariable=var3)
  txt3.place(x=350, y=200)
  txt4 = tk.Entry(mainc, textvariable=var4)
  txt4.place(x=500, y=200)
  auth = tk.Label(mainc, text="", fg='white', bg='#001933', font=("Arial", 8))
  auth.place(x=50, y=340)
  def btn_c(e):
    str1 = var1.get()
    str2 = var2.get()
    str3 = var3.get()
    str4 = var4.get()
    if str1==""or str2=="" or str3=="" or str4=="":
     auth.config(fg='white')
     auth.config(text="The activation key field is empty.")
    elif str1=="pc007" and str2=="gl007" and str3=="mit07" and str4=="std07":
     auth.config(fg='yellow')
     auth.config(text="Sucesfully activated.")
    else:
     auth.config(fg='white')
     auth.config(text="Wrong key entered.")

  btnc = tk.Label(mainc, text="Activate", width=15, bg='#006666', fg='white', font=("Calibri", 12))
  btnc.place(x=50, y=260)
  def btn_e(e):
   btnc.config(bg='#003333')
   btnc.config(fg='yellow')
  def btn_l(e):
   btnc.config(bg='#006666')
   btnc.config(fg='white')
  btnc.bind('<Enter>', btn_e)
  btnc.bind('<Leave>', btn_l)
  btnc.bind('<Button-1>', btn_c)

  t.mainloop()
