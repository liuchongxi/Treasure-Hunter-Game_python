'''
CMPT 120 2015-1
Assignment #5
Game: Diamond Treasure Hunter game

Instructor and author: Diana Cukierman



'''

def welcome_general():
    print ' Welcome to the "Diamond Treasure Hunter" game ' + \
          '\n=============================================\n\n'

def welcome_game():
    print '\n\n  One more game... ' + \
          '\n  ================\n\n'


### generic basic ask_user (this function is not required,
### one could have separate functions to deal with
### asking the user different types of values and valid ranges
    
def  ask_user(mssg,conversion,validIn,validOut):
    '''
    ask user with basic range validation
    
    input parameters:
        mssg -  message to the user
        conversion - "int" - conversion to int needed
                     "String" - no conversion needed
        validIn  - valid values (used to validate)
        validOut - the string "same" indicates that the same value that
                   the user inputs should be provided as result
                 - a list with values corresponding to the input values
                    
    output (returned values):
        value input (if validOut is "same" or some value
        corresponding to the value input             
    '''
    ok = False
    while (not ok):
        value = raw_input(mssg)
        if conversion == "int":
            while (not value.isdigit()):
                 print "The value should only have digits, please re-enter"
                 value = raw_input(mssg)
            value = int(value)  
        
        if (value not in validIn): # applicable for both int or String
            print "That is not a valid input, please re-enter"
        else:
            ok = True
        
        
    if (validOut == "same"):
        result = value
    else: 
        indexInVin = validIn.index(value)
        result = validOut[indexInVin]
    return result


def pp_matrix(title, matrix):
    '''
    only prints (pp: pretty print) - no values are returned
    assumes that it is a square matrix, implemented
    as a list or rows, where each row is a list
    (therefore the matrix has the same number of rows and columns,
    and all rows have the same number of columns)
    '''
    print title
    dim = len(matrix)
    print "\t     ",    #"\t" is a tabulating special character

    #printing titles of column numbers
    for c in range(0,dim):
        print "Col " + str(c) + "\t",
    #printing the matrix
    for r in range(0,dim):
        print "\nRow " + str(r) + "\t",
        for c in range(0,dim):
            print "\t", matrix[r][c],
    print


def create_random_row(dim,maxdiam):
    '''
    row with random integer numbers between 0 and maxdiam inclusive
    '''
    # the random module is imported globally
    row = []
    for r in range(0,dim):
        value = random.randint(0,maxdiam)
        row.append(value)
    return row

def create_random_board(dim,maxdiam):
    '''
    list of rows with random integers between 0 and maxdiam
    and one -1 with 80% chance
    '''
    board = []
    for r in range(0,dim):
        row = create_random_row(dim,maxdiam)
        board.append(row)
        
    include_minus = random.randint(0,10)  
    if (include_minus <= 8):  # 80% chance
        r = random.randint(0,dim-1)
        c = random.randint(0,dim-1)
        board[r][c] = -1
        
    return board

def create_user_board(dim):
    
    '''
    accepts list of lists from user - no validation
    input must be used insted of raw_input
    '''
    board = input("Provide a list of lists, same number of rows and columns" + \
                  "\n with integer numbers between 0 and 10 inclusive" + \
                  "\nand maybe one -1 ==> ")
    return board




def ask_user_modality_trip(board,hunter):
    # variables are initialized here with default values for
    # modalities that do not need them
    num = 0
    direction = ""
    
    pp_matrix("\nThe board is"+ \
              "\n------------\n", board)

    message_for_user = "\nHow would you want that " + hunter + \
                        " travels?: \n" + \
                        "r - row \n" + \
                        "c - col \n" + \
                        "m - main diagonal \n" + \
                        "s - secondary diagonal \n" + \
                        "x - random\t\t: "
    
    valid_inputs = ['r','R','c','C','m','M','s','S','x','X']
    
    modality = ask_user(message_for_user, "String", valid_inputs, "same")

    valid_positions = range(0,len(board))
    
    if (modality == 'r' or modality == "R"):
        num = ask_user("\nNumber row (0 to "+ str(len(board)-1) + "): ", \
                       "int", valid_positions,"same")
        
    if (modality == 'c' or modality == "C"):
        num = ask_user("\nNumber column (0 to "+ str(len(board)-1) + "): ", \
                       "int", valid_positions,"same")

    if (modality == 'x' or modality == "X"):
        num_cells = len(board)*len(board)
        num = ask_user("\nHow many random cells shall " + hunter + \
                        " visit?: ", "int",range(1,num_cells+1),"same")               
    


    
    
    return modality,num

def get_row(matrix,num_row):
    '''
    given a matrix and a row number 
    returns two lists:
    one list with the elements in that row
    another list with the positions as they are visited
    no printing is done here yet
    '''
    
    cells = []
    rows = []
    cols = []
    
    ### the range function produces a list: trajectory

    
    trajectory = range(0,len(matrix))
    
        
    for c in trajectory:
        cells.append(matrix[num_row][c])
        rows.append(num_row)
        cols.append(c) 
    return cells, rows,cols

