# -*- coding: UTF-8 -*-
from tkinter import *
from random import *
from time import *
from tkinter.messagebox import *
import menu                                 #������һ���ļ�,ʹ����Ϸ�������˻ز˵�

global opt,bulletX,bulletY,bulletX1,billetY1#�����ӵ����������ȫ�ֱ���
opt,bulletX,bulletY=0,0,0

class  Enemy:                               #�з��ɻ���
    def __init__(self,planepicture,frame):  #�з��ɻ�����
        self.planepicture=Label(frame,image=(planepicture),bd=0)
        self.x=50
        self.y=-40+100*random()
        self.speed=level
        self.direction=randrange(3)-1
    def move1(self):                        #�ƶ�ģʽһ
        self.y=self.y+self.speed
        self.planepicture.place(x=self.x,y=self.y)
    def move2(self):                        #�ƶ�ģʽ��
        if self.x<20:
            self.direction=1
        elif self.x>480:
            self.direction=-1
        self.x=self.x+self.direction*self.speed/3
        self.y=self.y+self.speed*(0.6+0.4*random())
        self.planepicture.place(x=self.x,y=self.y)
    def copy(self):                         #���ڳ�ʼ����з��ɻ�
        self.y=self.y+50
        self.planepicture.place(x=self.x,y=self.y,anchor=CENTER)
    def reset1(self):                       #�з��ɻ���ŷɳ��ͻָ�ԭλ��һ
        if self.y>670:
            self.y=-110
            self.x=100*random()
            return self.y,self.x
    def reset2(self):                       #�з��ɻ���ŷɳ��ͻָ�ԭλ�ö�
        if self.y>670:
            self.y=-110
            self.x=130+100*random()
            return self.y,self.x
    def reset3(self):                       #�з��ɻ���ŷɳ��ͻָ�ԭλ����
        if self.y>670:
            self.y=-110
            self.x=260+100*random()
            return self.y,self.x
    def reset4(self):                       #�з��ɻ���ŷɳ��ͻָ�ԭλ����
        if self.y>670:
            self.y=-110
            self.x=300+100*random()
            return self.y,self.x
    def reset5(self):                       #�з��ɻ���ŷɳ��ͻָ�ԭλ����
        if self.y>670:
            self.y=-110
            self.x=400 +100*random()
            return self.y,self.x

class Bullet:                               #�ӵ���
    def __init__(self,planepicture,frame):  #�ӵ�����
        self.planepicture=Label(frame,image=(planepicture),bd=0)
        self.speed=20
    def move(self,X,Y):                     #�ӵ��ƶ�
        self.planepicture.place(x=X,y=Y,anchor=CENTER)
    def option(self,event):                 #�����ӵ��Ƿ����У�������h����ʱ���ܷ����ӵ�
        global bulletX,bulletY,bulletX1,bulletY1,opt,h
        if h==100:
           opt,bulletX,bulletY,h=1,bulletX1,bulletY1,0
        return opt,bulletX,bulletY,bulletX1,bulletY1
    def crasha(self,enemy):                 #�ж��ӵ���л�����
        global bulletX,bulletY
        if abs(bulletX-enemy.x)<=20 and abs(bulletY-enemy.y)<=20:
            return True
        else:return False
    def reset(self):                        #��Ϸ����ʱ�ӵ���λ
        global bulletX,bulletY
        self.planepicture.place(x=1900,y=0,anchor=CENTER)

