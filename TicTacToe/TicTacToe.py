import pygame

WIDTH, HEIGHT = 360, 360
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)
ROWS, COLS = 3, 3
SQUARE_SIZE = WIDTH // COLS

CHECK_VICTORY = [[(0,0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

class TicTacToe:

    def __init__(self):
        self.player = 1
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.board = [["__" for _ in range(3)] for _ in range(3)]

        self.images = self.load_images()


    def load_images(self):
        pieces = ['X', 'O']
        images = {}
        for piece in pieces:
            image = pygame.image.load(f'image/{piece}.png').convert_alpha()
            image = pygame.transform.smoothscale(image, (SQUARE_SIZE, SQUARE_SIZE))
            images[piece] = image
        return images

    
    def draw_board(self) -> None:
        self.win.fill(WHITE)
        colors = [WHITE, GRAY]
        for row in range(ROWS):
            for col in range(COLS):
                color = colors[((row + col) % 2)]

                pygame.draw.rect(self.win, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        for row in range(1, ROWS):
            pygame.draw.line(self.win, BLACK, (0, row*SQUARE_SIZE), (360, row*SQUARE_SIZE), 4)
            pygame.draw.line(self.win, BLACK, (row*SQUARE_SIZE, 0), (row*SQUARE_SIZE, 360), 4)

    def show(self):
        self.draw_board()
        self.draw_symbol()
        pygame.display.flip()


    def draw_symbol(self) -> None:
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != "__":
                    self.win.blit(self.images[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

    def check_victory(self):
        for c in CHECK_VICTORY:
            symb = "__"
            check = True
            for i in c:
                row, col = i[0], i[1]
                if self.board[row][col] == "__":
                    check = False

                if symb == "__":
                    symb = self.board[row][col]
                elif symb != self.board[row][col]:
                    check = False
            if check:
                return symb
        return "__"
    
    def check_full(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] == "__":
                    return False
        return True
    
    def check_end(self):
        symb = self.check_victory()
        if symb == "X":
            print("Victoire du joueur X")
            return True
        elif symb == "O":
            print("Victoire du joueur O")
            return True
        elif self.check_full():
            print("Égalité")
            return True
        return False
                

    