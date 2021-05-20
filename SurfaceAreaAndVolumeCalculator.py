from tkinter import *
from math import pi as p
from tkinter import messagebox
from tkinter.messagebox import showinfo

root=Tk()
root.title('MATHS')

frame1=Frame(root,width='600',height='50',bg='black')
frame1.grid(row=0,column=0,sticky='ew')

l1=Label(frame1,text='MATHEMATICS',font=('Algerian',29),bg='black',fg='white')
l1.pack(fill=BOTH)

frame2=Frame(root,width='600',height='300',bg='violet')
frame2.grid(row=1,column=0,sticky='ew')

for i in range(3):
    frame2.columnconfigure(i,weight=1)

iframe1=Frame(frame2,width='100',height='300',bg='green') 
iframe1.grid(row=0,column=0,sticky='nsw')
    
iframe2=Frame(frame2,width='420',height='300',bg='violet')
iframe2.grid(row=0,column=1,sticky='nsew')

iframe3=Frame(frame2,width='80',height='300',bg='green')
iframe3.grid(row=0,column=2,sticky='e')

for i in range(3):
    iframe2.columnconfigure(i,weight=1)
for i in range(3):
    iframe1.columnconfigure(i,weight=1)
    
l2=Label(iframe2,text='Shape',font=('Times New Roman',12),bg='violet',fg='black')
l2.grid(row=1,column=0,sticky='ew')

cvar=StringVar()  
cvar.set('Select')
shapes=('Circle','Square','Rectangle','Cube','Cuboid','Solid Cylinder','Hollow Cylinder','Cone','Solid Sphere','Hollow Sphere','Solid Hemisphere','Hollow Hemisphere','Frustum')    
om1=OptionMenu(iframe2,cvar,*shapes)  
om1.grid(row=1,column=1,sticky='e')
om1.config(width='23')

frame3=Frame(root,width='600',height='50',bg='black')
frame3.grid(row=2,column=0,sticky='ew')