class MyPlane:                              #�ҷ�ս������
    def __init__(self,planepicture,frame):
        self.planepicture=Label(frame,image=(planepicture),bd=0)#����ɻ�ͼ��
        self.x1=200
        self.y1=600
    def planeplace(self):                   #�趨�ɻ�λ��
        self.planepicture.place(x=self.x1,y=self.y1,anchor=CENTER)

    def zuoyi(self,event):                  #�ɻ��ƶ�����
        if self.x1>=40:
           self.planepicture.place(x=self.x1-10,y=self.y1)
           self.x1=self.x1-10
        else:return
    def youyi(self,event):
        if self.x1<=460:
           self.planepicture.place(x=self.x1+10,y=self.y1)
           self.x1=self.x1+10
        else:return
    def shangyi(self,event):
        if self.y1>=40:
           self.planepicture.place(x=self.x1,y=self.y1-10)
           self.y1=self.y1-10
        else:return
    def xiayi(self,event):
        if self.y1<=660:
           self.planepicture.place(x=self.x1,y=self.y1+10)
           self.y1=self.y1+10
        else:return
    def crasha(self,enemy):                 #�ɻ���ײ����
        if abs(self.x1 - enemy.x)<=40 and abs(self.y1-enemy.y)<=47:return -1
        else:return 1

def callback(event):                        #��;�˳�
    global stop
    answer=askokcancel('Dialog','Do you want to quit?')
    if answer:                              #��stop�����˳�
        stop=1

def show(score):                            #�÷���ʾ
    showinfo(title='score', message='Your final score is %d.\nThanks!'%(score))
    return


