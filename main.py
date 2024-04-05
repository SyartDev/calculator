from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

end = False
while not end:
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  timeline = input("Type 'y' continue calculating, or type 'n' to exit.: ").lower()
  if timeline == "y":
    print("Restarting now for you")
  else:
      end = True
