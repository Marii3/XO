from random import randint

class Model:
    def __init__(self, player = 'x', comp = 'o'):
        self.player = player
        self.comp = comp
        self.newGame()
        
        
    def printField(self):
        for i in range(len(self.arr)):
            for j in range(len(self.arr[i])):
                print(f"{self.arr[i][j]:>3}", end="")
            print()
        print()
    
    def turn(self, row, col):
        if self.arr[row][col] != 0:
            return False
        self.arr[row][col] = self.player
        self.count+=1
        return True
        
    
    def comp_turn(self):
        if self.count > 9:
            return False
        while True:
            row = randint(0,2)
            col = randint(0,2) 
            if self.arr[row][col] == 0:
                self.count+=1
                self.arr[row][col] = self.comp
                return row, col
    
    def checkWinner(self):
        for i in range(len(self.arr)):
            if self.arr[i][0] == self.arr[i][1] == self.arr[i][2] and self.arr[i][0] != 0:
                return self.arr[i][0]
                
            elif self.arr[0][i] == self.arr[1][i] == self.arr[2][i] and self.arr[0][i] != 0:    
                return self.arr[0][i]
                
            elif self.arr[1][1] != 0 and ((self.arr[0][0] == self.arr[1][1] == self.arr[2][2]) or (self.arr[0][2] == self.arr[1][1] == self.arr[2][0])):
                return self.arr[1][1]
        return False 
  


    def newGame(self):
        self.arr = [[0 for i in range(3)]for j in range(3)]
        self.count = 0
    
    
    
if __name__ == "__main__":
    model = Model()
    while True:
        model.printField()
        row, col = map(int, input("Enter coords: ").split())
        if model.turn(row, col):
            if model.checkWinner():
                model.printField()
                print("You win!")
                break
            if model.count == 9:
                print("Draw")
                break
            c, z = model.comp_turn()
            print(c,z)
            model.printField()
            if model.checkWinner():
                print("Lose!")
                break

      