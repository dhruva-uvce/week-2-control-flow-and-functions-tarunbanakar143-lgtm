# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
score=float(input("enter the score : "))
if(score<0 or score>100):
  print("Invalid Score ")
elif(score>=90 or score<=100):
  print("A")
elif(score>=80 or score<=89):
  print("B")
elif(score>=70 or score<=79):
  print("C")
elif(score>=60 or score<=69):
  print("D")
else:
  print("F")
