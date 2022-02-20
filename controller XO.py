from model import *
from view import *

def s1(row, col):
    #print(col, row)

    if model.turn(row, col):
        view.draw_X(row,col)
        print(model.count)
        print(model.arr)
        if model.checkWinner():
            view.sign("WINNER")
            model.newGame()
            return         
       
    if model.count == 9:
        view.sign("DRAW")
        model.newGame()
        return       
  
    row, col = model.comp_turn()
    view.draw_O(row, col)
    print(model.count)
    print(model.arr) 
    if model.checkWinner():
        view.sign("LOSER")
        model.newGame()
        return
         

view = View(s1)
model = Model()
view.newGame(0,0)
model.newGame()
view.run()