def main(l):                                #��������lΪmenu���ݵ��ѶȲ���
    global f,pic3,crash,score,stop,h,level
    score=0
    level=l
    root = Tk()
    f=Frame(root,width=500,height=700)
    f.pack()
    pic=PhotoImage(file='plane5.gif')       #ͼƬ����
    pic2=PhotoImage(file='plane2.gif')
    pic1=PhotoImage(file='plane1.gif')
    pic4=PhotoImage(file='Bullet.gif')
    pic5=PhotoImage(file='ming.gif')

    myplane3=MyPlane(pic,f)                #���棨����������������
    myplane3.planepicture.place(x=250,y=350,anchor=CENTER)
    bullet=Bullet(pic4,f)
    myplane=MyPlane(pic1,f)
    myplane.planepicture.place(x=myplane.x1,y=myplane.y1,anchor=CENTER)
    myplane5=MyPlane(pic5,f)
    myplane5.planepicture.place(x=65,y=630,anchor=CENTER)
    myplane6=MyPlane(pic5,f)
    myplane6.planepicture.place(x=40,y=630,anchor=CENTER)
    myplane7=MyPlane(pic5,f)
    myplane7.planepicture.place(x=15,y=630,anchor=CENTER)

    enemyplane1=Enemy(pic2,f)               #����з��ɻ����������ɻ���λ��
    enemyplane1.x=100*random()              #��һ�зɻ���enemyplane2Ϊ�����Ѷ�ɾȥ����ͬ
    enemyplane1.copy()
    #enemyplane2=Enemy(pic2,f)
    #enemyplane2.x=100+100*random()
    #enemyplane2.copy()
    enemyplane3=Enemy(pic2,f)
    enemyplane3.x=200+100*random()
    enemyplane3.copy()
    enemyplane4=Enemy(pic2,f)
    enemyplane4.x=300+100*random()
    enemyplane4.copy()
    enemyplane5=Enemy(pic2,f)
    enemyplane5.x=400+100*random()
    enemyplane5.copy()

    enemyplane6=Enemy(pic2,f)               #�ڶ��зɻ�
    enemyplane6.x=100*random()
    enemyplane6.y=-280+100*random()
    enemyplane6.copy()
    enemyplane7=Enemy(pic2,f)
    enemyplane7.x=100+100*random()
    enemyplane7.y=-280+100*random()
    enemyplane7.copy()
    #enemyplane8=Enemy(pic2,f)
    #enemyplane8.x=200+100*random()
    #enemyplane8.y=-280+100*random()
    #enemyplane8.copy()
    enemyplane9=Enemy(pic2,f)
    enemyplane9.x=300+300*random()
    enemyplane9.y=-480+100*random()
    enemyplane9.copy()
    enemyplane10=Enemy(pic2,f)
    enemyplane10.x=400+100*random()
    enemyplane10.y=-280+100*random()
    enemyplane10.copy()

    enemyplane11=Enemy(pic2,f)              #�����зɻ�
    enemyplane11.x=100*random()
    enemyplane11.y=-480+100*random()
    enemyplane11.copy()
    enemyplane12=Enemy(pic2,f)
    enemyplane12.x=100+100*random()
    enemyplane12.y=-480+100*random()
    enemyplane12.copy()
    enemyplane13=Enemy(pic2,f)
    enemyplane13.x=200+100*random()
    enemyplane13.y=-480+100*random()
    enemyplane13.copy()
    #enemyplane14=Enemy(pic2,f)
    #enemyplane14.x=300+100*random()
    #enemyplane14.y=-480+100*random()
    #enemyplane14.copy()
    enemyplane15=Enemy(pic2,f)
    enemyplane15.x=400+100*random()
    enemyplane15.y=-480+100*random()
    enemyplane15.copy()
    lista=[enemyplane1,enemyplane3,enemyplane4,enemyplane5,enemyplane6,enemyplane7,
           enemyplane9,enemyplane10,enemyplane11,enemyplane12,enemyplane13,enemyplane15]

    crash,life,stop,score,h=1,3,0,0,0       #stop:�����˳���־   h��������

    f.bind("<Left>" ,myplane.zuoyi)         #�ҷŷɻ�ָ������
    f.bind("<Right>" ,myplane.youyi)
    f.bind("<Up>" ,myplane.shangyi)
    f.bind("<Down>" ,myplane.xiayi)
    score1=Label(f,text='score:',fg='red',bg='black')
    score1.place(x=415,y=23,anchor=SW)      #������ʾ
    score2=Label(f,text=score,fg='red',bg='black')
    score2.place(x=455,y=23,anchor=SW)
    enegy1=Label(f,text='enegy:',fg='red',bg='black')
    enegy1.place(x=435,y=650,anchor=SW)     #������ʾ
    enegy2=Label(f,text=h,fg='red',bg='black')
    enegy2.place(x=475,y=650,anchor=SW)


    for i in range(1000000) :               #��ѭ��

        score2.config(text=score)
        score2.place(x=455,y=23,anchor=SW)
        enegy2.config(text=h)
        enegy2.place(x=475,y=650,anchor=SW)
        score+=1
        f.bind('<Key-p>',callback)          #�趨P��ͣ

        if h<100:                           #�趨��������
            h+=1

        if (crash==-1 and life==0) or stop==1:  #�趨��Ϸ��������
            show(score)
            root.quit()
            root.destroy()
        if life==2:
            myplane5.planepicture.place(x=-65,y=630,anchor=CENTER)
        if life==1:
            myplane6.planepicture.place(x=-40,y=630,anchor=CENTER)


        global bulletX,bulletY,bulletX1,bulletY1
        bulletX1,bulletY1=myplane.x1,myplane.y1

        if h==100:f.bind("<space>" ,bullet.option)#�����ӵ�
        if opt==1:
            bullet.move(bulletX,bulletY)
            bulletY=bulletY-bullet.speed
        f.focus_set()
        f.pack()


        if life>0:                          #�з��ɻ��ƶ�
          for j in range(len(lista)) :
            crash=1
            crash=myplane.crasha(lista[j])
            if score<=1000:                 #��������1000ʱģʽһ
                lista[j].move1()

            elif score>1000:                #��������1000��ģʽ��
                if j%2==0:
                    lista[j].move2()
                else:
                    lista[j].move1()

            if crash!=1:
                life-=1
                lista[j].x=-100
            if bullet.crasha(lista[j]):
                lista[j].x=-100
                score+=100
            if j%4==0:
                lista[j].reset1()
            elif j%4==1:
                lista[j].reset2()
            elif j%4==2:
                lista[j].reset4()
            elif j%4==3:
                lista[j].reset5()

        else:                               #��Ϸ����
            myplane7.planepicture.place(x=-40,y=630,anchor=CENTER)
            bullet.reset()
            bulletX,bulletY=900,0
            show(score)
            root.quit()
            root.destroy()
            menu.main()

        root.update()
        w=0.02
        sleep(w)
        root.update()

    root.mainloop()

if __name__=="__main__":
    main(1)
