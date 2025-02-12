attendance = float(input("Enter attendance percentage: "))
min_marks = float(input("Enter minimum required marks: "))
marks_obtained = float(input("Enter marks obtained: "))

 if attendance_percentage >= 75 and student_marks >= min_marks_required:
        return "Eligible for the exam"
    else:
        return "Not eligible for the exam"