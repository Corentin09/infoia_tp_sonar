from TicTacToe import TicTacToe, WIDTH, HEIGHT, SQUARE_SIZE
import pygame

def run(board: TicTacToe):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                if board.board[row][col] == "__":
                    if board.player == 1:
                        board.board[row][col] = "X"
                    else:
                        board.board[row][col] = "O"
                    board.player = -1*board.player

    return True

def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Morpions')

    board = TicTacToe()
    running = True

    while running:
        if not run(board):
            running = False

        if board.check_end():
            running = False

        board.show()
    
    pygame.quit()




if __name__ == "__main__":
    main()