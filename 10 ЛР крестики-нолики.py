import tkinter as tk
import random

def stop_game():
    global game
    for item in game_left:
        buttons[item].config(state="disabled")

def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (game[6] == n and game[7] == n and game[8] == n) \
        or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (game[2] == n and game[5] == n and game[8] == n) \
        or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True


def start_new_game():
    global game
    global game_left
    global turn

    game = [None] * 9
    game_left = list(range(9))
    turn = 0

    label.config(text="Крестики-нолики")
    for i in range(9):
        buttons[i].config(text=' ', state="normal")


def push(b):
    global game
    global game_left
    global turn
    game[b] = 'X'
    buttons[b].config(text='X')
    game_left.remove(b)
    if b == 4 and turn == 0:
        t = random.choice(game_left)
    elif b != 4 and turn == 0:
        t = 4
    if turn > 0:
            t = 8 - b
    if t not in game_left:
        try:
            t = random.choice(game_left)
        except IndexError:
            label.config(text='Game over!')
            stop_game()
    game[t] = '0'
    buttons[t].config(text='0')
    if win('X'):
        label.config(text='you win!')
        stop_game()
    elif win('0'):
        label.config(text='you lose!')
        stop_game()
    else:
        if (len(game_left) > 1):
            game_left.remove(t)
        else:
            label.config(text='draw!')
            stop_game()
        turn += 1

game = [None] * 9
game_left = list(range(9))
turn = 0

root = tk.Tk()
label = tk.Label(width=20, text = "Крестики-нолики")
buttons = [tk.Button(width=5, height=2, font=('Arial', 28), command = lambda x=i: push(x)) for i in range(9)]



label.grid(row=0, column=0, columnspan=3)
row = 1; col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

reset_button = tk.Button(root, text="Играть заново", command=start_new_game)
# Размещаем кнопку в новой строке под полем
reset_button.grid(row=row, column=0, columnspan=3, pady=10)


root.mainloop()






