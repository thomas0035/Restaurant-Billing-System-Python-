from filcommon import *
import helpfil
import items
import customer
import billing
import items
import report
import os

while True:
    os.system(clear)
    print("HOTEL BILLING SYSTEM\n")
    print('''
MAIN MENU\n
1. Items
2. Billing
3. Customer Details
4. Report
5. Help
6. Exit Program
    ''')
    ch = int(input("Enter Choice(1-6): "))
    if ch == 1:
        items.main()
    elif ch == 2:
        billing.main()
    elif ch == 3:
        customer.main()
    elif ch==4:
        report.main()
    elif ch == 5:
        helpfil.main()
        os.system(pause)
    elif ch == 6:
        break
    else:
        print("Invalid Choice")
    
        
