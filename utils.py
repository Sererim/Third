
class Utils:
    
    @staticmethod
    def message(num: int) -> str:
        
        words: list[str] =[
            "Program is running.\n",
            "Enter the size of a list.\n",
            "Enter numbers.\n",
            "Enter a number.\n",
            "Do you want to treminate the program Y/y ?.\n"
        ]
        
        return words[num] 
    
    @staticmethod
    def terminate() -> bool:
        
        control: str = "NULL"
        while True:
            control = input(Utils.message(4))
            if control == "Y" or control == 'y':
                return True
            else:
                return False
    