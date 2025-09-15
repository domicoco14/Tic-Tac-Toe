print("""+ + + + + + + + + + + + + + +         + + + + + + + + + + + + + + +         + + + + + + + + + + + + + + + 
+  Welcome Player    to     +         +  Welcome Player    to     +         +  Welcome   Player  to     +
+                           +         +                           +         +                           +
+       DOMICOCODE          +         +       DOMICOCODE          +         +       DOMICOCODE          +
+                           +         +                           +         +                           +
+     TIC TAC TOE GAME      +         +     TIC TAC TOE GAME      +         +     TIC TAC TOE GAME      +
+                           +         +                           +         +                           +
+ + + + + + + + + + + + + + +         + + + + + + + + + + + + + + +         + + + + + + + + + + + + + + +      """)

print()

from random import randrange
brd= [1, 2, 3, 4, 5, 6, 7, 8, 9]

def board():
    print( "|**********|**********|********|")
    print(f"|    {brd[0]}     |     {brd[1]}    |    {brd[2]}   |")
    print( "|**********|**********|********|")
    print(f"|    {brd[3]}     |     {brd[4]}    |    {brd[5]}   |")
    print( "|**********|**********|********|")
    print(f"|    {brd[6]}     |     {brd[7]}    |    {brd[8]}   |")
    print( "|**********|**********|********|")

def check_win():
    if    (brd[0] == "X" and brd[1] == "X" and brd[2] == "X") or \
    (brd[3] == "X" and brd[4] == "X" and brd[5] == "X") or \
    (brd[6] == "X" and brd[7] == "X" and brd[8] == "X") or \
    (brd[0] == "X" and brd[3] == "X" and brd[6] == "X") or \
    (brd[1] == "X" and brd[4] == "X" and brd[7] == "X") or \
    (brd[2] == "X" and brd[5] == "X" and brd[8] == "X") or \
    (brd[0] == "X" and brd[4] == "X" and brd[8] == "X") or \
    (brd[2] == "X" and brd[4] == "X" and brd[6] == "X"):
        return ("Computer Wins!!! 💻💻💻")
    
    
    elif    =(brd[0] == "O" and brd[1] == "O" and brd[2] == "O") or \
    (brd[3] == "O" and brd[4] == "O" and brd[5] == "O") or \
    (brd[6] == "O" and brd[7] == "O" and brd[8] == "O") or \
    (brd[0] == "O" and brd[3] == "O" and brd[6] == "O") or \
    (brd[1] == "O" and brd[4] == "O" and brd[7] == "O") or \
    (brd[2] == "O" and brd[5] == "O" and brd[8] == "O") or \
    (brd[0] == "O" and brd[4] == "O" and brd[8] == "O") or \
    (brd[2] == "O" and brd[4] == "O" and brd[6] == "O"):
        return(f"\nCongratulations {player_name} You Win!!! 😁😎") 
        
def check_tie():
    if ((brd[0] in ["X","O"]) and
        (brd[1] in ["X","O"]) and
        (brd[2] in ["X","O"]) and
        (brd[3] in ["X","O"]) and
        (brd[4] in ["X","O"]) and
        (brd[5] in ["X","O"]) and
        (brd[6] in ["X","O"]) and
        (brd[7] in ["X","O"]) and
        (brd[8] in ["X","O"])) and not check_win():
        return "it's a tie 🤝🤝"

# def check_tie():
#     if all(i in ["X","O"] for i in board) and not check_win():
#         return "tie 🤝🤝"
player_name = input("Enter your gaming_name: ")
print()


def moves():
    while True:                                        
        
        while True:                                # Commputer's move loop
            computer_move = randrange(1,10)         
            if brd[computer_move - 1] not in ["X","O"]:
                brd[computer_move - 1] = "X"
                print()
                if computer_move == 1:
                    print("Computer chose 1️⃣")
                elif computer_move == 2: 
                    print("Computer chose 2️⃣\n")
                elif computer_move == 3: 
                    print("Computer chose 3️⃣\n")
                elif computer_move == 4: 
                    print("Computer chose 4️⃣\n")
                elif computer_move == 5: 
                    print("Computer chose 5️⃣\n")
                elif computer_move == 6: 
                    print("Computer chose 6️⃣\n")
                elif computer_move == 7: 
                    print("Computer chose 7️⃣\n")
                elif computer_move == 8: 
                    print("Computer chose 8️⃣\n")
                else:
                    print("Computer chose 9️⃣\n")
                break
        
        board()
        print()
        if check_tie():
            print(check_tie())
            return
        if check_win():
            print(check_win())
            return

                
        while True:                                       # Player's move loop
            print()
            try:                                    # To handle Invalid input from user
                player_move = int(input("Your turn! Pick a spot 🎯: "))
                if brd[player_move - 1] not in ["X","O"]:
                    brd[player_move - 1] = "O"
                    break
                else:
                    print("This spot has been taken, try again!!")
            except IndexError:                      # When number > 9 or number < 1
                print("That spot is not on the board! Choose a number between 1 and 9.")
            except ValueError:                      # when player number is not an integer
                print("Invalid input! Please enter a number between 1 and 9.")
        print()
        board()
        if check_tie():
            print(check_tie())
            return
        if check_win():
            print(check_win())
            return

board()
moves()

print("Thank you for playing my game, Gracias")