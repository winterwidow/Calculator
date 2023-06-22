import matplotlib.pyplot as plt
import numpy as np
from numpy import arange
from scipy.optimize import curve_fit
from tkinter import *
from tkinter import messagebox
import math as m
import sympy as smp
from sympy import sympify,solve
from sympy import symbols
from sympy.plotting import plot3d
#------------


window=Tk()
window.geometry('500x400+10+20')

#calculator

def ext():  
    quit()

def calc():
    root=Tk()
    root.title("scientific calculator")
   
    e=Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="black", bg="white")
    e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

    def click(to_print):
        old=e.get()
        e.delete(0,END)
        e.insert(0,old+to_print)
        return

    def clear(event):
        e.delete(0,END)
        return

    def sc(event):
        key=event.widget
        text=key['text']
        no=e.get()
        result=''
        if text=='deg':
            result=str(round(m.degrees(float(no)),5))
        if text=='sin':
            result=str(round(m.sin(float(no)),5))
        if text=='cos':
            result=str(round(m.cos(float(no)),5))
        if text=='tan':
            result=str(round(m.tan(float(no)),5))
        if text=='log':
            if '-' in no:
                messagebox.showinfo("Scientific calculator","Invalid input")
            else:
                result=str(round(m.log10(float(no)),5))
        if text=='ln':
            if '-' in no:
                messagebox.showinfo("Scientific calculator","Invalid input")
            else:
                result=str(round(m.log(float(no)),5))
        if text=='sqrt':
            if '-' in no:
                messagebox.showinfo("Scientific calculator","Invalid input")
            else:
                result=str(round(m.sqrt(float(no)),5))
        if text=='x!':
            if no.isdigit()==False:
                messagebox.showinfo("Scientific calculator","Invalid input")
            else:
                result=str(round(m.factorial(int(no)),5))
        if text=='1/x':
            result=str(round(1/(float(no)),5))
        if text=='x^2':
            result=str(round(m.pow(float(no),2),5))
        e.delete(0,END)
        e.insert(0,result)
       
    def out(event):
        quit()
       
    def evaluate(event):
        ans=e.get()
        ans=eval(ans)
        e.delete(0,END)
        e.insert(0,ans)

    log=Button(root,text="log",padx=28,pady=10)
    log.bind("<Button-1>",sc)
   
    ln=Button(root,text="ln",padx=28,pady=10)
    ln.bind("<Button-1>",sc)
   
    par1st=Button(root,text="(",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("("))
    par2nd=Button(root,text=")",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click(")"))

    dot=Button(root,text=".",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("."))
    exp=Button(root,text="^",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("**"))

    degb=Button(root,text="deg",padx=23,pady=10)
    degb.bind("<Button-1>",sc)

    sinb=Button(root,text="sin",padx=23,pady=10)
    sinb.bind("<Button-1>",sc)

    cosb=Button(root,text="cos",padx=23,pady=10)
    cosb.bind("<Button-1>",sc)

    tanb=Button(root,text="tan",padx=23,pady=10)
    tanb.bind("<Button-1>",sc)

    sqrtb=Button(root,text="sqrt",padx=23,pady=10)
    sqrtb.bind("<Button-1>",sc)

    ac=Button(root,text="C",padx=29,pady=10)
    ac.bind("<Button-1>",clear)

    sq=Button(root,text="x^2",padx=19,pady=10)
    sq.bind("<Button-1>",sc)

    mod=Button(root,text="mod",padx=19,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("%"))
    div=Button(root,text="/",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("/"))
    mult=Button(root,text="*",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("*"))
    minus=Button(root,text="-",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("-"))
    plus=Button(root,text="+",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("+"))
    frac=Button(root,text="1/x",padx=25,pady=10)
    frac.bind("<Button-1>",sc)

    pib=Button(root,text="pi",padx=19,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("3.141592653589793238"))
    eb=Button(root,text="e",padx=19,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("2.71828182845904523536"))

    equal=Button(root,text="=",padx=29,pady=10)
    equal.bind("<Button-1>",evaluate)

    fact=Button(root,text="x!",padx=23,pady=10)
    fact.bind("<Button-1>",sc)


    seven=Button(root,text="7",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("7"))
    eight=Button(root,text="8",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("8"))
    nine=Button(root,text="9",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("9"))
    four=Button(root,text="4",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("4"))
    five=Button(root,text="5",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("5"))
    six=Button(root,text="6",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("6"))
    one=Button(root,text="1",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("1"))
    two=Button(root,text="2",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("2"))
    three=Button(root,text="3",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("3"))
    zero=Button(root,text="0",padx=30,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("0"))


    log.grid(row=1,column=0)
    ln.grid(row=1,column=1)
    par1st.grid(row=1,column=2)
    par2nd.grid(row=1,column=3)

    dot.grid(row=1,column=4)
    exp.grid(row=2,column=0)
    degb.grid(row=2,column=1)

    sinb.grid(row=2,column=2)
    cosb.grid(row=2,column=3)
    tanb.grid(row=2,column=4)

    sqrtb.grid(row=3,column=0)
   
    equal.grid(row=7,column=3)
    ac.grid(row=3,column=1)
    sq.grid(row=3,column=2)
   
    mod.grid(row=3,column=3)
    div.grid(row=3,column=4)
    fact.grid(row=4,column=0)
    mult.grid(row=4,column=4)
    frac.grid(row=5,column=0)
    minus.grid(row=5,column=4)
    plus.grid(row=6,column=4)
   
    zero.grid(row=7,column=2)
    one.grid(row=6,column=1)
    two.grid(row=6,column=2)
    three.grid(row=6,column=3)
    four.grid(row=5,column=1)
    five.grid(row=5,column=2)
    six.grid(row=5,column=3)
    seven.grid(row=4,column=1)
    eight.grid(row=4,column=2)
    nine.grid(row=4,column=3)
   
    pib.grid(row=6,column=0)
    eb.grid(row=7,column=1)
   
    exit=Button(root,text="exit",padx=29,pady=10,relief=RAISED, bg="Black", fg="White")
    exit.bind("<Button-1>",out)

    exit.grid(row=8,column=2)
    
    ac=Button(root,text="C",padx=29,pady=10,relief=RAISED, bg="Black", fg="White")
    ac.bind("<Button-1>",clear)
    
    ac.grid(row=3,column=1)
    
    root.mainloop()
    
