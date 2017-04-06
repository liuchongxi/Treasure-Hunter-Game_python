# Treasure-Hunter-Game_python
This is my assignment 5 for CMPT 120.

The game is played on a board (square matrix) with integer numbers in each board cell. 
The board represents a diamond mine with tunnels and special passages.
The numbers represent the number of diamonds in each cell location.
Each time a new game starts the user provides the name for the treasure hunter and the values to create the board.
Each game may allow a hunter to do many "treasure trips".
The users can play as many games as he/she wants with a different hunter each game.

The user is require to:
  
    Run the program in Python 2.7 IDE
    Provide an input for the hunter's name
    Provide values to create a board
 
The game will then proceed.
The game specification is provided in more details in the assig5-explorer-diamonds.pdf.
Please refer to this file in the repo for more information.

Sample Run:
>>>==============================================RESTART================================================================================<<<
Welcome to the "Diamond Treasure Hunter" game

======================================

Would you like to play? (y/n): y

One more game...
 ================
Name of treasure hunter: Jones
Size of board (between 3 and 6 inclusive): 3
Creation of board? (r-random, u-user): u
Provide a list of lists, same number of rows and columns
 with integer numbers between 0 and 10 inclusive
and maybe one -1 ==> [[1,4,3],[0,2,5],[8,3,0]] 

The board is
------------
 Col 0 Col 1 Col 2
Row 0 1 4 3
Row 1 0 2 5
Row 2 8 3 0
How would you want that Jones travels?:
r - row
c - col
m - main diagonal
s - secondary diagonal
x - random : r
Number row (0 to 2): 1
positions visited: ...
 [1][0]
 [1][1]
 [1][2]
points obtained in this trip:... 6
Board after trip
 Col 0 Col 1 Col 2 
 Row 0 1 4 3
 Row 1 0 1 0
 Row 2 8 3 0
 
 Would you like Jones to do another trip? (y/n): y
The board is
------------
 Col 0 Col 1 Col 2
Row 0 1 4 3
Row 1 0 1 0
Row 2 8 3 0
How would you want that Jones travels?:
r - row
c - col
m - main diagonal
s - secondary diagonal
x - random : c
Number column (0 to 2): 12
That is not a valid input, please re-enter

Number column (0 to 2): a
The value should only have digits, please re-enter
Number column (0 to 2): !@
The value should only have digits, please re-enter
Number column (0 to 2): 1
positions visited: ...
 [0][1]
 [1][1]
 [2][1]
points obtained in this trip:... 6
Board after trip
 Col 0 Col 1 Col 2
Row 0 1 2 3
Row 1 0 0 0
Row 2 8 0 0
Would you like Jones to do another trip? (y/n): n
The treasure hunter Jones obtained 16 points in its game
The values of each row in the board (as binary number) are:
6, 0, 0, and therefore the board lucky number is: 6 


 
