# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
# Q08. Sum of Digits (while loop)

n = int(input("Enter a number: "))

temp = n
digit_sum = 0

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    temp = temp // 10

print(f"Sum of digits of {n} = {digit_sum}")
