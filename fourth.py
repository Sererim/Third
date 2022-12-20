# Fibonacci numbers with a negative part
from utils import Utils


class Fibbonacci():
    
    def __init__(self, num: int) -> None:
        
        half_sequence: list[int] = [0, 1]
        full_sequence: list[int] = []
        
        self.half_sequence = half_sequence
        self.full_sequence = full_sequence
        self.num = num
    
    def get_sequence(self) -> None:
        foo: int = 0
        
        for i in range(self.num + 1):
            if i == 0 or i == 1:
                pass
            else:
                foo = self.half_sequence[i - 1] + self.half_sequence[i - 2]
                self.half_sequence.append(foo)
            
    def get_full_sequence(self) -> None:
        self.half_sequence.reverse()
        self.full_sequence = self.half_sequence[:]
        self.half_sequence.reverse()
        size: int = len(self.full_sequence)
        for i in range(size):
            self.full_sequence[i] *= -1
        for i in range(size):
            if self.half_sequence[i] == 0:
                pass
            else:
                self.full_sequence.append(self.half_sequence[i])


def main() -> int:
    
    foo: int = 0
    
    print(f"{Utils.message(0)}")
    while True:
        foo = int(input(f"{Utils.message(3)}"))
        if Utils.ispositive(foo):
            fib = Fibbonacci(foo)
            fib.get_sequence()
            fib.get_full_sequence()
            print(fib.full_sequence)
            if Utils.terminate():
                break
        else:
            Utils.message(5)
    return 0


if __name__ == "__main__":
    main()