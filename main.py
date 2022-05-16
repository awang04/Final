#This code is written through collaboration

is_there_a_winner = False
#Varibles 
a = "-"
b = "-"
c = "-"
d = "-"
e = "-"
f = "-"
g = "-"
h = "-"
i = "-"
x = "x"
o = "O"
reset = "-"
#Board varibles 
row1 = [a,b,c]
row2 = [d,e,f]
row3 = [g,h,i]
#resets the board and set winner to false.
def resetBoard():
  global is_there_a_winner
  row1[0] = reset 
  row1[1] = reset
  row1[2] = reset
  row2[0] = reset 
  row2[1] = reset
  row2[2] = reset
  row3[0] = reset 
  row3[1] = reset
  row3[2] = reset
  is_there_a_winner = False
  
#supposed to Print the board
def print_board():
  print(row1)
  print(row2)
  print(row3)
#Checks if user wins supposed to return true inorder to stop the while loop.
def win_condition():
  if row1[0] == x and row1[1] == x and row1[2] == x:
    print("User 1 wins")
    return True
  elif row2[0] == x and row2[1] == x and row2[2] == x:
    print("User 1 wins")
    return True
  elif row3[0] == x and row3[1] == x  and row3[2] == x:
    print("User 1 wins")
    return True
  elif row1[0] == x and row2[1] == x  and row3[2] == x:
    print("User 1 wins")
    return True
  elif row1[0] == x and row2[0] == x  and row3[0] == x:
    print("User 1 wins")
    return True
  elif row1[1] == x and row2[1] == x  and row3[1] == x:
    print("User 1 wins")
    return True
  elif row1[2] == x and row2[2] == x  and row3[2] == x:
    print("User 1 wins")
    return True
  elif row1[2] == x and row2[1] == x  and row3[0] == x:
    print("User 1 wins")
    return True
  elif row1[0] == o and row1[1] == o and row1[2] == o:
    print("User 2 wins")
    return True
  elif row2[0] == o and row2[1] == o and row2[2] == o:
    print("User 2 wins")
    return True
  elif row3[0] == o and row3[1] == o  and row3[2] == o:
    print("User 2 wins")
    return True
  elif row1[0] == o and row2[0] == o and row3[0] == o:
    print("User 2 wins")
    return True
  elif row1[1] == o and row2[1] == o  and row3[1] == o:
    print("User 2 wins")
    return True
  elif row1[2] == o and row2[2] == o  and row3[2] == o:
    print("User 2 wins")
    return True
  elif row1[2] == o and row2[1] == o  and row3[0] == o:
    print("User 2 wins")
    return True
  else:
    return False

#the main method declare global var to begin with
def game():
  global x
  global o
  global row1
  global row2
  global row3
  global is_there_a_winner
  count = 0
  while is_there_a_winner == False:
    #checks if board is filled stops the game at 10 inputs no matter what. 
    if count == 10: 
      break
      #take in user 1 input and update var then print out new board.
    q = input("User 1, pick a letter a-i: ")
    count += 1
    if q == "a" and a != o:
      row1[0] = x
      print_board()
      win_condition()
    elif q == "b" and b != o:
      row1[1] = x 
      print_board()
      win_condition()
    elif q == "c" and c != o:
      row1[2] = x 
      print_board()
      win_condition()
    elif q == "d" and d != o:
      row2[0] = x
      print_board()
      win_condition()
    elif q == "e" and e != o:
      row2[1] = x
      print_board()
      win_condition()
    elif q == "f" and f != o:
      row2[2] = x
      print_board()
      win_condition()
    elif q == "g" and g != o:
      row3[0] = x
      print_board()
      win_condition()
    elif q == "h" and h != o:
      row3[1] = x
      print_board()
      win_condition()
    elif q == "i" and i != o:
      row3[2] = x
      print_board()
      win_condition()
    else:
      print("thats not in the range of a-i")
      break
    
    if win_condition() == True:
      is_there_a_winner = True
      break
    #stops the game when board is filled.
    if count == 9:
      print("Draw")
      break
      
    print_board
    #Take in user 2 input then prints new board also checks win_condition
    z = input("User 2, pick a letter a-i: ")
    count += 1
    if z == "a" and a != x:
      row1[0] = o
      print_board()
      win_condition()
    elif z == "b" and b != x:
      row1[1] = o
      print_board()
      win_condition()
    elif z == "c" and c != x:
      row1[2] = o 
      print_board()
      win_condition()
    elif z == "d" and d != x:
      row2[0] = o
      print_board()
      win_condition()
    elif z == "e" and e != x:
      row2[1] = o
      print_board()
      win_condition()
    elif z == "f" and f != x:
      row2[2] = o
      print_board()
      win_condition()
    elif z == "g" and g != x:
      row3[0] = o
      print_board() 
      win_condition()
    elif z == "h" and h != x:
      row3[1] = o
      print_board() 
      win_condition()
    elif z == "i" and i != x:
      row3[2] = o
      print_board()
      win_condition()
    else:
      print("thats not in the range of a-i")
      break
      #takes userinput and loop the value to run the total amount of code.
def gameAmount(games):
    for x in range(games):
      resetBoard()
      print_board()
      game()
      print("-------------------------")
      
      
#start the game/code
games = int(input("how many games do you want to play? "))
gameAmount(games)

