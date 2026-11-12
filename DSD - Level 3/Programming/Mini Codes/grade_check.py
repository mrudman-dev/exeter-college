grade_score = int(input("Enter your grade score (0-100): "))

if grade_score > 100 or grade_score <= -1:
    print("Invalid range, please enter again")
else:
    if grade_score >= 90:
        print("Grade: A*")
    elif grade_score >= 80:
        print("Grade: A")
    elif grade_score >= 70:
        print("Grade: B")
    elif grade_score >= 60:
        print("Grade: C")
    elif grade_score >= 50:
        print("Grade: D")
    elif grade_score >= 40:
        print("Grade: E")
    elif grade_score < 40:
        print("Grade: U")
