import random
import math
import time

# -------------------- GLOBAL TRACKERS --------------------
brain_points = 0
wins = 0
losses = 0
draws = 0

# -------------------- WELCOME --------------------
def welcome():
    print("\n🧠🤖 Welcome to BrainBot Arena – Study Break Edition 🤖🧠")
    print("“Small board. Big brain moves.”")
    print("Take a short reset before we begin...\n")
    time.sleep(1)
    print("🧘 Inhale...")
    time.sleep(1)
    print("Exhale...")
    time.sleep(1)
    print("Alright. Let’s play smart.\n")

# -------------------- ENERGY CHECK --------------------
def energy_check():
    print("How’s your energy right now?")
    print("1. Drained 😴")
    print("2. Okay-ish 🙂")
    print("3. Fully charged ⚡")
    return input("Choose (1-3): ")

# -------------------- MODE --------------------
def choose_mode():
    print("\nChoose your battle mode:")
    print("1. 😌 Chill Mode")
    print("2. 🔥 Savage Mode")
    print("3. 🎓 Study Break Mode")
    return input("Select mode (1-3): ")

# -------------------- SYMBOL --------------------
def choose_symbol():
    print("\nPick your symbol:")
    print("1. X")
    print("2. O")
    print("3. 🔥")
    print("4. ⭐")
    choice = input("Choose (1-4): ")

    symbols = ["X", "O", "🔥", "⭐"]
    player = symbols[int(choice)-1]
    bot = "O" if player != "O" else "X"
    return player, bot

# -------------------- BOARD --------------------
def print_board(board):
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def check_winner(board, symbol):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    return any(all(board[i] == symbol for i in combo) for combo in combos)

def is_full(board):
    return " " not in board

# -------------------- MINIMAX AI --------------------
def minimax(board, depth, is_max, bot, player):
    if check_winner(board, bot):
        return 1
    if check_winner(board, player):
        return -1
    if is_full(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = bot
                score = minimax(board, depth+1, False, bot, player)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = player
                score = minimax(board, depth+1, True, bot, player)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move(board, bot, player):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = bot
            score = minimax(board, 0, False, bot, player)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = bot

# -------------------- ATTITUDE RESPONSES --------------------
def attitude_response(result, mode):
    responses = {
        "win": [
            "Brain > Bot confirmed 🧠🔥",
            "Main character move right there.",
            "Sharp thinking!"
        ],
        "lose": [
            "Bot supremacy… temporarily 😌",
            "Processing complete. Victory acquired.",
            "Rematch?"
        ],
        "draw": [
            "Mental gym session complete.",
            "Balanced brains today.",
            "Strategic stalemate."
        ]
    }

    if mode == "2":  # Savage Mode
        print(random.choice(responses[result]))
    elif mode == "3":  # Study Mode
        if result == "win":
            print("Confidence builds momentum.")
        elif result == "lose":
            print("Progress > Perfection.")
        else:
            print("Balance is strength.")
    else:
        print("Good game.")

# -------------------- MOTIVATIONAL QUOTES --------------------
def motivational_quote():
    quotes = [
        "Consistency beats luck.",
        "Strategy is silent power.",
        "Think sharp. Move smart.",
        "Growth happens through play."
    ]
    print("💡", random.choice(quotes))

# -------------------- BRAIN FACT --------------------
def brain_fact():
    facts = [
        "Playing strategy games improves decision-making.",
        "Short breaks boost focus and retention.",
        "Mental challenges increase cognitive flexibility."
    ]
    print("🧠 Fun Fact:", random.choice(facts))

# -------------------- RANKING --------------------
def show_rank():
    global wins, losses, draws, brain_points
    print("\n📊 Your Stats")
    print("Wins:", wins)
    print("Losses:", losses)
    print("Draws:", draws)
    print("Brain Points:", brain_points)

    if wins > losses:
        print("Rank: Rising Strategist 🧠⚡")
    elif wins == losses:
        print("Rank: Balanced Thinker ⚖️")
    else:
        print("Rank: Learning Warrior 📚")

# -------------------- MAIN GAME LOOP --------------------
def play_game():
    global brain_points, wins, losses, draws

    welcome()
    energy_check()
    mode = choose_mode()
    player, bot = choose_symbol()

    while True:
        board = [" " for _ in range(9)]
        print("\n🎧 Imagine lo-fi music playing... Let’s focus.")
        print_board([str(i+1) for i in range(9)])

        while True:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
            else:
                print("Spot taken! Try again.")
                continue

            print_board(board)

            if check_winner(board, player):
                print("You win! 🎉")
                wins += 1
                brain_points += 50
                attitude_response("win", mode)
                break

            if is_full(board):
                print("It's a draw!")
                draws += 1
                attitude_response("draw", mode)
                break

            ai_move(board, bot, player)
            print_board(board)

            if check_winner(board, bot):
                print("AI wins!")
                losses += 1
                attitude_response("lose", mode)
                break

        motivational_quote()
        brain_fact()
        show_rank()

        again = input("\nPlay another round? (yes/no): ").lower()
        if again != "yes":
            print("\nBreak complete.")
            print("Brain refreshed.")
            print("Go win your real battles now. 🚀")
            break

play_game()
