import sys
import random
import copy

class MineSweeper(object):
    '''
    initialize the board
    randomly set some bombs at the hidden board
    init win/lose flag
    '''
    def __init__(self, width, length, mine_percentage):
        if width == 0:
            raise Exception('width cannot be zero')
        if length == 0:
            raise Exception('length cannot be zero')

        self.board = [['*' for _ in range(width)] for _ in range(length)]
        self.mines = copy.deepcopy(self.board)

        self.minesNum = self._setMines(mine_percentage)
        self.bombed = False

    '''
    help to randomly set bombs
    '''
    def _setMines(self, mine_percentage):
        counter = 0
        for i in range(len(self.mines)):
            for j in range(len(self.mines[i])):
                r = random.random()
                if r <= mine_percentage:
                    self.mines[i][j] = 'X'
                    counter += 1
        return counter

    def _printboard(self, board):
        for row in board:
            print ' '.join(row) + '\n'
        return ;

    def start(self):
        print "Welcome to my MineSweeper."
        self._printboard(self.board)
        print "---------------------"
        # self._printboard(self.mines)
        self._loop()

    '''
    Main loop of the game
    '''
    def _loop(self):
        while not self.bombed:
            x, y = parse_move(raw_input("Please enter your next move like this: '(x, y)':"))
            assert isinstance(x, int) and isinstance(y, int)
            res = self.clickWin(x, y)
            if res == 1:
                break
        if self.bombed:
            print "Bomb!"
        else:
            print "You won!"

        return ;

    '''
    user's input at each round triggers this function during the main loop
    it returns a number everytime indicating if (x, y) is bomb or the game should continue
    '''
    def clickWin(self, x, y):
        if x < 0 or x >= len(self.board) or y < 0 or y >= len(self.board[0]):
            raise Exception("WRONG INPUT")

        if self.mines[x][y] == 'X':
            self.bombed = True
            return 0
        else:
            self._show_safe_area(x, y)
            if self._win():
                return 1
            else:
                return 0

    '''
    This wraps around the core_bfs function and uses self._printboard() to print the state of the board after each successful move.
    In mineSweeper, if it were a successful move, it will somehow display a range of safe locations with numbers on them,
    indicating how many bombs are around them.
    '''
    def _show_safe_area(self, x, y):
        safe_list = self._find_safe_area(x, y)
        for tup in safe_list:
            x, y, n = tup
            self.board[x][y] = str(n)
        self._printboard(self.board)

    '''
    This is the core_bfs function, where it will keep exploring safe locations until some bomb nearby is detected.
    '''
    def _find_safe_area(self, x, y):
        safe_list = []
        # avoid re-visit
        visited = [[False for _ in range(len(self.board))] for _ in range(len(self.board[0]))]
        # bfs queue
        queue = [(x, y)]
        while len(queue) > 0:
            x, y = queue.pop(0)
            visited[x][y] = True
            bomb_counter = 0
            # keep tracks of how many bombs are actually around this (x, y) in its "one-step vicinity"
            for i in range(-1, 2):
                for j in range(-1, 2):
                    # sanity check
                    if x + i < 0 or x + i >= len(self.board) or y + j < 0 or y + j >= len(self.board[0]): continue
                    if visited[x+i][y+j]: continue

                    if self.mines[x+i][y+j] == 'X':
                        bomb_counter += 1
                    else:
                        queue.append((x+i, y+j))
            safe_list.append((x, y, bomb_counter))
            # stop exploring when some bomb is discovered.
            if bomb_counter > 0:
                break

        return safe_list

    '''
    I was unclear about how to judge if the game is won. This is the solution I can think of. It will be checked everytime a user makes a move.
    '''
    def _win(self):
        counter = 0
        for row in self.board:
            for cell in row:
                if cell == '*':
                    counter += 1
        if counter == self.minesNum:
            return True
        elif counter < self.minesNum:
            raise Exception("WRONG PROGRAM")
        else:
            return False

'''
parse user's input
'''
def parse_move(strTup):
    if strTup[0] != '(': raise Exception("WRONG INPUT")
    if strTup[-1] != ')': raise Exception("WRONG INPUT")

    movelist = strTup[1:-1].split(',')
    if len(movelist) != 2: raise Exception("WRONG INPUT")

    try:
        x = int(movelist[0])
        y = int(movelist[1])
    except ValueError:
        raise Exception("WRONG INPUT")

    return x, y


def main():
    ms = MineSweeper(int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]))
    ms.start()


if __name__ == '__main__':
    main()
