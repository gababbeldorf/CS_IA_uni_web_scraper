# POINTS CALCULATOR
# Enter SL subjects and grades
class PointsCalculator:
    sl_in = input("Enter your SL subjects (separated by a ,): ")
    sl = sl_in.split(", ")
    sl_grades = []

    for s in sl:
        sl_ask_grade = int(input(f"Enter your grade for {s}: "))

        if sl_ask_grade <= 7:
            sl_grades.append(sl_ask_grade)

        elif sl_ask_grade > 7:
            print("Grade can't be greater than 7")
            sl_ask_grade = int(input(f"Enter your grade for {s}: "))
            sl_grades.append(sl_ask_grade)

        elif sl_ask_grade < 0:
            print("Grade can't be less than 7")
            sl_ask_grade = int(input(f"Enter your grade for {s}: "))
            sl_grades.append(sl_ask_grade)

    sl_total = sum(sl_grades)
    print(f"Your total SL points are: {sl_total}")

    print()

    # Enter HL subjects and grades
    hl_in = input("Enter your HL subjects (separated by a ,): ")
    hl = hl_in.split(", ")
    hl_grades = []

    for h in hl:
        hl_ask_grade = int(input(f"Enter your grade for {h}: "))

        if hl_ask_grade <= 7:
            hl_grades.append(hl_ask_grade)

        elif hl_ask_grade > 7:
            print("Grade can't be greater than 7")
            hl_ask_grade = int(input(f"Enter your grade for {h}: "))
            hl_grades.append(hl_ask_grade)

        elif hl_ask_grade < 0:
            print("Grade can't be less than 7")
            hl_ask_grade = int(input(f"Enter your grade for {h}: "))
            hl_grades.append(hl_ask_grade)

    hl_total = sum(hl_grades)
    print(f"Your total HL points are: {hl_total}")

    print()

    # Calculate total points
    total_pts = sl_total + hl_total
    print(f"Your total points are: {total_pts}")


certain = input("Do you know which STEM field you want to go in to (yes/no): ")

if certain == "yes":
    field = input("Which field would you like to go in to: ")
    if field == "science":
        open("physics.html")
    if field == "technology":
        open("cs.html")
    if field == "engineering":
        open("electric_eng.html")
    if field == "math":
        open("math.html")

    """if field = science --> physics top 20
        if field = technology --> cs top 20
        if field = engineering --> engineering top 20
        if field = math --> math top 20"""
if certain == "no":
    pass
    """Working with hands
        Standing
        Sitting
        """