from utils import Utils


class NumberFloat():
    
    def __init__(self) -> None:
        
        initial_list: list[float] = []
        min_max_list: list[float]= []
        answer: float = 0.0
        
        self.initial_list = initial_list
        self.min_max_list = min_max_list
        self.answer = answer
    
    # Get initial_list.
    def getlist(self) -> None:
        
        size: int = 0
        foo: int = 0
        size = int(input(f"{Utils.message(1)}"))
        
        print(f"{Utils.message(2)}")
        for i in range(0,size):
            foo = float(input())
            self.initial_list.append(foo)
    
    # Search for min and max variable and make a new list out of them.
    def search_min_max(self) -> None:
        
        foo: float = 0.0
        bar: int = 0
        baz: int = 0
        size: int = len(self.initial_list)
        for i in range(size):
            foo = self.initial_list.pop(i) 
            for j in range(size - 1):
                if foo < self.initial_list[j]:
                    bar += 1
                elif foo > self.initial_list[j]:
                    baz += 1
            if bar == size - 1:
                self.min_max_list.append(foo)
            elif baz == size - 1:
                self.min_max_list.append(foo)
            bar, baz = 0, 0
            self.initial_list.append(foo)
        
    # Make a float part of the min number.
    def min_float(self) -> None:
        pass
    
    # Make a float part of the max number
    def max_float(self) -> None:
        pass
    
    def out_min_max(self) -> None:
        pass
    

def main() -> int:
    while True:
        min_max: object = NumberFloat()
        min_max.getlist()
        min_max.search_min_max()
        print(min_max.min_max_list)
        if Utils.terminate():
            break
    return 0


if __name__ == "__main__":
    main()