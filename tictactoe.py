def print_board(grid):
    print("\n")
    print(f" {grid[0][0]} | {grid[0][1]} | {grid[0][2]} ")
    print("---+---+---")
    print(f" {grid[1][0]} | {grid[1][1]} | {grid[1][2]} ")
    print("---+---+---")
    print(f" {grid[2][0]} | {grid[2][1]} | {grid[2][2]} ")
    print("\n")

def check_win(grid, player):
    # Проверка строк и столбцов
    for i in range(3):
        if all(grid[i][j] == player for j in range(3)) or all(grid[j][i] == player for j in range(3)):
            return True
    # Проверка диагоналей
    if all(grid[i][i] == player for i in range(3)) or all(grid[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(grid):
    return all(cell in ['X', 'O'] for row in grid for cell in row)

def play_game():
    # Игровое поле на основе вашего JSON grid_layout
    grid = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    
    current_player = "X"
    
    print("=== Крестики-нолики ===")
    print("Вводите номер клетки (от 1 до 9), чтобы сделать ход.")

    while True:
        print_board(grid)
        move = input(f"Ход игрока [{current_player}]. Выберите клетку (1-9): ")
        
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Ошибка! Введите число от 1 до 9.")
            continue
            
        move = int(move)
        # Находим координаты по введенному числу
        row = (move - 1) // 3
        col = (move - 1) % 3
        
        if grid[row][col] in ['X', 'O']:
            print("Эта клетка уже занята! Выберите другую.")
            continue
            
        grid[row][col] = current_player
        
        if check_win(grid, current_player):
            print_board(grid)
            print(f"🎉 Игрок [{current_player}] победил!")
            break
            
        if check_draw(grid):
            print_board(grid)
            print("🤝 Ничья!")
            break
            
        # Смена игрока
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_game()