#-------------- END OF SCIENTIFIC CALC -------------------

#vectors

def vector():

    root1=Tk()
    root1.title("vector")
    root1.geometry("500x300")

    e=Entry(root1, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
    e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

    def mod1(event):
        flag=True
        key=event.widget
        text=key['text']
       
        ax1=ax.get().split('.')
        az1=az.get().split('.')
        ay1=ay.get().split('.')


        list=[ax1,az1,ay1]
        for a in list:
            for b in a:
                if b.isdigit()==False:
                    flag=False
                   

        if(flag==True):
            if text=='mod':
                result=m.sqrt(float(ax.get())**2+float(ay.get())**2+float(az.get())**2)
            e.delete(0,END)
            e.insert(0,result)  

        else:
            messagebox.showinfo("Vector algebra","Invalid input")

    def compute(event):
        key=event.widget
        text=key['text']
        flag=True

        ax1=ax.get().split('.')
        bx1=bx.get().split('.')
        ay1=ay.get().split('.')
        by1=by.get().split('.')
        az1=az.get().split('.')
        bz1=bz.get().split('.')

        list=[ax1,bx1,ay1,by1,az1,bz1]
        for a in list:
            for b in a:
                if b.isdigit()==False:
                    flag=False
                   

        if(flag==True):
           
       
            if text=='dot':
                result=float(ax.get())*float(bx.get())+float(ay.get())*float(by.get())+float(az.get())*float(bz.get())
            if text=='mod':
                result=m.sqrt(float(ax.get())**2+float(ay.get())**2+float(az.get())**2)
            if text=='cross':
                cpi=float(ay.get())*float(bz.get())-float(az.get())*float(by.get())
                cpj=float(ax.get())*float(bz.get())-float(az.get())*float(bx.get())
                cpk=float(ax.get())*float(by.get())-float(ay.get())*float(bx.get())
                result=str(cpi)+"i+"+str(cpj)+"j+"+str(cpk)+"k"
            if text=='add':
                i=float(ax.get())+float(bx.get())
                j=float(ay.get())+float(by.get())
                k=float(az.get())+float(bz.get())
                result=str(i)+"i+"+str(j)+"j+"+str(k)+"k"
            if text=='subtract':
                i=float(ax.get())-float(bx.get())
                j=float(ay.get())-float(by.get())
                k=float(az.get())-float(bz.get())
                result=str(i)+"i+"+str(j)+"j+"+str(k)+"k"
            if text=='angle':
                moda=m.sqrt(float(ax.get())**2+float(ay.get())**2+float(az.get())**2)
                modb=m.sqrt(float(bx.get())**2+float(by.get())**2+float(bz.get())**2)
                dp=float(ax.get())*float(bx.get())+float(ay.get())*float(by.get())+float(az.get())*float(bz.get())
                angle0=m.acos(dp/(moda*modb))
                result=round(angle0,3)
            e.delete(0,END)
            e.insert(0,result)

        else:
            messagebox.showinfo("Vector algebra","Invalid input")


    def out(event):
        quit()

    ax = StringVar(root1)
    ay = StringVar(root1)
    az = StringVar(root1)

    Label(root1, text="ax:").grid(row=1, column=0)
    Label(root1, text="ay:").grid(row=2, column=0)
    Label(root1, text="az:").grid(row=3, column=0)

    Entry(root1, textvariable=ax).grid(row=1, column=1)
    Entry(root1, textvariable=ay).grid(row=2, column=1)
    Entry(root1, textvariable=az).grid(row=3, column=1)

    bx = StringVar(root1)
    by = StringVar(root1)
    bz = StringVar(root1)

    Label(root1, text="bx:").grid(row=1, column=2)
    Label(root1, text="by:").grid(row=2, column=2)
    Label(root1, text="bz:").grid(row=3, column=2)
   
    Entry(root1, textvariable=bx).grid(row=1, column=3)
    Entry(root1, textvariable=by).grid(row=2, column=3)
    Entry(root1, textvariable=bz).grid(row=3, column=3)



    dot=Button(root1,text="dot",padx=28,pady=10)
    dot.bind("<Button-1>",compute)
    cross=Button(root1,text="cross",padx=28,pady=10)
    cross.bind("<Button-1>",compute)
    mod=Button(root1,text="mod",padx=28,pady=10)
    mod.bind("<Button-1>",mod1)
    add=Button(root1,text="add",padx=28,pady=10)
    add.bind("<Button-1>",compute)
    subtract=Button(root1,text="subtract",padx=28,pady=10)
    subtract.bind("<Button-1>",compute)
    angle=Button(root1,text="angle",padx=28,pady=10)
    angle.bind("<Button-1>",compute)
    exit=Button(root1,text="exit",padx=28,pady=10, relief=RAISED, bg="Black", fg="White")
    exit.bind("<Button-1>",out)


    dot.grid(row=4,column=0)
    cross.grid(row=4,column=1)
    mod.grid(row=4,column=2)
    add.grid(row=5,column=0)
    subtract.grid(row=5,column=1)
    angle.grid(row=5,column=2)
    exit.grid(row=6,column=1)

    root1.mainloop()
   
#---------- END OF VECTORS --------------

#graphs
  
def graph():
    root1=Tk()
    root1.title("Graphing calculator")
    x,y=smp.symbols('x y')
   
    def out(event):
        quit()
        
    def click(to_print):
        old=e.get()
        e.delete(0,END)
        e.insert(0,old+to_print)
        return

    def clear(event):
        e.delete(0,END)
        return

    def plottings(event):
        if function.get()!='':
            x=smp.symbols('x')
            user=function.get()
            L=list(user)
            c_open=c_close=0
            sin_0=['s','i','n']
            cos_0=['c','o','s']
            tan_0=['t','a','n']
            log_0=['l','o','g']
            flag=True
            for i in range(len(L)):
                if L[i] in 'qwertyuiopasdfghjklzcvbnm':
                    if (L[i:i+3]==sin_0 or L[i-1:i+2]==sin_0 or L[i-2:i+1]==sin_0
                        or L[i:i+3]==cos_0 or L[i-1:i+2]==cos_0 or L[i-2:i+1]==cos_0
                        or L[i:i+3]==tan_0 or L[i-1:i+2]==tan_0 or L[i-2:i+1]==tan_0
                        or L[i:i+3]==log_0 or L[i-1:i+2]==log_0 or L[i-2:i+1]==log_0):
                        pass
                    else:
                        flag=False
                        break
                elif L[i]=='(':
                    c_open+=1
                elif L[i]==')':
                    c_close+=1
            if c_open!=c_close:
                flag=False
           
            if flag==True:
                f=sympify(user)
                fig=plt.figure()

                axis = fig.add_subplot(1, 1, 1)
                axis.spines['top'].set_color('none')
                axis.spines['left'].set_position('zero')
                axis.spines['right'].set_color('none')
                axis.spines['bottom'].set_position('zero')
       
                f_f=smp.lambdify(x,f)
                x=np.arange(-5,4*np.pi,0.1)
                y=f_f(x)
                plt.plot(x,y)
                plt.show()
            else:
                messagebox.showinfo("Graphs","Invalid input")


        if function2.get()!='':
            x=smp.symbols('x')
            y=smp.symbols('y')
            user2=function2.get()
            L=list(user2)
            c_open=c_close=0
            sin_0=['s','i','n']
            cos_0=['c','o','s']
            tan_0=['t','a','n']
            log_0=['l','o','g']
            flag=True
            for i in range(len(L)):
                if L[i] in 'qwertuiopasdfghjklzcvbnm':
                    if (L[i:i+3]==sin_0 or L[i-1:i+2]==sin_0 or L[i-2:i+1]==sin_0
                        or L[i:i+3]==cos_0 or L[i-1:i+2]==cos_0 or L[i-2:i+1]==cos_0
                        or L[i:i+3]==tan_0 or L[i-1:i+2]==tan_0 or L[i-2:i+1]==tan_0
                        or L[i:i+3]==log_0 or L[i-1:i+2]==log_0 or L[i-2:i+1]==log_0):
                        pass
                    else:
                        flag=False
                        break
                elif L[i]=='(':
                    c_open+=1
                elif L[i]==')':
                    c_close+=1
            if c_open!=c_close:
                flag=False

            if flag==True:
                x, y = symbols('x y')
                f=sympify(user2)
                plot3d(f, (x, -5, 5), (y, -5, 5))
            else:
                messagebox.showinfo("Graphs","Invalid input")
        
    function = StringVar(root1)
    function2 = StringVar(root1)
   
    Label(root1, text="function (dependent variable x):").grid(row=1, column=1)
    Label(root1, text="function (dependent variables x and y):").grid(row=2, column=1)

    Entry(root1, textvariable=function).grid(row=1, column=2)
    Entry(root1, textvariable=function2).grid(row=2, column=2)

    ploting=Button(root1,text="plot",padx=29,pady=10)
    ploting.bind("<Button-1>",plottings)

    ploting.grid(row=3,column=3)
    
    exit=Button(root1,text="exit",padx=28,pady=10, relief=RAISED, bg="Black", fg="White")
    exit.bind("<Button-1>",out)
    exit.grid(row=4,column=2)

    root1.mainloop()

#----------- END OF graphs ---------------

#calculus

def calculus():
    root1=Tk()
    root1.title("calculus calculator")
    e=Entry(root1, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
    e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)


    x=smp.symbols('x')
    
    def out(event):
        quit()
        
    def click(to_print):
        old=e.get()
        e.delete(0,END)
        e.insert(0,old+to_print)
        return

    def clear(event):
        e.delete(0,END)
        return

    def integ(event):                                                           #integration
        x=smp.symbols('x')
        user=ent.get()
        L=list(user)
        c_open=c_close=0
        sin_0=['s','i','n']
        cos_0=['c','o','s']
        tan_0=['t','a','n']
        log_0=['l','o','g']
        flag=True
        for i in range(len(L)):
            if L[i] in 'qwertyuiopasdfghjklzcvbnm':
                if (L[i:i+3]==sin_0 or L[i-1:i+2]==sin_0 or L[i-2:i+1]==sin_0
                    or L[i:i+3]==cos_0 or L[i-1:i+2]==cos_0 or L[i-2:i+1]==cos_0
                    or L[i:i+3]==tan_0 or L[i-1:i+2]==tan_0 or L[i-2:i+1]==tan_0
                    or L[i:i+3]==log_0 or L[i-1:i+2]==log_0 or L[i-2:i+1]==log_0):
                    pass
                else:
                    flag=False
                    break
            elif L[i]=='(':
                c_open+=1
            elif L[i]==')':
                c_close+=1
        if c_open!=c_close:
            flag=False

        if flag==True:
            f=sympify(user)
            flag=True
       
            if up_lim.get()=='' and low_lim.get()=='':
                flag='empty'
            elif up_lim.get()=='' or low_lim.get()=='':
                flag=False
            else:
                up1=up_lim.get().split('.')
                low1=low_lim.get().split('.')

                list1=[up1,low1]
                for a in list1:
                    for b in a:
                        if b[0]=='-':
                            if b[1:].isdigit()==False:
                                flag=False
                        elif b.isdigit()==False:
                            flag=False
                        elif b=='inf' or b=='-inf':
                            flag=True
                   

            if flag=='empty':
                integral=smp.integrate(f,x).simplify()
                e.delete(0,END)
                e.insert(0,integral)
            elif flag==True:
                integral=str(round(smp.integrate(f,(x,float(low_lim.get()),float(up_lim.get()))).simplify(),5))
                if 'Accum' in integral:
                    messagebox.showinfo("Integration","Definite integral doesn't converge")
                elif 'Integral' in integral:
                    messagebox.showinfo("Integration","Integral cannot be computed")
                else:
                    e.delete(0,END)
                    e.insert(0,integral)
            else:
                messagebox.showinfo("Limiting values","Invalid input")
        else:
            messagebox.showinfo("Calculus","Invalid input")
   
    def differentiate(event):                                           #differentiation
        x=smp.symbols('x')
        user=ent.get()
        L=list(user)
        c_open=c_close=0
        sin_0=['s','i','n']
        cos_0=['c','o','s']
        tan_0=['t','a','n']
        log_0=['l','o','g']
        flag=True
        for i in range(len(L)):
            if L[i] in 'qwertyuiopasdfghjklzcvbnm':
                if (L[i:i+3]==sin_0 or L[i-1:i+2]==sin_0 or L[i-2:i+1]==sin_0
                    or L[i:i+3]==cos_0 or L[i-1:i+2]==cos_0 or L[i-2:i+1]==cos_0
                    or L[i:i+3]==tan_0 or L[i-1:i+2]==tan_0 or L[i-2:i+1]==tan_0
                    or L[i:i+3]==log_0 or L[i-1:i+2]==log_0 or L[i-2:i+1]==log_0):
                    pass
                else:
                    flag=False
                    break
            elif L[i]=='(':
                c_open+=1
            elif L[i]==')':
                c_close+=1
        if c_open!=c_close:
            flag=False

        if flag==True:
            f=sympify(user)
            dfdx=smp.diff(f,x)
            e.delete(0,END)
            e.insert(0,dfdx)
        else:
            messagebox.showinfo("calculus","Invalid input")

    def limit(event):                                               #limits
        x=smp.symbols('x')
        user=ent.get()
        L=list(user)
        c_open=c_close=0
        sin_0=['s','i','n']
        cos_0=['c','o','s']
        tan_0=['t','a','n']
        log_0=['l','o','g']
        flag=True
        for i in range(len(L)):
            if L[i] in 'qwertyuiopasdfghjklzcvbnm':
                if (L[i:i+3]==sin_0 or L[i-1:i+2]==sin_0 or L[i-2:i+1]==sin_0
                    or L[i:i+3]==cos_0 or L[i-1:i+2]==cos_0 or L[i-2:i+1]==cos_0
                    or L[i:i+3]==tan_0 or L[i-1:i+2]==tan_0 or L[i-2:i+1]==tan_0 
                    or L[i:i+3]==log_0 or L[i-1:i+2]==log_0 or L[i-2:i+1]==log_0):
                    pass
                else:
                    flag=False
                    break
            elif L[i]=='(':
                c_open+=1
            elif L[i]==')':
                c_close+=1
        if c_open!=c_close:
            flag=False

        if flag==True:
            user=ent.get()
            f=sympify(user)
            flag=True

            b=approach.get()
            if b=='':
                flag=False
            elif b.isdigit()==False:
                b0=b.split('.')
                print(b0)
                for a in b0:
                    if a[0]=='-':
                        if a[1:].isdigit()==False:
                            flag=False
                    elif b=='inf' or b=='-inf':
                        flag=True
                    elif a.isdigit()==True:
                        flag=True
                    else:
                        flag=False

            if flag==True:
                LHL=smp.limit(f,x,float(approach.get()),'-')
                RHL=smp.limit(f,x,float(approach.get()),'+')
                if LHL==RHL:
                    limiting=str(round(smp.limit(f,x,float(approach.get())),5))
                    if 'Accum' in limiting:
                        messagebox.showinfo("Limit","Limit does not converge")
                    elif 'imit' in limiting:
                        messagebox.showinfo("Limit","Cannot compute limit")
                    else:
                        e.delete(0,END)
                        e.insert(0,limiting)
                else:
                    messagebox.showinfo("LHL not equal to RHL","Limit does not exist")
            else:
                messagebox.showinfo("Approaching value of x","Invalid input")

        else:
            messagebox.showinfo("calculus","Invalid input")

    up_lim = StringVar(root1)
    drop_up=OptionMenu(root1, up_lim,"inf","-inf",m.pi,m.e)
    drop_up.grid(row=2, column=2)
    low_lim = StringVar(root1)
    drop_low=OptionMenu(root1, low_lim,"inf","-inf",m.pi,m.e)
    drop_low.grid(row=3, column=2)
    approach = StringVar(root1)
    drop_up=OptionMenu(root1, approach,"inf","-inf",m.pi,m.e)
    drop_up.grid(row=4, column=2)
    ent=StringVar(root1)    

    Label(root1, text="upper limit:").grid(row=2, column=0)
    Label(root1, text="lower limit:").grid(row=3, column=0)

    Entry(root1, textvariable=up_lim).grid(row=2, column=1)
    Entry(root1, textvariable=low_lim).grid(row=3, column=1)

    Label(root1, text="x approaches:").grid(row=4, column=0)
    Entry(root1, textvariable=approach).grid(row=4, column=1)

    Label(root1, text="Function:").grid(row=1, column=0)
    Entry(root1, textvariable=ent).grid(row=1, column=1)

    inte=Button(root1,text=chr(8747),padx=29,pady=10)
    inte.bind("<Button-1>",integ)
    diff=Button(root1,text="d/dx",padx=29,pady=10)
    diff.bind("<Button-1>",differentiate)
    lim=Button(root1,text="lim",padx=29,pady=10)
    lim.bind("<Button-1>",limit)
    eb=Button(root1,text="e",padx=29,pady=10,relief=RAISED,bg="Grey",fg="White",command=lambda:click("e"))
   
    inte.grid(row=8,column=3)
    diff.grid(row=8,column=4)
    lim.grid(row=9,column=4)

    ac=Button(root1,text="C",padx=29,pady=10,relief=RAISED,bg="Black",fg="White")
    ac.bind("<Button-1>",clear)
    
    exit=Button(root1,text="exit",padx=28,pady=10, relief=RAISED, bg="Black", fg="White")
    exit.bind("<Button-1>",out)
    
    ac.grid(row=8,column=0)
    exit.grid(row=9,column=0)
    
    root1.mainloop()
    
#----------- END OF CALCULUS ---------------

#Simplification of equations 
    
def simp():
    root=Tk()
    root.title("scientific calculator")
   
    e=Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="black", bg="white")
    e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

    x=smp.symbols('x')
    def out(event):
        quit()

    def clear(event):
        e.delete(0,END)
        return

    def simp(event):
        user=e.get()
        f=sympify(user)

        f_f=smp.simplify(f)
        e.delete(0,END)
        e.insert(0,f_f)

    def exp(event):
        user=e.get()
        f=sympify(user)

        f_f=smp.expand(f)
        e.delete(0,END)
        e.insert(0,f_f)

    def factor(event):
        user=e.get()
        f=sympify(user)

        f_f=smp.factor(f)
        e.delete(0,END)
        e.insert(0,f_f)

    def rooting(event):
        user=e.get()
        f=sympify(user)

        f_f=smp.solve(f,x)
        e.delete(0,END)
        e.insert(0,f_f)

    def evaluate(event):
        user=e.get()
        f=sympify(user)
        s=f.subs([(x,n)]).evalf()
        e.delete(0,END)
        e.insert(0,s)

    evaluate=Button(root,text="simplify",padx=29,pady=10)                   #simplifying
    evaluate.bind("<Button-1>",simp)
    evaluate.grid(row=1,column=0)

    expand=Button(root,text="expand",padx=29,pady=10)                       #expanding
    expand.bind("<Button-1>",exp)
    expand.grid(row=1,column=1)

    factorise=Button(root,text="Factorise",padx=29,pady=10)                 #factorising
    factorise.bind("<Button-1>",factor)
    factorise.grid(row=2,column=0)

    roots=Button(root,text="roots",padx=29,pady=10)                         #roots
    roots.bind("<Button-1>",rooting)
    roots.grid(row=2,column=1)
   
    ac=Button(root,text="C",padx=29,pady=10,relief=RAISED,bg="Black",fg="White")
    ac.bind("<Button-1>",clear)
   
    exit=Button(root,text="exit",padx=28,pady=10, relief=RAISED, bg="Black", fg="White")
    exit.bind("<Button-1>",out)
    exit.grid(row=3,column=1)
    ac.grid(row=3,column=0)
    root.mainloop()


