def calcucator():
    print("**********\nCALCULATOR")

    number_1=input("Input number 1: ")
    if mycheck(number_1)==1:
        return 1

    operate=input()

    number_2=input("Input number 2: ")
    if mycheck(number_2)==1:
        return 1

    if myswitch(float(number_1),float(number_2),operate)==1:
        return 1
    

def mycheck(val):
    if isfloat(val):
        pass
    else:
        print("Incorrect number!")
        return 1


def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def myswitch(number_1, number_2, operate):
    if(operate=='+'):
        print("Answer: ")
        print(mysum(number_1,number_2))
    elif(operate=='-'):
        print("Answer: ")
        print(mydif(number_1,number_2))
    elif(operate=='*'):
        print("Answer: ")
        print(mymul(number_1,number_2))
    elif(operate=='/'):
        print("Answer: ")
        print(mydiv(number_1,number_2))
    else:
        print("Incorrect operation!")
        return 1


def mysum(number_1,number_2):
    return number_1+number_2
def mydif(number_1,number_2):
    return number_1-number_2
def mymul(number_1,number_2):
    return number_1*number_2
def mydiv(number_1,number_2):
    if(number_2!=0):
        return number_1/number_2

i=1
while(i!=0):
    j=0 # for (Y/N)
    calcucator()
    while (j<3):
        answer = input("Restart CALCULATOR? (Y/N): ")
        if ( answer!='Y' and answer!='N' and answer!='y' and answer!='n' ):
            j+=1
            print("Incorrect answer! ", j, "/ 3")
            if j>=3: 
                print("Closing CALCUCATOR...")
                i=0
            continue
        elif (answer=='Y' or answer=='y'):
            print("Restart CALCUCATOR...")
            break
        elif (answer=='N' or answer=='n'):
            print("Closing CALCUCATOR...")
            i=0
            break
        else:
            print("Attempts are over")
            i=0
            break