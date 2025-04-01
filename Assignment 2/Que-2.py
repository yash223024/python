def student_info():
    student_number = input("Enter Student Number: ")
    student_name = input("Enter Student Name: ")
    marks = []

    for i in range(1, 5):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total_marks = sum(marks)
    average_marks = total_marks / 4

    print("\nStudent Information")
    print(f"Student Number: {student_number}")
    print(f"Student Name: {student_name}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")


if __name__ == "__main__":
    student_info()