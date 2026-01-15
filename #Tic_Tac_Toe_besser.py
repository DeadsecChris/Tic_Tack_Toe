winners = []   # speichert die letzten 5 Gewinner


def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    print("\n  1   2   3")
    for i in range(3):
        print(f"{i+1} {board[i][0]} | {board[i][1]} | {board[i][2]}")
        if i < 2:
            print("  ---------")


def check_win(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True

    if all(board[i][i] == symbol for i in range(3)):
        return True
    if all(board[i][2-i] == symbol for i in range(3)):
        return True

    return False


def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True


def show_winners():
    print("\n--- Letzte Gewinner ---")
    if not winners:
        print("Noch keine Spiele gespielt.")
    else:
        for i, name in enumerate(winners, 1):
            print(f"{i}. {name}")


def play_game():
    print("\n--- Tic Tac Toe ---")
    show_winners()   # Gewinner anzeigen

    player1 = input("\nName Spieler X: ")
    player2 = input("Name Spieler O: ")

    board = create_board()
    current_player = player1
    symbol = "X"

    while True:
        print_board(board)
        print(f"\n{current_player} ({symbol}) ist am Zug")

        try:
            row = int(input("Zeile (1-3): ")) - 1
            col = int(input("Spalte (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Ungültige Eingabe!")
                continue

            if board[row][col] != " ":
                print("Feld bereits belegt!")
                continue

            board[row][col] = symbol

            if check_win(board, symbol):
                print_board(board)
                print(f"\n🎉 {current_player} hat gewonnen!")

                winners.append(current_player)
                if len(winners) > 5:
                    winners.pop(0)   # ältesten löschen

                break

            if check_draw(board):
                print_board(board)
                print("\n🤝 Unentschieden!")
                break

            if symbol == "X":
                symbol = "O"
                current_player = player2
            else:
                symbol = "X"
                current_player = player1

        except ValueError:
            print("Bitte nur Zahlen eingeben!")


def main():
    while True:
        play_game()
        again = input("\nNeue Runde? (j/n): ").lower()
        if again != "j":
            print("Spiel beendet.")
            break


main()