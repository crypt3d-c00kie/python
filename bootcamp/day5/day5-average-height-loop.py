#day5
#finding average of heights
#using loops

student_heights = input("Input a list of student heights : ").split()

for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

print(f"Number of people : {len(student_heights)}")
print(student_heights)
#now printing the sum of the heights of all students
height_sum = 0
tallest = 0
idx = 0
for n in range(0,len(student_heights)):
    height_sum+=student_heights[n]
    if  student_heights[n] > tallest:
        idx = n
        tallest = student_heights[n]

print(f"The tallest of them all : {tallest} at position {idx+1} ")
print(f"The sum of their height : {height_sum}")
print(f"Average height : {round(height_sum/len(student_heights))}")