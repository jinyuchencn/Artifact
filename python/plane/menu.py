# -*- coding: UTF-8 -*-
from tkinter import*
from tkinter.messagebox import*
import plane                        #导入plane以运行游戏

def start():                        #开始游戏
    global l
    root.quit()
    root.destroy()
    plane.main(l)

def help():                         #游戏帮助
    showinfo(title='Plane', message='1.利用键盘控制战机,左键代表左移,右键代表右移,上键代表上移,下键代表下移。\n2.小心不要让敌军飞机伤害你！否则你会失去一条生命,\
你只有三条宝贵的生命！生命会在左下角显示。\n3.你可以使用炮弹攻击敌军飞机，利用空格键释放一颗炮弹。\n4.炮弹的释放需要积累100点能量，释放一次炮弹能量将归零。\
能量的积累会在右下角显示。\n5.摧毁一架敌军飞机可以得5分，存活时间越长你的成绩也会相应增加，成绩会在右上角显示。\n6.你可以随时通过alt键暂停。\n7.你可以随时通过P键\
退出这场战斗。\n祝你好运！')
    return

def quit():                         #退出游戏
    root.destroy()

def setleveleasy():                 #选择游戏难度
    global l,Button4,Button5,Button6
    l=3
    Button4.config(bg="red")
    Button5.config(bg="orange")
    Button6.config(bg="orange")
def setlevelnormal():
    global l,Button4,Button5,Button6
    l=5
    Button4.config(bg="orange")
    Button5.config(bg="red")
    Button6.config(bg="orange")
def setlevelhard():
    global l,Button4,Button5,Button6
    l=8
    Button4.config(bg="orange")
    Button5.config(bg="orange")
    Button6.config(bg="red")

def main():                     #界面设置
    global label,root,l,Button4,Button5,Button6
    l=5                         #难度默认normal
    root=Tk()
    root.title('plane')
    img=PhotoImage(file='menu.gif')
    label=Label(root,width=500,height=700,image=img)
    label.pack()
    Button1=Button(label,relief = FLAT,bg = "orange",text='Start',font=('Arial', 30),command=start).place(x=130,y=160,anchor=S)
    Button2=Button(label,relief = FLAT,bg = "orange",text='Help',font=('Arial', 30),command=help).place(x=130,y=350,anchor=S)
    Button3=Button(label,relief = FLAT,bg = "orange",text='Quit',font=('Arial', 30),command=quit).place(x=130,y=530,anchor=S)
    Button4=Button(label,relief = FLAT,bg = "orange",text='easy',font=('Arial', 20),command=setleveleasy)
    Button4.place(x=100,y=650,anchor=S)
    Button5=Button(label,relief = FLAT,bg = "red",text='normal',font=('Arial', 20),command=setlevelnormal)
    Button5.place(x=240,y=650,anchor=S)
    Button6=Button(label,relief = FLAT,bg = "orange",text='hard',font=('Arial', 20),command=setlevelhard)
    Button6.place(x=380,y=650,anchor=S)
    mainloop()
if __name__=="__main__":
    main()
