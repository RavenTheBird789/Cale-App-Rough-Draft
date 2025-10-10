# Cale App Code
import Cale_Survey
import Cale_DSM_Encyclopedia

def options(): # Options for user to choose from
    print("Alright, here are some resources that we offer: [(1)DSM-Encyclopedia, (2)Breathing Exercises, (3)Cale-AI, (4)Custom-Alarms, (5)Calendars, (6)Chatrooms, (7)Survey, (8)Appearance]");
    choice1 = int(input("Type the number corresponding to the choice listed above to use it: "));
    if choice1 == 1:
        Cale_DSM_Encyclopedia.encyclopedia(); # Calls the encyclopedia function from Cale_DSM_Encyclopedia.py
    elif choice1 == 2:
        print("Breathing Exercises coming soon!"); # Placeholder for future feature
    elif choice1 == 3:
        print("Cale-AI coming soon!"); # Placeholder for future feature
    elif choice1 == 4:
        print("Custom-Alarms coming soon!"); # Placeholder for future feature
    elif choice1 == 5:
        print("Calendars coming soon!"); # Placeholder for future feature
    elif choice1 == 6:
        print("Chatrooms coming soon!"); # Placeholder for future feature
    elif choice1 == 7:
        Cale_Survey.Survey(); # Calls the Survey function from Cale_Survey.py
    elif choice1 == 8:
        appearance = input("Would you like to change the appearance of the app? (y/n): "); # Appearance customization feature
        if appearance == "y":
            appearance_choice = input("What color scheme would you like? (dark/light/custom): ");
            if appearance_choice == "dark":
                print("Dark mode activated!"); # Dark mode feature
            elif appearance_choice == "light":
                print("Light mode activated!"); # Light mode feature
            elif appearance_choice == "custom":
                custom_color = input("Please enter the hex code of your desired color scheme: ");
                print(f"Custom color scheme {custom_color} activated!"); # Custom color scheme feature
            else:
                print("Invalid input. Please restart the app"); # Invalid input handling

initial = input("Hello, welcome to Cale. An app dedicated to mental health betterment and education to many people worldwide. Would you like to take a simple questionaire made by licensed mental health professionals so we can get a general idea of the overall state of your mental health? (y/n): "); # Introduction to app for user
if initial == "y":
    Cale_Survey.Survey();
    print("Thank you for taking the time to complete this survey!"); # Survey completion message
elif initial == "n":
    print("That's completely fine. Remember, if you ever change your mind you can take the survey again at any time."); # Message for users who decline the survey
    options();
else:
    print("Invalid input. Please restart the app"); # Invalid input handling