#----------- END OF simplification ---------------

# Data & histogram
def data():
    root=Tk()
    root.title("Data")

    def ext():  
        quit()

    def plots():
        root1=Tk()
        root1.title("Plot")
   

        e=Entry(root1, width=50, borderwidth=5, relief=RIDGE, fg="black", bg="white")
        e.grid(row=0,column=0,columnspan=5,padx=10,pady=15)

        def plotting(event):
            x_values=xvalues.get().split(',')
            y_values=yvalues.get().split(',')
            x=[]
            y=[]    
            flag=True
            for i in x_values:
                el0=''
                for j in i:
                    if j in '1234567890. -+':
                        el0+=j
                        flag1=True
                    else:
                        flag1=False
                        break
                if flag1==True:    
                    el=float(el0)
                    x+=[el]
                else:
                    flag=False
            for i in y_values:
                el0=''
                for j in i:
                    if j in '1234567890. -+':
                        el0+=j
                        flag1=True
                    else:
                        flag1=False
                        break
                if flag1==True:    
                    el=float(el0)
                    y+=[el]
                else:
                    flag=False
            if flag==True:
                plt.figure(figsize=(8,3))
                plt.plot(x,y,'o--')
                plt.show()
            else:
                messagebox.showinfo("Data","Invalid input")

        def best_fit(event):
            text=types.get()
            x_values=xvalues.get().split(',')
            y_values=yvalues.get().split(',')
            x=[]
            y=[]
            flag=True
            for i in x_values:
                el0=''
                for j in i:
                    if j in '1234567890. -+':
                        el0+=j
                        flag1=True
                    else:
                        flag1=False
                        break
                if flag1==True:    
                    el=float(el0)
                    x+=[el]
                else:
                    flag=False
            for i in y_values:
                el0=''
                for j in i:
                    if j in '1234567890. -+':
                        el0+=j
                        flag1=True
                    else:
                        flag1=False
                        break
                if flag1==True:    
                    el=float(el0)
                    y+=[el]
                else:
                    flag=False
       
            if flag==True:

                if text=='linear':
                    def objective(x, a, b):
                        return a * x + b
                    popt, _ = curve_fit(objective, x, y)
                    a, b = popt
                    k='y = %.5f * x + %.5f' % (a, b)
                    e.delete(0,END)
                    e.insert(0,k)
                    x_line = arange(min(x), max(x), 1)
                    y_line = objective(x_line, a, b)
                    plt.plot(x, y,'o--',lw=0.2)
                    plt.plot(x_line, y_line, '--', color='red')
                    plt.show()
   
                if text=='quadratic':
                    def objective(x, a, b,c):
                        return a * x **2 + b*x+c
                    popt, _ = curve_fit(objective, x, y)
                    a, b,c = popt
                    k='y = %.5f * x + %.5f * x^2 +%.5f' % (a, b,c)
                    e.delete(0,END)
                    e.insert(0,k)
                    x_line = arange(min(x), max(x), 1)
                    y_line = objective(x_line, a, b,c)
                    plt.plot(x, y,'o--',lw=0.2)
                    plt.plot(x_line, y_line, '--', color='red')
                    plt.show()
   
                if text=='cubic':
                    def objective(x, a, b, c, d):
                        return a*x**3+b*x**2+c*x+d
                    popt, _ = curve_fit(objective, x, y)
                    a, b,c,d = popt
                    k='y = %.5f * x + %.5f * x^2 +%.5f *x^3 + %.5f' % (a, b, c, d)
                    e.delete(0,END)
                    e.insert(0,k)
                    x_line = arange(min(x), max(x), 1)
                    y_line = objective(x_line, a, b,c ,d)
                    plt.plot(x, y,'o--',lw=0.2)
                    plt.plot(x_line, y_line, '--', color='red')
                    plt.show()
       
                if text=='sin':
                    def objective(x, a, b,c):
                        return a*np.sin(b*x-c)
                    popt, _ = curve_fit(objective, x, y)
                    a, b ,c= popt
                    k='y = %.5f * sin(%.5f * x) + %.5f' % (a, b,c)
                    e.delete(0,END)
                    e.insert(0,k)
                    x_line = arange(min(x), max(x), 1)
                    y_line = objective(x_line, a, b,c)
                    plt.plot(x, y,'o--',lw=0.2)
                    plt.plot(x_line, y_line, '--', color='red')
                    plt.show()
   
                if text=='exponential':
                    def objective(x, a, b):
                        return a*np.e**(x*b)
                    popt, _ = curve_fit(objective, x, y)
                    a, b = popt
                    k='y = %.5f * e^(x + %.5f)' % (a, b)
                    e.delete(0,END)
                    e.insert(0,k)
                    x_line = arange(min(x), max(x), 1)
                    y_line = objective(x_line, a, b)
                    plt.plot(x, y,'o--',lw=0.2)
                    plt.plot(x_line, y_line, '--', color='red')
                    plt.show()
            else:
                messagebox.showinfo("Data","Invalid input")     


