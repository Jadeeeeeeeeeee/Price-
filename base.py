#Functions go here 
def instructions():
   
  instruction = input("Would you like to view the instructions: ").lower()

  if instruction == "yes" or instructions == "y":
    print("instructions")

  elif instruction == "no" or instruction == "n":
    pass

  else:
    print("Please answer yes or no")

#Main routine go here:
instructions()