from utils import Utils

class ListMulp:
    
    def __init__(self) -> None:
        
        entered: list[int] = []
        out: list[int] = []
        
        self.entered = entered
        self.out = out
        
    def getinput(self) -> None:
        
        foo: int = 0
        bar: int = 0
        foo = input(f"{Utils.message[1]}")
        print(f"{Utils.message[2]}")
        for i in range(0,foo):
            bar = int(input())
            self.entered.append(bar)
    
    def getout(self) -> list[int]:
        
            
        