#below function are arthematic operation is done.
def additio(n1,n2):
    print("output is :",n1+n2)
    return n1+n2
def subtra(n1,n2):
    print("output is :",n1-n2)
    return n1-n2
def divis(n1,n2):
    try:#This is used if any number is trying to divide by zero then exception raise so we use try block.
        print("output is :",n1/n2)
        return n1/n2
    except:#It will catch the exception.
        print("any number with zero cannot divisble")    
        return 0

def multp(n1,n2):
    print("output is :",n1*n2)
    return n1*n2

# taking the input from user .
n1=int(input("enter the number :"))# entering the number 1.
a=input("enter the operator :")# arthmetic operator is entered.
n2=int(input("enter the number :"))# entering the number 2.

#infinite loop is run.
while True:
    print('''
          option 
          1.For exit enter (E or e).
          2.For clear data enter (C or c).
          ''')
    #below thing is used for calling the function for doing operation. 
    if(a=='+'):
        data=additio(n1,n2)
    elif(a=='-'):
        data=subtra(n1,n2)
    elif(a=='/'):
        data=divis(n1,n2)            
    elif(a=='*'):
        data=multp(n1,n2) 
    
    if data!=0:#check of there is data is 0 or not. 
        #After first operation is done.          
        a=input("enter the option or operator :")
        if a=='E' or a=='e': # To exit the calculatr.
            break
        elif(a=='c' or a=='C'):# To clear the data.
            n1=int(input("enter the number :"))
            a=input("enter the operator :")
            n2=int(input("enter the number :"))
            data=0
        else:
            n1=data
            n2=int(input("enter the number :"))
    #if data is zero then it will ask again 2 number for doing operation.        
    else: 
        n1=int(input("enter the number :"))
        a=input("enter the operator :")
        n2=int(input("enter the number :"))
    
