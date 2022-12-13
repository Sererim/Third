
class Utils:
    
    @staticmethod
    def message(num: int) -> str:
        
        words: list[str] =[
            "Program is running",
            "Enter the size of a list.",
            "Enter numbers.",
            "Enter a number.",
            "Do you want to treminate a program Y/y ?."
        ]
        
        return words[num]