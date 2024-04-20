from filcommon import *

rec = {'Itno': 1,
       'Itnm': '',
       'Price': 0.0,
       'Measure': ''}

lst = ['Item Number', 
       'Item Name  ',
       'Price      ',
       'Measure    ']

def it_search(itn):
    if not os.path.exists('items.txt') :
        return False
    with open("items.txt", "rb") as fl:
        flag=False
        while True:
            try:
                rec = pickle.load(fl)
                if rec['Itno'] == itn:
                    flag=rec
                    break
            except EOFError:
                break
    return flag

def it_printrec(rec):
    c = 0
    for key, value in rec.items():
        if key == 'Itno':
            c += 1
            continue
        print(lst[c]+': ', value)
        c += 1
    print()

def it_inputrec(rec, itn):
    c = 0
    for key, value in rec.items():
        if key == 'Itno':
            c += 1
            rec['Itno'] = itn
            continue
        rec[key] = myinp(lst[c], rec[key])
        c += 1
    return rec

def it_append():
    print('ADDING NEW ITEM\n')
    print('Enter Item Details...')
    itn=0
    itn=acceptint('Item Number: ', itn)
    rc=it_search(itn)
    if rc==False:  
        global rec
        rec = it_inputrec(rec, itn)
        print()
        ch = input('Save Details?(Y/N): ')
        if ch in 'yY':
            with open('Items.txt', 'ab') as fl:
                pickle.dump(rec, fl)
            print('Details Saved !')
        else:
            print('Saving Cancelled !')
    else:
        print("\nItem Details Already Entered...\n")
        it_printrec(rc)

def it_listing():
    print('MENU\n')
    fl = open('Items.txt', 'rb')
    flag = True
    print('%-8s %-15s %-25s %13s     %-15s' % ('Sl.No.', 'Item Number', 'Item Name', 'Price', 'Measure'))
    sl = 1
    while True:
        try:
            rec = pickle.load(fl)
            print('%-8d %-15s %-25s %13.2f     %-15s' %
                  (sl, rec['Itno'],
                       rec['Itnm'],
                       rec['Price'],
                       rec['Measure']))
            sl += 1
        except EOFError:
            break
    fl.close()


def it_update():
    print('EDITING BY ITEM NUMBER\n')
    itn = int(input('Item number to be updated: '))
    rec = it_search(itn)
    if rec != False:
        print('Current Details...')
        it_printrec(rec)
        opt = input('Modify (Y/N): ')
        if opt in 'yY':
            fl = open('Items.txt', 'rb')
            reclst = []
            while True:
                try:
                    rec = pickle.load(fl)
                    reclst.append(rec)
                except EOFError:
                    break
            fl.close()
            print()
            rc = it_inputrec(rec, itn)
            for c in range(len(reclst)):
                if reclst[c]['Itno'] == itn:
                    reclst[c] = rc
            fl = open('Items.txt', 'wb')
            for rec in reclst:
                pickle.dump(rec, fl)
            fl.close()
            print('Updated Successfully !')
        else:
            print('Modification Cancelled !')
    else:
        print('Invalid Item Number !')

def it_view():
    print('VIEWING BY ITEM NUMBER\n')
    itn = int(input('Item number to be viewed: '))
    rec = it_search(itn)
    if rec != False:
        it_printrec(rec)
    else:    
        print('Given Item number NOT found !!!')
    


def it_delete():
    print('DELETING BY ITEMCODE\n')
    itno = int(input('Itemnumber to be deleted: '))
    fl1 = open('Items.txt', 'rb')
    fl2 = open('Itemstemp.txt', 'wb')
    while True:
        try:
            rec = pickle.load(fl1)
            if rec['Itno'] != itno:
                pickle.dump(rec, fl2)
        except EOFError:
            break
        
    fl1.close()
    fl2.close()
    os.remove('Items.txt')
    os.rename('Itemstemp.txt', 'Items.txt')
    it_listing()
    print('\n')


def main():
    while True:
        mnlst = ['1. Add New Item', '2. Menu', '3. By Item number(View/Edit/Delete)', '4. Exit Items Menu']
        submnu = ['1. View', '2. Edit', '3. Delete', '4. Return to Items Menu']
        print('MAIN MENU - ITEMS \n')
        for a in range(len(mnlst)):
            print(mnlst[a], end = '\n')
        print()
        ch = 0
        ch = acceptint('Enter Choice (1 - 4): ', ch)
        print()
        if not os.path.exists('items.txt') :
            print('No Details Entered Yet...\n')
            if ch == 2 or ch == 3:
                continue
        if ch == 1:
            it_append()
        elif ch == 2:
            it_listing()
        elif ch == 3:
            while True:
                print('SUBMENU - BY ITEM NUMBER...')
                for b in range(len(submnu)):
                    print('\t'+submnu[b], end = '\n')
                cho = 0
                cho = acceptint('Enter Choice (1-4): ', cho)
                print()
                if cho == 1:
                    it_view()
                elif cho == 2:
                    it_update()
                elif cho == 3:
                    it_delete()
                elif cho == 4:
                    break
                else:
                    print('Invalid Choice Entered !!!')
                print('\n')
        elif ch == 4:
            break
        else:
            print('Invalid Choice Entered !!!')
        print('\n')
                    
if __name__== '__main__':
    main()
