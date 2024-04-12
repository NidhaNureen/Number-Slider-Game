import random

def main():
    tiles_list = [str(num) for num in generate_random_list()]
    draw_grid(tiles_list)
    user_moves(tiles_list)

def user_moves(tiles_list):
    # Count number of valid moves
    valid_moves_counter = 0

    # Check if the puzzle is already solved or not
    if is_solved(tiles_list):
        print(f"You won in {valid_moves_counter} moves. Congratulations!")
        return

    while True:
        user_move = input("Your move (or type 'quit' to end game): ")

        # If user wishes to quit
        if user_move == "quit":
            print("Goodbye!")
            return

        # Check validity of user's move, if valid, can swap tile
        if user_move in tiles_list:
            tile_index = tiles_list.index(user_move)

            if is_valid_move(tile_index, tiles_list):
                swap_tiles(tiles_list, user_move), draw_grid(tiles_list)
                valid_moves_counter += 1
            else:
                print(f"{user_move} is not valid. Try again.")

        else:
            print(f"{user_move} is not valid. Try again.")

        # Check if puzzle is solved
        if is_solved(tiles_list):
            print(f"You won in {valid_moves_counter} moves. Congratulations!")
            return

def generate_random_list():
    # Generate a list of numbers from 1 to 8
    numbers = list(range(1, 9))

    # Insert a blank at a random index in list
    blank_index = random.randint(0, 8)
    numbers.insert(blank_index, '')

    return numbers

# Function to display the grid
def draw_grid(tiles_list):
    grid_size = int(len(tiles_list) ** 0.5)

    # Draw top of grid
    print('┌────' + '┬────' * (grid_size - 1) + '┐')
    # Draw rows of grid
    for i in range(grid_size):
        row = "│"
        for j in range(grid_size):
            label = tiles_list[i * grid_size + j]
            if label == '':
                label = '   '
            elif len(label) == 1:
                label = '  ' + label
            elif len(label) == 2:
                label = ' ' + label
            row += label + ' │'
        print(row)
        if i < grid_size - 1:
            print("├────" + "┼────" * (grid_size - 1) + "┤")
    # Draw bottom of grid
    print("└────" + "┴────" * (grid_size - 1) + "┘")


# Function to check if user move is valid
def is_valid_move(tile_index, tiles_list):
    # Find row and column of tile chosen
    tile_row = tile_index // int(len(tiles_list) ** 0.5)
    tile_column = tile_index % int(len(tiles_list) ** 0.5)

    # Find index of the empty tile and its row and column
    index_empty = tiles_list.index('')
    row_empty = index_empty // int(len(tiles_list) ** 0.5)
    column_empty = index_empty % int(len(tiles_list) ** 0.5)

    # Check if user move is orthogonally adjacent to empty tile
    if tile_row == row_empty and abs(tile_column - column_empty) == 1:
        return True
    elif tile_column == column_empty and abs(tile_row - row_empty) == 1:
        return True
    else:
        return False


# Function to swap blank tile with user's choice
def swap_tiles(tiles_list, user_move):
    tile_index = tiles_list.index(user_move)
    index_empty = tiles_list.index('')
    tiles_list[tile_index] = ''
    tiles_list[index_empty] = user_move


# Function to check if the puzzle is solved
def is_solved(tiles_list):
    numbers = [int(tile) for tile in tiles_list if tile.isdigit()]
    # Check if numbers in grid are in ascending order and last tile is blank
    if numbers == sorted(numbers) and tiles_list[-1] == '':
        return True
    else:
        return False

main()
