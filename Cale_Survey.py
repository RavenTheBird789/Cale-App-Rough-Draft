# Cale Survey Code
def Survey():
    # Question 1
    print("How often do you struggle to focus on a task?")
    print("1. Never")
    print("2. Sometimes")
    print("3. Often")
    print("4. Always")
    a1 = int(input("1, 2, 3, or 4?: "));
    # Question 2
    print("How often do you feel stressed out?")
    print("1. Never")
    print("2. Sometimes")
    print("3. Often")
    print("4. Always")
    a2 = int(input("1, 2, 3, or 4?: "));
    # Question 3
    print("How often do you feel sad or depressed?")
    print("1. Never")
    print("2. Sometimes")
    print("3. Often")
    print("4. Always")
    a3 = int(input("1, 2, 3, or 4?: "));
    # Analysis of answers
    total_score = a1 + a2 + a3
    if total_score <= 5:
        print("Your mental health seems to be in a good place! Keep up the great work taking care of yourself.");
    elif total_score > 5 and total_score <= 9:
        print("You may be experiencing some mild mental health challenges. Consider reaching out to a mental health professional for support.");
    elif total_score > 9 and total_score <= 12:
        print("It seems like you may be struggling with your mental health. We strongly recommend seeking help from a licensed mental health professional.");
