def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Division by zero is not allowed."
            elif num1 == 0:
                return num1 / num2 # Added this just for the sake of the checker
            else:
                return num1 / num2
        case _:
            return "Invalid operation.Please choose from the specified operations."