def get_col(matrix,num_col):
    
    cells = []
    rows = []
    cols = []
    
    
    trajectory = range(0,len(matrix))
    
        
    for r in trajectory:
        cells.append(matrix[r][num_col])
        rows.append(r)
        cols.append(num_col)
    return cells, rows,cols   

def get_main(matrix):
    
    cells = []
    rows = []
    cols = []
    
    trajectory = range(0,len(matrix))
        
    for i in trajectory:
        cells.append(matrix[i][i])
        rows.append(i)
        cols.append(i)
    return cells, rows,cols

def get_secondary(matrix):
    
    cells = []
    rows = []
    cols = []
    
    trajectory = range(0,len(matrix))
        
    for r in trajectory:
        c = len(matrix)-r-1
        cells.append(matrix[r][c])
        rows.append(r)
        cols.append(c)
    return cells, rows,cols  

def get_random(matrix,num):
    
    cells = []
    rows = []
    cols = []
        
    for x in range(num):
        r = random.randint(0,len(matrix)-1)
        c = random.randint(0,len(matrix)-1)
        cells.append(matrix[r][c])
        rows.append(r)
        cols.append(c)
        
    return cells, rows,cols  


def get_Nupdate_points_and_show_trip(board,cells_list,rows_list,cols_list):
    #print "TRACE: cells_list, positions_list",cells_list, rows_list,cols_list
    '''
    this function does not know whether the values and positions
    come from a row or a column or others. it just receives three lists,
    one with the cell contents, and  with the row positions and
    one with the cols positions
    '''
    
    print "\npositions visited: ..."
    trapped = False
    points = 0
    i = 0
    while i < len(cells_list) and not trapped:
        r = rows_list[i]
        c = cols_list[i]
        cell = cells_list[i]
        if cell != -1:
            if cell%2 == 0:
                picked = cell/2
                
            else:
                picked = cell
            print " " + "[" + str(r) + "][" + str(c) + "]"
            points = points + picked
            board[r][c] = board[r][c] - picked
            
            
        else:
            trapped = True
            print " " + "[" + str(r) + "][" + str(c) + "]" + "   ooooh! a -1!! "
        i = i + 1
        
    print "\npoints obtained in this trip:... ", points
    pp_matrix("Board after trip",board)
    return points, trapped

def travel(board,modality,num):

    
    if (modality == "r"):
        cells_list,rows_list,cols_list = get_row(board,num)    
    elif (modality == "c"):
        cells_list,rows_list,cols_list = get_col(board,num)
    elif (modality == "m"):
        cells_list,rows_list,cols_list = get_main(board)
    elif (modality == "s"):
        cells_list,rows_list,cols_list = get_secondary(board)
    else:  #(modality == "x")
        cells_list,rows_list,cols_list = get_random(board,num)

    points, trapped = \
            get_Nupdate_points_and_show_trip(board,cells_list,rows_list,cols_list)
    return points, trapped


def do_one_trip(board,hunter):
    
    modality,num = ask_user_modality_trip(board,hunter)
    points, trapped = travel(board,modality,num)
    return points, trapped 




def play_one_game(board,hunter):
    '''
    a hunter can do several trips, in a modality as chosen
    by the user and as many trips as the user wants or
    until the hunter gets trapped (falls in a -1 cell).
    as the hunter travels, accumulates points
    the boolean variable trapped is true if the hunter gets trapped
    '''

    total_points = 0 ## the hunter's points

    ## forcing at least one trip
    trapped = False
    one_more = True

    while ((not trapped) and one_more):
        
        points, trapped = do_one_trip(board,hunter)  # points - the points
                    # corresponding to one trip only
        total_points = total_points + points

        if (trapped):
            print "\n Oh no! " + hunter + " got trapped!\n" + \
                  hunter + " cannot travel again :(  "
        else:
            one_more = ask_user("\n\nWould  you like " + hunter + \
                            " to do another trip? (y/n): ","String", \
                            ['y','Y','n','N'], \
                            [True,True,False,False])
        
    # end of while loop - the hunter may be trapped or the user did not want
    # the hunter to travel again. here we do not care to identify
    # which situation it is, trapped is returned from here and 
    # it will be considered outside this function
            
    print "\n" "The treasure hunter " + hunter + " obtained " + \
          str(total_points) + " points in its game"
    return total_points, trapped 


def convert_2_to_10(lbin):
    '''
    lbin is a binary number represented as a list of 's and 1's
    it may have a -1 (which will be treated as a 1 for this conversion process
    '''
    dim = len(lbin)
    val = 0
    for i in range(0,dim):
        digit = abs(lbin[i])  #if there is a -1, it is changed to 1
        exponent = dim -1 -i
        val = val + digit*2**exponent
    #print "TRACE 2 to 10, lbin,val",lbin,val
    return val


