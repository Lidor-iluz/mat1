def pownum (x:float,i):
    if i==0:
        return 1
    else:
         calc=x
         for num in range(1,i):
             calc = calc*x
    return calc



def atseret (i):
    if i<1:
        return 1
    else:
        calc=i
        for num in range(1,i):
            calc = calc*num
        return calc
    
    
        
def exponent (x:float):
     calc=1
     for i in  range(1,100):
         calc=calc+(pownum(x,i)) /atseret( i)
     return calc


def absFun(x:float):
    if x>0 :
        return x
    else:
        return x*-1
    
def even (x:float):
    if x%2!=0:
        return True
    else:
        return False
    
 
    
def Ln(x:float):
    if x<=0:
        return 0 
    calc=x-1
    z=0
    while absFun(z-calc)>0.001:
        z=calc
        calc=calc+2*((x-exponent(calc))/ (x+exponent(calc)))
    return calc


def XtimesY (x:float,y:float):
    if x<0:
        return 0.0
    if y==0:
        return 1.0
    elif y==1:
        return float(x)
    else:
        solution=exponent(y*Ln(x))
        return solution


def sqrt (x:float,y:float):
    if y==0:
        return 0.0
    if y<0 and even(x):
        calc=XtimesY(-y, 1/x)
        return -1*calc
    calc=XtimesY(y, 1/x)
    return calc



def calculate(x:float):
    calc=exponent(x)*XtimesY(x,-1)*XtimesY(7,x)*sqrt(x,x)
    return float('%0.6f' % calc)