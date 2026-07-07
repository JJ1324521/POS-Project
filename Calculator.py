class calculator:
    def __init__(self):
        self.result = 0
    
    #This is for addition
    def add(self, value):
        self.result += value
        return self.result

    #This is for subtraction
    def substract(self, value):
        self.result -= value
        return  self.result

    #This is for multiplication
    def multiply(self, value):
        self.result *= value
        return self.result

    #This is for division
    def divide(self, value):
        self.result /= value
        return self.result

    #This is for Clearing the value
    def clear(self):
        self.result = 0
        return self.result

    #This is the main program
    def run(self):
        print("Welcome to the Calculator! Type 'exit' to quit.")
        self.result = float(input("Enter starting number: "))

        #Start of while loop
        while True:
            operator = input("Enter operator (+, -, *, /) or 'exit' or 'clear': ")
            
            #Check for exit
            if operator == "exit":
                print("Final result:", self.result)
                break
            
            #Check for clearing
            if operator == "clear":
                self.clear()
                self.result = float(input("Enter starting number: "))
                continue

            #Capture number input
            try:
                value = float(input("Enter next number: "))
            except ValueError:
                print("Invalid number, try again.")
                continue

            #Do operations
            if operator == "+":
                print("Result:", self.add(value))
            elif operator == "-":
                print("Result:", self.subtract(value))
            elif operator == "*":
                print("Result:", self.multiply(value))
            elif operator == "/":
                print("Result:", self.divide(value))
            else:
                print("Invalid operator, try again.")

calc = calculator()
calc.run()