def obtain_list_0s_1s(board,row_num):
    lbin = []
    for c in range(0,len(board[row_num])):  
        lbin.append(board[row_num][c] %2) #(0 or 1 depending if even or odd)
    return lbin

def calculate_and_print_board_lucky_num(board):
    '''
    each row is treated as a binary number and converted to base 10
    and then appended to a list with the values of each row.
    num accumulates these values
    '''
    values = []
    num = 0
    for r in range(0,len(board)):
        row = board[r]
        lbin = obtain_list_0s_1s(board,r)
        val_row = convert_2_to_10(lbin)
        num = num + val_row
        values.append(val_row)

    print "\nThe values of each row in the board (as binary number) are:"
    for v in values:
        print str(v)+",",
    print " and therefore the board lucky number is:",num
    return num



def show_totals():
    '''
    uses global variables with totals, minimums and maximums
    '''
    
    print
    print "Total hunters that played: ", total_hunters
    print "Total points of all hunters: ", total_hunters_points
    
    if trapped_state_max_hunter:
        state = "trapped"
    else:
        state = "fine"
        
    print
    print "Maximum hunter points: "
    print "  The hunter " + name_max_hunter + ", who is " + state + ",\n" + \
          "  got the maximum points: " + str(maximum_hunter_points)
    
    if trapped_state_min_lucky_hunter:
        state = "trapped"
    else:
        state = "fine"

    print
    print "Minimum lucky number: "

    if minimum_board_lucky_num == MAX_LUCKY:
        lucky_to_print = "n/a"
    else:
        lucky_to_print = str(minimum_board_lucky_num)
        
    print "  The board with the hunter " + name_min_lucky_hunter + ", who is " \
          + state + ",\n" + \
          "  got the minimum lucky number: " + lucky_to_print


def say_bye():
    print "\n\nBye"


###  ---------------- TOP LEVEL ----------------


# ---------------- INITIALIZE GENERAL ----------------

import random

# initialize totals and results for all games
total_hunters = 0
total_hunters_points = 0

maximum_hunter_points = 0
name_max_hunter = ""
trapped_state_max_hunter = False

MAX_LUCKY = 6*(2**6-1) + 1
          ## (a number which is greater (+1) than any possible lucky number
          ##  the largest board has dimension 6, the largest binary number
          ##  corresponding to one row is 2**6 - 1, adding 6 rows gives us
          ##  6 * (2**6 - 1)

minimum_board_lucky_num = MAX_LUCKY
name_min_lucky_hunter = ""
trapped_state_min_lucky_hunter = False

num_games = 0

# ---------------- START ALL GAMES ----------------

welcome_general()
play_again = ask_user("Would  you like to play? (y/n): ", \
                      "String",\
                      ['y','Y','n','N'], \
                      [True,True,False,False])

while (play_again):

    welcome_game()

    # ---------------- ASK INITIAL VALUES FOR ONE GAME ----------------
    # ask for hunter name (no validation done)
    this_hunter = raw_input("Name of treasure hunter: ")

    # ask for dim for board - validation that it is an integer
    # and values are in [3,4,5,6] (which is the same as range(3,7))
    dim = ask_user("Size of board (between 3 and 6 inclusive): ","int",
                   range(3,7),"same")

    # ask option board creation
    create_random = ask_user("Creation of board? (r-random, u-user): ", \
                             "String",['r','R','u','U'], \
                             [True,True,False,False])
    
    if (create_random):
        maxdiam = ask_user("Maximum number diamonds in a cell (from 1 to 10): ", \
                           "int",range(1,11),"same")
        board = create_random_board(dim,maxdiam)
    else:
        board = create_user_board(dim)
         

    #---------------- CORE ONE GAME ----------------
    
   
    this_hunter_points, this_hunter_state = play_one_game(board,this_hunter)
    # board and hunter could be used in play_one_game
    # directly using the global variables, but are passed here to make it
    # more explicit that they are used there
    

    #---------------- PROCESS TOTALS THIS GAME ----------------
    
    # accumulate totals
    total_hunters = total_hunters + 1
    total_hunters_points = total_hunters_points + this_hunter_points

    # revise max hunter points
    if (this_hunter_points >= maximum_hunter_points):
        maximum_hunter_points = this_hunter_points
        name_max_hunter = this_hunter
        trapped_state_max_hunter = this_hunter_state

    # this board lucky number
    this_board_lucky_num = calculate_and_print_board_lucky_num(board)
 
    # revise min board lucky number
    if (this_board_lucky_num <= minimum_board_lucky_num):
        minimum_board_lucky_num = this_board_lucky_num
        name_min_lucky_hunter = this_hunter
        trapped_state_min_lucky_hunter = this_hunter_state

    # ---------------- WANT TO PLAY AGAIN? ----------------
    play_again = ask_user("\nWould  you like to play again? (y/n): ", \
                          "String",['y','Y','n','N'], \
                          [True,True,False,False])

# ---------------- end outside while loop: no more games

show_totals() # will use global variables
say_bye()

# END


    
        
    
