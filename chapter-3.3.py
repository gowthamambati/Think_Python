def print_border():
   print "+", "- " * 4, "+"

def print_row():
   row = "|", " " * 8, "|\n"
   print row * 4

def block():
   print_border()
   print_row()
   
block()
