def helpfil():
    fil = open('helpfil.txt', 'r')
    st = fil.read()
    print(st)
    fil.close()
    
def main():
    helpfil()
    
if __name__ == '__main__':
    main()
    
