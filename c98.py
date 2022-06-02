def countWordsFromFile():
    f=input("Enter the file name")
    a=1
    file=open(f)
    for line in file:
        words=line.split()
        a=a+len(words)
        print("The number of words ",a," and ",line)    
countWordsFromFile()    