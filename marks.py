empty_list = []
print()

marks = [98,87,75,63,60]
print(marks)

print("=====MARKS-ANALYSIS=====")

print("Top 3 marks in exams this year were: ", marks[:3])

print("All the marks from lowest to highest: ", list(reversed(marks)))

i = 0
while i < len(marks):
    print(f"Index {i} has mark: {marks[i]}")
    i += 1

print("\nIndividual Marks: Eric: ", marks[0], "Alex: ", marks[1], "Sarah: ", marks[2], "Abdullah: ", marks[3], "Aayan: ", marks[4])

print("The Summary of the Marks:")
print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Average:", sum(marks) / len(marks))