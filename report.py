def main():
    print("REPORT\n")
    import pickle
    import billing
    global blrec, ctrec
    fl=open("billing.txt", 'rb')
    fil=open("customer.txt", 'rb')
    print("%-8s %-13s %-18s %-20s %-15s %15s" %("Bill No", "Bill Date", "Customer Name", "Customer Address", "Contact Number", "Total Amount"))
    print()
    grndtot=0
    while True:
        totamt=0
        amt=0
        try:
            rec1=pickle.load(fl)
            rec2=pickle.load(fil)
            for c in range(0, len(rec1["Items"]), 5):
                amt=rec1["Items"][c+3]* rec1["Items"][c+4]
                totamt+=amt
            grndtot+=totamt
            print('%-8s %-13s %-18s %-20s %-15s %13.2f' %(rec1["Bno"], rec1["Bdate"], rec2["Cnm"], rec2["Cad"], rec2["Cno"], totamt))
            print()
        except EOFError:
            break
    print("="*96)
    print('%-78s %13.2f' %("Grand Total:", grndtot))
    print("="*96)
    fl.close()
    fil.close()


if __name__ == '__main__':
    main()
       
