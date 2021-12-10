import os

def cls():
  os.system("cls" if os.name == "nt" else "clear")

def print_game_state():
  cls()
  print()

  display = ""

  for i in range(9):
    square = i + 1

    if squares[i] == "":
      display += f" {square} "
    else:
      display += f" {squares[i]} "

    if square % 3 > 0:
      display += "|"
    elif square < 9:
      display += "\n---+---+---\n"

  print(f"{display}\n")

def get_square():
  while True:
    square = input("Which square? ")

    if square == "" or square not in "123456789":
      print("Choose 1-9.\n")
    elif squares[int(square) - 1] != "":
      print(f"Square {square} is occupied.\n")
    else:
      return int(square)

def three_in_row():
  ways_to_win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

  for way in ways_to_win:
    if all(squares[way[i]] == player for i in range(3)):
      return True

  return False

def board_is_full():
  return all(squares[i] != "" for i in range(9))

squares = ["", "", "", "", "", "", "", "", ""]
game_over = False
player = "X"

while not game_over:
  print_game_state()
  print(f"Player {player}:")

  square = get_square()
  squares[square - 1] = player

  if three_in_row():
    game_over = True
    print_game_state()
    print(f"Player {player} wins!")
  elif board_is_full():
    game_over = True
    print_game_state()
    print("Tie game")
  else:
    player = "O" if player == "X" else "X"
