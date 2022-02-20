from turtle import *

setup(430, 430)
width(8)
speed(0)
ht()

class View:
    def __init__(self,arg):
        self.arg= arg
    
    
    def draw_X(self, row, col):
        color("DarkMagenta")
        x = -140 + col*140
        y = 140 - 140*row        
        up()
        goto(x-40, y+40)
        down()
        goto(x+40, y-40)
        up()
        goto(x+40, y+40)
        down()
        goto(x-40, y-40)

    
    def draw_O(self, row, col):
        color("black")
        x = -140 + col*140
        y = 140 - 140*row           
        seth(0)
        up()
        goto(x,y-50)
        down()
        circle(50)    
    
        
    def drawField( self ):
        bgcolor("CornflowerBlue")
        color("black")
        for i in range(2):
            up()
            goto(-70 + 140*i,200)
            down()
            goto(-70 +140*i, -200)
        
        for j in range(0,-2,-1):
            up()
            goto(-200, 70 + 140*j)
            down()
            goto(200 , 70 + 140*j)    
    
    
    def sign(self, text):
        up()
        goto(0,0)
        down()
        color("DarkSlateGray1")
        write(text, move=False, align="center", font=("Arial", 30, "bold"))  
        onscreenclick(self.newGame) 
      
        
    def newGame(self, x, y):
        clear()
        self.drawField()
        onscreenclick(self.clickAnalizer)  
    
    
    def clickAnalizer(self,x,y): #X, O, None
        row = 2 - int((y+210)//140)
        col = int((x+210)//140)

        self.arg(row, col)
        
        
    
        
                
    def run(self):
        done()
    
    
if __name__ == "__main__":
    def foo(row, col):
        print(row, col)
    view = View(foo)
    view.newGame()
    view.drawField()
    view.draw_X(1,1)
    view.draw_O(1,2)
    view.run()