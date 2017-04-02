#jacky(sicong) Liu
#number of hours:14 hours
#some additonal require not done, but still a good practice for final exams
#student ID:301269558
#sla255@sfu.ca
def the_board():
    nrows=len(mat)
    ncols=len(mat[0])

    for c in range(ncols):
        print "\t","Col",c,
    print
    for r in range(nrows):
        print "row",r,"\t",
        for c in range(ncols):
            print mat[r][c], "\t",
        print
   
def row():
    colect=0
    print"Number row (0 to",len(mat)-1,")"
    r=input(":")
    print
    print "positions visited:...",
    print
    for c in range(len(mat[r])):
        print "[",r,"]",
        print "[",c,"]"
        if mat[r][c]%2==0:
                   colect=colect+mat[r][c]/2
                   mat[r][c]=(mat[r][c])/2
        elif mat[r][c]%2==1:
                   colect=colect+mat[r][c]
                   mat[r][c]=0
    print"points obtained in this trip:...",colect
    return colect

def col():
    colect=0
    print"Number column (0 to",len(mat[0])-1,")"
    c=input(":")
    if c>=0 and c<=len(mat[0])-1:
        print"positions visited:...",
        print
        for r in range(len(mat[c])):
            print "[",r,"]",
            print"[",c,"]"
            if mat[r][c]%2==0:
                   colect=colect+mat[r][c]/2
                   mat[r][c]=(mat[r][c])/2
            elif mat[r][c]%2==1:
                   colect=colect+mat[r][c]
                   mat[r][c]=0
        print"points obtained in this trip:...",colect
    elif c<0 or c>len(mat[0])-1:
        print "That is not a alid input, please re-enter"
        print"Number column (0 to",len(mat),")"
        c=input(":")
    else:
        print "The valus should only have digits, please re-enter"
        print"Number column (0 to",len(mat),")"
        c=input(":")
    return colect
                                   
def m_diagonal():
    colect=0
    print "positions visited:...",
    print
    for c in range(len(mat[0])):
            print "[",c,"]",
            print "[",c,"]"
            if mat[c][c]%2==0:
                   colect=colect+mat[c][c]/2
                   mat[c][c]=(mat[c][c])/2
            elif mat[c][c]%2==1:
                   colect=colect+mat[c][c]
                   mat[c][c]=0
    print"points obtained in this trip:...",colect
    return colect
def s_diagonal():
    colect=0
    print "positions visited:...",
    print
    for c in range(len(mat[0])):
            print "[",c,"]",
            print "[",len(mat[0])-c-1,"]"
            if mat[c][len(mat[0])-c-1]%2==0:
                   colect=colect+mat[c][len(mat[0])-c-1]/2
                   mat[c][len(mat[0])-c-1]=(mat[c][len(mat[0])-c-1])/2
            elif mat[c][len(mat[0])-c-1]%2==1:
                   colect=colect+mat[c][len(mat[0])-c-1]
                   mat[c][len(mat[0])-c-1]=0
    print"points obtained in this trip:...",colect
    return colect
def random_cells():
    colect=0
    cells=input("How many random cells sall the hunter visit?")
    print "positions visited:...",
    print         
    for c in range(cells):
                a=r.randint(0,len(mat)-1)
                b=r.randint(0,len(mat)-1)
                print"[",a,"]",
                print"[",b,"]"
                if mat[a][b]%2==0:
                   colect=colect+mat[a][b]/2
                   mat[a][b]=(mat[a][b])/2
                elif mat[a][b]%2==1:
                   colect=colect+mat[a][b]
                   mat[a][b]=0
    print"points obtained in this trip:...",colect
    return colect
def result():
    print"The treasure hunter",name,"obtained",point,"points in its game"
    print"The values of each row in the board(as binary number) are:",luck_each(),
    print
    print "and therefore the board luncky number is:",luck_number(),
    return

def final_result():
    print "Totla hunters that played:",count,
    print
    print "Total points of all hunters:",totalpoint,
def luck_each():
    total=0
    res=""
    for i in range(len(mat)):
        for d in range(len(mat)):
            if mat[i][d]%2==0:
                mat[i][d]=0
            if mat[i][d]%2==1:
                mat[i][d]=1
    for n in range(len(mat)):
        total=0
    
        for i in range(len(mat[i])):
            total=total+mat[n][i]*2**(len(mat[i])-1-i)
        res=res+str(total)+"  "
    return res
def luck_number():
    for i in range(len(mat)):
        for d in range(len(mat)):
            if mat[i][d]%2==0:
                mat[i][d]=0
            if mat[i][d]%2==1:
                mat[i][d]=1
    total=0
    for n in range(len(mat)):
        for i in range(len(mat[i])):
            total=total+mat[n][i]*2**(len(mat[i])-1-i)
    return total
        
                
#TOP LEVEL
import random as r
print 'Welcome to the "Diamond Treasure Hunter"game'
print
print "=============================================="
print
print
start=raw_input("Would you like to play?(y/n):")
print
print
a=0
totalpoint=0
while (a==0):
    point=0
    count=1
    if start=="y":
        print "One more game..."
        print "================"
        print
        print
        name=raw_input("Name of treasure hunter:")
        size=raw_input("Size of board(between 3 and 6 inclusive):")
        creation=raw_input("creation of board?(r-random,u-user):")
        if creation=="u":
            print "Provide a list of lists, same number of rows and columns"
            print "with integer numbers between 0 and 10 inclusive and maybe"
            mat=input("one -1 ==>")
        elif creation=="r":
            diamond=input("Maximum number diamonds in acell(from 1 to 10):")
            nrows=int(size)
            ncols=int(size)
            mat=[]
            for c in range(nrows):
                z=r.randint(0,diamond)
                mat.append([z])
            for c in range(nrows):
                for d in range(nrows-1):
                    z=r.randint(0,diamond)
                    mat[c].append(z)
                    print
        print
        print
        other_trip="y"
        while(other_trip=="y"):
            print "The board is"
            print "------------"
            print
            the_board()
            print
            print
            print"how would you want that",name,"travels?:"
            print"r-row"
            print"c-col"
            print"m-main diagonal"
            print"s-secondary diagonal"
            move=raw_input("x-random         :")
            if move=="r":
                colect=row()
            elif move=="c":
                colect=col()
            elif move=="m":
                colect=m_diagonal()
            elif move=="s":
                colect=s_diagonal()
            elif move=="x":
                colect=random_cells()
            point=point+colect
               
            print "Board after trip"
            the_board()
            other_trip=raw_input("Would you like to do another trip?(y/n):")
            if other_trip=="n":
                print
            elif other_trip=="y":
                    other_trip=="y"
            else:
                print"That is not a valid input, p[lease re-enter"
                other_trip=raw_input("Would you like to do another trip?(y/n):")
                while (other_trip!="y" and other_trip!="n"):
                    print"That is not a valid input, p[lease re-enter"
                    other_trip=raw_input("Would you like to do another trip?(y/n):")
            print
      
            
        result()
        totalpoint=totalpoint+point
        play_again=raw_input("would like to play again?")
        if play_again=="n":
            a=1
        elif play_again=="y":
            count=count+1
            a=0
    elif start=="n":
        final_result()
        a=1
    else:
        print "this is not vaild, ples try again."
        start=raw_input("Would you like to play?(y/n):")
final_result()
