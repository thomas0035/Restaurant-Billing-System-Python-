##def main():
##    
##    fl=open("customer.txt", "rb")
##    import pickle
##    print("CUSTOMER DETAILS\n")
##    custnm=input("Enter Customer Name: ")
##    while True:
##        try:
##            rec=pickle.load(fl)
##            if rec["Cnm"]==custnm:
##                print("Bill Number   : ", rec["Bno"])
##                print("Address       : ", rec["Cad"])
##                print("Contact Number: ", rec["Cno"])
##            else:
##                print("No Such Name!")
##                break
##        except EOFError:
##            break
##    fl.close()
##
##if __name__ == '__main__':

    

from filcommon import *
def main():
    import pickle
    fl=open("customer.txt", 'rb')
    print("%-18s %-20s %-15s" %("Customer Name", "Customer Address", "Contact Number"))
    print()
    while True:
        try:
            rec2=pickle.load(fl)
            print('%-18s %-20s %-15s' %(rec2["Cnm"], rec2["Cad"], rec2["Cno"]))
            print()
        except EOFError:
            break
    
    fl.close()
    if __name__ == '__main__':
        main()




