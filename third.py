# From decimal to binary
# 45 -> 00101101
from utils import Utils


class DecToBinary():
    
    @staticmethod
    def convert(decimal_number: int) -> list[int]:
        binary: list[int] = []
        for i in range(8):
            if decimal_number % 2 == 1:
                decimal_number -= 1
                decimal_number /= 2
                binary.append(1)
            else:
                decimal_number /= 2
                binary.append(0)
        binary.reverse()
        return binary
    
    
def main() -> int:
    
    toconvert: int = 0
    print(f"{Utils.message(0)}\n"
          "Program converts to 8-bit binary number.\n"
          "From 0 to 255")
    
    while True:
        toconvert = int(input(f"{Utils.message(3)}"))
        print(DecToBinary.convert(toconvert))
        
        if Utils.terminate():
            break
    
    return 0
            
            
if __name__ == "__main__":
    main()    
