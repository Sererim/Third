from utils import Utils
from decimal import Decimal as decimal, getcontext as gtc

class Homework:
    
    def __init__(self) -> None:
        
        gtc().prec = 2
        initial_list: list[decimal] = []
        new_list: list[decimal] = []
        answer: decimal = decimal('0.0')
        
        self.initial = initial_list
        self.final = new_list
        self.answer = answer
        
    def get_list(self) -> None:
        size: int = 0
        foo: decimal = '0.0'
        size = int(input(f"{Utils.message(1)}"))
        
        print(f"{Utils.message(2)}")
        for i in range(0,size):
            foo = decimal(input())
            self.initial.append(foo)
            
    def fraction_list(self) -> None:
        for i in range(len(self.initial)):
            self.initial[i] = (decimal(self.initial[i] - int(self.initial[i])))
    
    def search(self) -> None:
        
        foo: decimal = decimal('0.0')
        bar: int = 0
        baz: int = 0
        size: int = len(self.initial)
        
        for i in range(0, size):
            foo = self.initial.pop(i)
            for j in range(0, size - 1):
                if foo < self.initial[j]:
                    bar += 1
                elif foo > self.initial[j]:
                    baz += 1
            if bar == size - 1:
                self.final.append(foo)
            elif baz == size - 1:
                self.final.append(foo)
            bar, baz = 0, 0
            self.initial.append(foo)
    
    def get_answer(self) -> None:
        self.answer = self.final[0] - self.final[1]
        if self.answer < 0:
            self.answer *= -1
    
def main() -> int:
    while True:
        number: object = Homework()
        number.get_list()
        number.fraction_list()
        number.search()
        number.get_answer()
        print(f"{number.answer}")
        if Utils.terminate():
            break
    return 0


if __name__ == "__main__":
    main()        
            