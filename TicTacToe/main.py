from TicTacToe import TicTacToe, WIDTH, HEIGHT, SQUARE_SIZE
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Morpions')

    board = TicTacToe()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[1] // SQUARE_SIZE, pos[0] // SQUARE_SIZE
                if board.board[row][col] == "__":
                    if board.player == 1:
                        board.board[row][col] = "X"
                    else:
                        board.board[row][col] = "O"
                    board.player = -1*board.player

        symb = board.check_victory()
        if symb == "X":
            print("Victoire du joueur X")
            running = False
        elif symb == "O":
            print("Victoire du joueur O")
            running = False

        if board.check_full():
            print("Égalité")
            running = False

        board.draw_board()
        board.draw_symbol()
        pygame.display.flip()
    
    pygame.quit()




if __name__ == "__main__":
    main()