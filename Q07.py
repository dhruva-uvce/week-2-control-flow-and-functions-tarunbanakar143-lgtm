# Q07. Reverse a Number (while loop)
#
# Ask the user for a positive integer.
# Print the reverse of the number using a while loop.
#
# Sample Input 1:   Enter a number: 1234
# Sample Output 1:  Reversed: 4321
#
# Sample Input 2:   Enter a number: 5000
# Sample Output 2:  Reversed: 5

# --- YOUR CODE HERE ---
# Q07. Reverse a Number (while loop)

n = int(input("Enter a number: "))

reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reversed:", reverse)
