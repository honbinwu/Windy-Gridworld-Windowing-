from tkinter import *
from tkinter import messagebox
import time
import numpy as np
import random
import gc

def draw(q_table,win):
    can=Canvas(win,width=800,height=600,background="white")
    can.grid(row=0,column=0)
       
    can.create_rectangle(0,240,80,320,fill="#ccffcc")
    
    can.create_rectangle(560,240,640,320,fill="#ccccff")

    for i in range(10):
        can.create_line(i*80,0,i*80,600,fill="black")
    for i in range(8):
        can.create_line(0,i*80,800,i*80,fill="black")

    for i in range(3):
        can.create_text(40+(80*i),580,text="氣流0")
        can.create_text(280+(80*i),580,text="氣流1")

    for i in range(2):
        can.create_text(520+(80*i),580,text="氣流2")

    for i in range(1):
        can.create_text(680+(80*i),580,text="氣流1")
        can.create_text(760+(80*i),580,text="氣流0")

    for i in range(4):
       for j in range(4):
        q_table[30+i][j]-=1
    
    for i in range(2):
        for j in range(4):
            q_table[24-(9*i)][j]-=1

    q_dis = np.around(q_table.astype(float),decimals=2)

    y=[20,60,40,40]
    for i in range(70):
        if(i>0 and i%10==0):
            y=np.array(y)+80
        can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1])#上
        can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2])#下
        can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3])#左
        can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4])#右
    
    state=30
    
    count=0
    while True:
        can.create_line(40,280,280,280,fill="red")
        can.create_line(280,280,520,40,fill="red")
        can.create_line(520,40,760,40,fill="red")
        can.create_line(760,40,760,360,fill="red")
        can.create_line(760,360,680,360,fill="red")
        can.create_line(680,360,600,280,fill="red")
        break
    win.update()
    del q_table
    gc.collect()
    print("總訓練時間:",int(time.time()-start_time),"秒")
    messagebox.showinfo("訓練結束")
def update(q_table,win,state,action):
    can=Canvas(win,width=800,height=600,background="white")
    can.grid(row=0,column=0)
       
    can.create_rectangle(0,240,80,320,fill="#ccffcc")
    
    can.create_rectangle(560,240,640,320,fill="#ccccff")

    for i in range(10):
        can.create_line(i*80,0,i*80,600,fill="black")
    for i in range(8):
        can.create_line(0,i*80,800,i*80,fill="black")

    for i in range(3):
        can.create_text(40+(80*i),580,text="氣流0")
        can.create_text(280+(80*i),580,text="氣流1")

    for i in range(2):
        can.create_text(520+(80*i),580,text="氣流2")

    for i in range(1):
        can.create_text(680+(80*i),580,text="氣流1")
        can.create_text(760+(80*i),580,text="氣流0")

    q_dis = np.around(q_table.astype(float),decimals=2)

    y=[20,60,40,40]
    for i in range(70):
        if(i>0 and i%10==0):
            y=np.array(y)+80  
        if(i==state and action==1):
            can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1],fill="red",font=('Arial', 18))#上
            can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2])#下
            can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3])#左
            can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4])#右
        elif(i==state and action==2):
            can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1])#上
            can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2],fill="red",font=('Arial', 18))#下
            can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3])#左
            can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4])#右
        elif(i==state and action==3):
            can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1])#上
            can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2])#下
            can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3],fill="red",font=('Arial', 18))#左
            can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4])#右
        elif(i==state and action==4):
            can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1])#上
            can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2])#下
            can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3])#左
            can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4],fill="red",font=('Arial', 18))#右
        else:
            can.create_text(40+(80*(i%10)),y[0],text=q_dis[i][1])#上
            can.create_text(40+(80*(i%10)),y[1],text=q_dis[i][2])#下
            can.create_text(20+(80*(i%10)),y[2],text=q_dis[i][3])#左
            can.create_text(60+(80*(i%10)),y[3],text=q_dis[i][4])#右

def epsGreedy(state,q_table,epsilon,actions_list):
    greedy_act=''
    max_q=-1e10
    for i in range(1,5):
        if(q_table[state][i]>max_q):
            greedy_act=i
            max_q=q_table[state][i]
    p=[]
    for act in range(1,5):  
        if act == greedy_act:
            p.append((epsilon*1./4)+1-epsilon)
        else:
            p.append((epsilon*1./4)) 
    choice=np.random.choice(actions_list,size=1,p=p)
    return choice[0]

q_table=np.zeros([70,5],object)
for i in range (0,70):
    q_table[i][0]=i

win=Tk()
win.title('Sarsa_Windy Grid World')
win.geometry("800x700+200+50")
can=Canvas(win,width=800,height=600,background="white")
can.grid(row=0,column=0)

actions_list = ['1', '2', '3', '4']
epsilon=0.1
alpha=0.5
gamma=1

start_time=time.time()

for ep in range(250):
    print("Episode:"+str(ep+1))
    reward=-1
    state=30
    while True:
        state_now=state
        action=int(epsGreedy(state_now,q_table,epsilon,actions_list))
        if(action==1):#上
            if(state<10):
                state=state
            elif((state-3)%10==0 or (state-4)%10==0 or (state-5)%10==0 or (state-8)%10==0):#wind1
                state-=20
                if(state<0):
                    state+=10
            elif((state-6)%10==0 or (state-7)%10==0):#wind2
                state-=30
                if(state<0):
                    state+=20
            else:
                state-=10
        elif(action==2):#下 
            if(state>=60):
                state=state
            elif((state-3)%10==0 or (state-4)%10==0 or (state-5)%10==0 or (state-8)%10==0):#wind1
                state=state
            elif((state-6)%10==0 or (state-7)%10==0):#wind2
                state-=10
                if(state<0):
                   state+=10    
            else:
                state+=10
        elif(action==3):#左 
            if(state%10==0):
                state=state
            elif((state-3)%10==0 or (state-4)%10==0 or (state-5)%10==0 or (state-8)%10==0):#wind1
                state-=11
                if(state<0):
                    state+=10
            elif((state-6)%10==0 or (state-7)%10==0):#wind2
                state-=21 
                if(state<0):
                    state+=20   
            else:
                state-=1
        else:
            if(((state-9)%10)==0):
                state=state
            elif((state-3)%10==0 or (state-4)%10==0 or (state-5)%10==0 or (state-8)%10==0):#wind1
                state-=9
                if(state<0):
                    state+=10
            elif((state-6)%10==0 or (state-7)%10==0):#wind2
                state-=19 
                if(state<0):
                    state+=20 
            else:
                state+=1
        state_next=state
        if(state_next==37):
            reward=0
        action_next=int(epsGreedy(state_next,q_table,epsilon,actions_list))
        q_table[state_now][action]+=alpha*(reward + (gamma*(q_table[state_next][action_next]))-(q_table[state_now][action]))
        
        win.update()
        update(q_table,win,state_now,action)
        
        if(state_next==37):
            state=30
            break

draw(q_table,win)
win.mainloop()