def Next():
    global e1,e2,e3,e4,e5,e6,e7,e15,e16
    if cvar.get()=='Circle':
        l3=Label(iframe2,text='Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='Circumfrence',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=3,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=3,column=1,sticky='e')
        
        l5=Label(iframe2,text='Area',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=4,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=4,column=1,sticky='e')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=5,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=5,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Square':
        l3=Label(iframe2,text='Side',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='Perimeter',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=3,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=3,column=1,sticky='e')
        
        l5=Label(iframe2,text='Area',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=4,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=4,column=1,sticky='e')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=5,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=5,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Rectangle':
        l3=Label(iframe2,text='Length',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l6=Label(iframe2,text='Width',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=3,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=3,column=1,sticky='e')
        
        l4=Label(iframe2,text='Perimeter',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=4,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=4,column=1,sticky='e')
        
        l5=Label(iframe2,text='Area',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Cube':
        l3=Label(iframe2,text='Side',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l7=Label(iframe2,text='Perimeter',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=3,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=3,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=4,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=4,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=6,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=6,column=1,sticky='e')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Cuboid':
        l3=Label(iframe2,text='Length',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l7=Label(iframe2,text='Perimeter',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=6,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=6,column=1,sticky='e')
        
        temp=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        temp.grid(row=7,column=0,sticky='ew')
        e15=Entry(iframe2,width=30)
        e15.grid(row=7,column=1,sticky='e')
        
        temp1=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='ew')
        e16=Entry(iframe2,width=30)
        e16.grid(row=8,column=1,sticky='e')
        
        l8=Label(iframe2,text='Width',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=3,column=0,sticky='ew')
        e6=Entry(iframe2,width=30)
        e6.grid(row=3,column=1,sticky='e')
        
        l9=Label(iframe2,text='Height',font=('Times New Roman',12),bg='violet',fg='black')
        l9.grid(row=4,column=0,sticky='ew')
        e7=Entry(iframe2,width=30)
        e7.grid(row=4,column=1,sticky='e')
        
    elif cvar.get()=='Solid Cylinder':
        l3=Label(iframe2,text='Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=4,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=4,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=6,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=6,column=1,sticky='e')
        
        l7=Label(iframe2,text='Height',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=3,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=3,column=1,sticky='e')    
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Hollow Cylinder':
        l3=Label(iframe2,text='Outer Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=5,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=5,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=6,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=6,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=7,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=7,column=1,sticky='e')
        
        l7=Label(iframe2,text='Height',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=4,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=4,column=1,sticky='e') 
        
        l8=Label(iframe2,text='Inner Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=3,column=0,sticky='ew')
        e6=Entry(iframe2,width=30)
        e6.grid(row=3,column=1,sticky='e')    
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
    elif cvar.get()=='Cone':
        l3=Label(iframe2,text='Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=5,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=5,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=6,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=6,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=7,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=7,column=1,sticky='e')
        
        l7=Label(iframe2,text='Height',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=4,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=4,column=1,sticky='e') 
        
        l8=Label(iframe2,text='Slant Height',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=3,column=0,sticky='ew')
        e6=Entry(iframe2,width=30)
        e6.grid(row=3,column=1,sticky='e')    
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')      
        
    elif cvar.get()=='Solid Sphere':
        l3=Label(iframe2,text='Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='Surface Area',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=3,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=3,column=1,sticky='e')
        
        l5=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=4,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=4,column=1,sticky='e')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=5,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=5,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Hollow Sphere':
        l3=Label(iframe2,text='Outer Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l6=Label(iframe2,text='Inner Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=3,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=3,column=1,sticky='e')
        
        l4=Label(iframe2,text='Surface Area',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=4,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=4,column=1,sticky='e')
        
        l5=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')    
        
    elif cvar.get()=='Solid Hemisphere':
        l3=Label(iframe2,text='Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=3,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=3,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=4,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=4,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=5,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=5,column=1,sticky='e')
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=6,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=6,column=1,sticky='nsew')
      
    elif cvar.get()=='Hollow Hemisphere':
        l3=Label(iframe2,text='Outer Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=4,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=4,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=5,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=5,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=6,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=6,column=1,sticky='e')
        
        l7=Label(iframe2,text='Inner Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=3,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=3,column=1,sticky='e')    
        
        temp1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        temp1.grid(row=8,column=0,sticky='nsew')
        te1=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        te1.grid(row=8,column=1,sticky='nsew')
        
        l8=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=7,column=0,sticky='nsew')
        e6=Label(iframe2,text='',font=('Times New Roman',12),bg='violet',fg='black')
        e6.grid(row=7,column=1,sticky='nsew')
        
    elif cvar.get()=='Frustum':
        l3=Label(iframe2,text='Outer Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l3.grid(row=2,column=0,sticky='ew')
        e1=Entry(iframe2,width=30)
        e1.grid(row=2,column=1,sticky='e')
        
        l4=Label(iframe2,text='CSA',font=('Times New Roman',12),bg='violet',fg='black')
        l4.grid(row=6,column=0,sticky='ew')
        e2=Entry(iframe2,width=30)
        e2.grid(row=6,column=1,sticky='e')
        
        l5=Label(iframe2,text='TSA',font=('Times New Roman',12),bg='violet',fg='black')
        l5.grid(row=7,column=0,sticky='ew')
        e3=Entry(iframe2,width=30)
        e3.grid(row=7,column=1,sticky='e')
        
        l6=Label(iframe2,text='Volume',font=('Times New Roman',12),bg='violet',fg='black')
        l6.grid(row=8,column=0,sticky='ew')
        e4=Entry(iframe2,width=30)
        e4.grid(row=8,column=1,sticky='e')
        
        l7=Label(iframe2,text='Height',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=5,column=0,sticky='ew')
        e7=Entry(iframe2,width=30)
        e7.grid(row=5,column=1,sticky='e') 
        
        l8=Label(iframe2,text='Slant Height',font=('Times New Roman',12),bg='violet',fg='black')
        l8.grid(row=4,column=0,sticky='ew')
        e6=Entry(iframe2,width=30)
        e6.grid(row=4,column=1,sticky='e')        
        
        l7=Label(iframe2,text='Inner Radius',font=('Times New Roman',12),bg='violet',fg='black')
        l7.grid(row=3,column=0,sticky='ew')
        e5=Entry(iframe2,width=30)
        e5.grid(row=3,column=1,sticky='e')
    return 

def view():
    try:
        e2.delete('0',END)
        e3.delete('0',END)
        if cvar.get()=='Circle':
            r=float(e1.get())
            e2.insert('0',2*p*r)
            e3.insert('0',p*r*r)
            
        elif cvar.get()=='Square':
            s=float(e1.get())
            e2.insert('0',4*s)
            e3.insert('0',s*s)
            
        elif cvar.get()=='Rectangle':
            l=float(e1.get())
            b=float(e4.get())
            e2.insert('0',2*(l+b))
            e3.insert('0',l*b)
            
        elif cvar.get()=='Cube':
            e4.delete('0',END)
            e5.delete('0',END)
            s=float(e1.get())
            e2.insert('0',4*s*s)
            e3.insert('0',6*s*s)   
            e4.insert('0',s*s*s)
            e5.insert('0',12*s)
            
        elif cvar.get()=='Cuboid':
            e15.delete('0',END)
            e16.delete('0',END)
            l=float(e1.get())
            b=float(e6.get())
            h=float(e7.get())
            e2.insert('0',2*h*(l+b))
            e15.insert('0',2*(l*b+l*h+b*h))   
            e16.insert('0',l*b*h)
            e3.insert('0',4*(l+b+h))  
            
        elif cvar.get()=='Solid Cylinder':
            e4.delete('0',END)
            r=float(e1.get())
            h=float(e5.get())
            e2.insert('0',2*p*r*h)
            e3.insert('0',2*p*r*(r+h))   
            e4.insert('0',p*r*r*h)  
            
        elif cvar.get()=='Hollow Cylinder':
            e4.delete('0',END)
            R=float(e1.get())
            h=float(e5.get())
            r=float(e6.get())
            e2.insert('0',2*p*h*(R+r))
            e3.insert('0',2*p*(r+R)*(R-r+h))  
            e4.insert('0',p*h*(R*R-r*r))  
            
        elif cvar.get()=='Cone':
            e4.delete('0',END)
            r=float(e1.get())
            h=float(e5.get())
            l=float(e6.get())
            e2.insert('0',p*r*l)
            e3.insert('0',p*r*(l+2))  
            e4.insert('0',(1/3)*(p*r*r*h))  
            
        elif cvar.get()=='Solid Sphere':
            r=float(e1.get())
            e2.insert('0',4*p*r*r)
            e3.insert('0',(4/3)*p*r*r*r)
                 
        elif cvar.get()=='Hollow Sphere':
            R=float(e1.get())
            r=float(e4.get())
            e2.insert('0',4*p*(R**2-r**2))
            e3.insert('0',(4/3)*p*(R**3-r**3)) 
            
        elif cvar.get()=='Solid Hemisphere':
            e4.delete('0',END)
            r=float(e1.get())
            e2.insert('0',2*p*r*r)
            e3.insert('0',3*p*r*r)   
            e4.insert('0',(2/3)*p*r*r*r)
            
        elif cvar.get()=='Hollow Hemisphere':
            e4.delete('0',END)
            R=float(e1.get())
            r=float(e5.get())
            e2.insert('0',2*p*(r**2+R**2))
            e3.insert('0',2*p*(r**2+R**2)+p*(R**2-r**2))   
            e4.insert('0',(2/3)*p*(R**3-r**3))     
            
        elif cvar.get()=='Frustum':
            e4.delete('0',END)
            R=float(e1.get())
            r=float(e5.get())
            l=float(e6.get())
            h=float(e7.get())
            e2.insert('0',p*l*(R+r))
            e3.insert('0',p*l*(R+r)+p*(R**2+r**2))  
            e4.insert('0',(1/3)*p*h*(R**2+r**2+R*r))      
    except:
        messagebox.showinfo('showinfo','Please select a shape')
        return     

b1=Button(iframe1,text='Next',command=Next)
b1.grid(row=0,column=0,sticky='nsew')
b1.config(width='10')

b2=Button(iframe1,text='View',command=view)
b2.grid(row=1,column=0,sticky='nsew')
b1.config(width='10')
root.mainloop()