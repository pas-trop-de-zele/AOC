class Board:
    def __init__(self, matrix):
        self.M = [[0 for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                self.M[i][j] = matrix[i][j]
    
        self.marked = [[False for _ in range(5)] for _ in range(5)]
        
    def pick(self, x):
        for i in range(5):
            for j in range(5):
                if self.M[i][j] == x:
                    self.marked[i][j] = True
    
    def win(self):
        for i in range(5):
            row_marked = True
            for j in range(5):
                row_marked &= self.marked[i][j] == True
            if row_marked:
                return True
        
        for j in range(5):
            col_marked = True
            for i in range(5):
                col_marked &= self.marked[i][j] == True
            if col_marked:
                return True
    
    def display(self):
        for r in self.M:
            for c in r:
                print(c, end=' ')
            print()
        print()

    def show_marked(self):
        for r in self.marked:
            for c in r:
                print(c, end=' ')
            print()
        print()