#----------------------------------        

        xvalues = StringVar(root1)
        yvalues= StringVar(root1)
        types=StringVar(root1)
        drop_down=OptionMenu(root1, types,"linear","quadratic","cubic","sin","exponential")
        drop_down.grid(row=4, column=2)
   
        Label(root1, text="Enter independent values:").grid(row=2, column=0)
        Label(root1, text="Enter dependent values:").grid(row=3, column=0)
        Label(root1, text="Select function type:").grid(row=4, column=0)
   
        Entry(root1, textvariable=xvalues).grid(row=2, column=1)
        Entry(root1, textvariable=yvalues).grid(row=3, column=1)
        Entry(root1, textvariable=types).grid(row=4, column=1)
 
        plot=Button(root1,text='plot',padx=29,pady=10)
        plot.bind("<Button-1>",plotting)
        best=Button(root1,text='Best fit curve',padx=29,pady=10)
        best.bind("<Button-1>",best_fit)
       
        plot.grid(row=8,column=3)
        best.grid(row=8,column=4)
   
        root1.mainloop()
   
    def histo():
        root1=Tk()
        root1.title("Histogram")
   
        def histogram(event):
            x_values=xvalues.get().split(',')
            x=[]
            flag=True
            for i in x_values:
                el0=''
                for j in i:
                    if j in '1234567890. -+':
                        el0+=j
                        flag1=True
                    else:
                        flag1=False
                        break
                if flag1==True:    
                    el=float(el0)
                    x+=[el]
                else:
                    flag=False

                if bins.get().isdigit()==False:
                    flag=False
            if flag==True:
                n=int(bins.get())
                plt.figure(figsize=(8,3))
                plt.hist(x,bins=n, histtype='step')
                plt.show()
            else:
                messagebox.showinfo("Histogram","Invalid input")    


        xvalues = StringVar(root1)
        bins = StringVar(root1)

        Label(root1,text="Enter data seperated by commas ( , )").grid(row=2,column=0)

        Label(root1, text="Enter data:").grid(row=4, column=0)
        Label(root1, text="No. of bins:").grid(row=5, column=0)
   
        Entry(root1, textvariable=xvalues).grid(row=4, column=1)
        Entry(root1, textvariable=bins).grid(row=5, column=1)
   
        his=Button(root1,text='Histogram',padx=29,pady=10)
        his.bind("<Button-1>",histogram)
   
        his.grid(row=8,column=4)
   
        root1.mainloop()
   
    plotts=Button(root, text="Plot", bd=7, bg='pink',fg='blue')
    histog=Button(root, text="Histogram ", bd=7, bg='pink',fg='blue')
    A7=Button(root, text="Exit", bd=7, bg="pink", fg="blue")

    plotts.pack()
    histog.pack()
    A7.pack()

    plotts.configure(command=plots)
    histog.configure(command=histo)
    A7.configure(command=ext)

    root.mainloop()

#----------- END OF DATA --------------------

#BUTTONS
    
Calc=Button(window, text="Scientific calculator", bd=7, bg='black',fg='cyan')
Vector=Button(window, text="Vector Algebra ", bd=7,bg='black',fg='cyan')
Graph=Button(window, text="Graph Functions ", bd=7, bg='black',fg='cyan')
Calculus=Button(window, text="Calculus ", bd=7, bg='black',fg='cyan')
Simplify=Button(window, text="Simplify", bd=7,bg='black',fg='cyan')
Data=Button(window, text="Data manipulation",bg='black',fg='cyan')
A7=Button(window, text="Exit", bd=7,bg='black',fg='cyan')


Calc.pack()
Vector.pack()
Graph.pack()
Calculus.pack()
Simplify.pack()
Data.pack()
A7.pack()

   
Calc.configure(command=calc)
Vector.configure(command=vector)
Graph.configure(command=graph)
Calculus.configure(command=calculus)
Simplify.configure(command=simp)
Data.configure(command=data)
A7.configure(command=ext)

window.mainloop()

#------ END ------
