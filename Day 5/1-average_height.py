string = input("Enter all the student heights")
student_heights = string.split(", ")
count=0
sum=0
for height in student_heights:
    sum=sum+int(height)
    count=count+1
average = round(sum/count,0)
print(int(average))