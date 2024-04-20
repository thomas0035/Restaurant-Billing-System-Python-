from filcommon import *
from items import *
import pickle

bllst = ["Bill no.   ",
         "Bill Date  "]

lstit=  ["Item Number",
         "Item Name  ",
         "Measure    ",
         "Price      ",
         "Qty Ordered"]

itlist=[]

ctlst = ['Customer Name   ',
         'Customer Address',
         'Contact Number  ']

blrec={"Bno"  : 1,
       "Bdate": '',
       "Items": []}

ctrec={'Bno': 1,
       'Cnm': '',
       'Cad': '',
       'Cno': ''}

def nxtbillno():
    ln=0
    if os.path.exists("billing.txt"):
        fl=open("billing.txt", "rb")
        while True:       
            try:
                rec=pickle.load(fl)
                ln+=1
            except:
                break
        fl.close()
    return ln+1

def billing():
    global blrec, ctrec, itlist
    blrec["Bno"] = nxtbillno()
    print('BILLING\n')
    print('Bill Number:', blrec["Bno"])    
    blrec['Bdate'] = input(bllst[1]+': ')
    print()
    ctrec['Bno']=blrec["Bno"]
    ctrec['Cnm'] = input(ctlst[0]+': ')
    ctrec['Cad'] = input(ctlst[1]+': ')
    ctrec['Cno'] = input(ctlst[2]+': ')
    print()
    while True:
        itn = 0
        itn = acceptint("Item Number: ", itn)
        itrec = it_search(itn)
        if itrec:
            it_printrec(itrec)
            qt=0
            qt = acceptint("Qty Ordered: ", qt)
            itlist.append(itrec['Itno'])
            itlist.append(itrec['Itnm'])
            itlist.append(itrec['Measure'])
            itlist.append(itrec['Price'])
            itlist.append(qt)
           
            
        else:
            print('Invalid Item Number...')
        print()
        ch = input('More Items ?(Y/N): ')
        print()
        if ch not in 'yY':
            break
        print()
    blrec["Items"]=itlist
    view_bill()
    
    opt=input("SAVE BILL(Y/N): ")
    if opt in 'Yy':
        fl=open("billing.txt", "ab")
        pickle.dump(blrec, fl)
        fl.close()
        fil=open("customer.txt", "ab")
        pickle.dump(ctrec, fil)
        fil.close()
        print("Bill Stored!")
    else:
        print("Bill Cancelled!")
    blrec={}
    ctrec={}
        
def view_bill():
    global blrec, ctrec, itlist
    print('SALES BILL\n')
    print("Bill Number:", blrec["Bno"])
    print("Bill Date  :", blrec["Bdate"])
    print()
    print("Customer Name   :", ctrec["Cnm"])
    print("Customer Address:", ctrec["Cad"])
    print("Contact Number  :", ctrec["Cno"])
    print() 
    print('%-8s %-15s %-25s %-15s %-13s %-13s %-13s' % ('Sl.No.', 'Item Number', 'Item Name', 'Measure',
                                            'Price', 'Qty Ordered', 'Amount'))
    sl = 1
    amt = 0
    totamt = 0
    for c in range(0, len(blrec["Items"]), 5):
        amt=blrec["Items"][c+3]* blrec["Items"][c+4]  
        print('%-8d %-15s %-25s %-15s %-13.2f %-13.2f %-13.2f' % 
              (sl, blrec["Items"][c],
               blrec["Items"][c+1],
               blrec["Items"][c+2],
               blrec["Items"][c+3],
               blrec["Items"][c+4],
               amt))
        sl += 1
        totamt += amt
    print("="*110)
    print("%-87s %13.2f" %("Total Amount: ", totamt))
    print()
    print("="*110)
    main()

def search_bill():
    global blrec, ctrec, itlist
    bn=0
    bn=acceptint("Enter Bill Number: ", bn)
    fl=open("billing.txt", "rb")
    flag=0
    while True:
        try:
            rec=pickle.load(fl)
            if rec["Bno"]==bn:
                blrec=rec
                itlist=blrec["Items"]
                flag=1
                break
        except:
            break
    fl.close()
    if flag==1:
        fl=open("customer.txt", "rb")
        while True:
            try:
                rec=pickle.load(fl)
                if rec["Bno"]==bn:
                    ctrec=rec
                    break
            except:
                break
        fl.close()
        view_bill()
    else:
        print("Invalid Bill Number!")
        
        
def main():
    print("MAIN MENU\n")
    print('''1.Enter New Bill
2.Search Bill
3.Exit Billing System\n''')
    opt=int(input("Enter your Choice(1-3): "))
    print()
    if opt==1:
        billing()
    elif opt==2:
        search_bill()
    elif opt==3:
        return
    else:
        print("Invalid Choice!")
        
if __name__ == '__main__':
    main()
       

