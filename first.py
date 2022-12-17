from utils import Utils

class ListMulp:
    
    def __init__(self) -> None:
        
        entered: list[int] = []
        out: list[int] = []
        
        self.entered = entered
        self.out = out
        
    # Get input for the entered list 
    def getinput(self) -> None:
        
        foo: int = 0
        bar: int = 0
        foo = int(input(f"{Utils.message(1)}"))
        print(f"{Utils.message(2)}")
        for i in range(0,foo):
            bar = int(input())
            self.entered.append(bar)
    
    # Make out list
    def makeoutlist(self):
        
        j: int = len(self.entered) - 1
        i: int = 0
        
        while True:
            self.out.append(self.entered[j] * self.entered[i])
            j -= 1
            i += 1
            if i > j:
                break
    
    def takeoutlist(self) -> list[int]:
        return self.out
    

def main() -> int:
    
    mulp: object = ListMulp()
    print(f"{Utils.message(0)}")
    while True:
        mulp.getinput()
        mulp.makeoutlist()
        print(mulp.takeoutlist())
        if Utils.terminate():
            break
    return 0


if __name__ == "__main__":
    main()
