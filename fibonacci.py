#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Validating and returning user input.
def validation():
  while True:
    try:
      num_of_terms = int(input("Enter a positive integer: "))
      if num_of_terms <=0:
        print("Error: Please enter a positive integer.")
      else:
        return num_of_terms
    except ValueError:
            print("Error: Invalid input. Please enter an integer.")


# Generating the Fibonacci sequence.
def generate_sequence(num):
  f_sequence = []
  a, b = 0, 1
  for _ in range(num):
    f_sequence.append(a)
    a, b = b, a + b
  return f_sequence

# Printing the sequence.
def print_sequence(f_sequence):
  print("\nFibonacci Sequence: ")
  for num in f_sequence:
    print(num, end = " ")
  print()

# Calling on each function to get input, generate the sequence, and print the sequence.
def main():
  num_of_terms = validation()
  f_sequence = generate_sequence(num_of_terms)
  print_sequence (f_sequence)
  
main()
