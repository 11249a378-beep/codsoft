import math
import random

# Game Board
board = [" " for _ in range(9)]

# AI Messages
player_messages = [
    "Nice move!",
    "Interesting choice.",
    "You're making this challenging.",
    "That was clever.",
    "Let's see what happens next."
]

ai_messages = [
    "I'm thinking...",
    "I think I can win this one.",
    "Let's see if you can stop me.",
    "Calculating the best move...",
    "This match is getting interesting."
]

# Print Board
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Check Winner
def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for win in wins:
        if all(board[i] == player for i in win):
            return True

    return False

# Check Draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score

# AI Move
def ai_move():

    print("\nAI:", random.choice(ai_messages))

    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

# Human Move
def human_move():

    while True:
        try:
            move = int(input("\nEnter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                print("AI:", random.choice(player_messages))
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a valid number.")

# Welcome Message
print("=" * 40)
print("      TIC-TAC-TOE AI")
print("=" * 40)

print("\nYou are X")
print("AI is O")

print("\nBoard Positions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

print("\nAI: Welcome! Let's play.")
print("AI: Try your best... I'm not easy to beat. 😎")

# Main Game Loop
while True:

    print_board()

    # Human Turn
    human_move()

    if check_winner("X"):
        print_board()
        print("🎉 Congratulations! You win!")
        print("AI: Wow! That was impressive.")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        print("AI: Great game!")
        break

    # AI Turn
    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        print("AI: Good game! Maybe next time you'll beat me. 😄")
        break

    if is_draw():
        print_board()
        print("🤝 It's a draw!")
        print("AI: That was a close match!")