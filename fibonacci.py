#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Validating and returning user input.
def validation():
  while True:
    num_of_terms = int(input("Enter a positive integer: "))
    if num_of_terms <=0:
      print("Error: Please enter a positive integer.")
    else:
      return num_of_terms

# Generating the Fibonacci sequence.
def generate_sequence(num):
  f_sequence = []
  a, b = 0, 1
  for _ in range(num):
    sequence.append(a)
    a = b
    b = a + b
  return f_sequence

# Printing the sequence.
def print_sequence(f_sequence)
  print("\n Fibonacci Sequence: ")
  for num in sequece:
    print(num, end = " ")

# Calling on each function to get input, generate the sequence, and print the sequence.
def main():
  num_of_terms = validation()
  f_sequence = generate_sequence(num_of_terms)
  print_sequence (f_sequence)

main()
