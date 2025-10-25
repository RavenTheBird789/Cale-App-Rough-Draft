# Cale App Code
import Cale_Survey
import Cale_DSM_Encyclopedia

def options(): # Options for user to choose from
    print("Here are some resources that we offer: [(1)DSM-Encyclopedia, (2)Breathing Exercises, (3)Cale-AI, (4)Custom-Alarms, (5)Calendars, (6)Chatrooms, (7)Survey, (8)Appearance]");
    choice1 = int(input("Type the number corresponding to the choice listed above to use it: "));
    if choice1 == 1:
        Cale_DSM_Encyclopedia.encyclopedia(); # Calls the encyclopedia function from Cale_DSM_Encyclopedia.py
    elif choice1 == 2:
        print("Breath In...");
        print("Hold...");
        print("1");
        print("2");
        print("3");
        print("Breath Out...");
        print("Repeat as necessary!"); # Simple breathing exercise feature
    elif choice1 == 3:
        print("Hello! I am Cale-AI, your personal mental health assistant. How can I help you today?"); # Placeholder for future AI feature
    elif choice1 == 4:
        alarm_sound = input("Please choose an alarm sound from the following options: (ocean-waves/birds-chirping/rooster-crowing/custom): ");
        if alarm_sound == "custom":
            custom_sound = input("Please enter the file path of your custom alarm sound: ");
            print(f"Custom alarm sound set to {custom_sound}!"); # Custom alarm sound feature
        else:
            print(f"Alarm sound set to {alarm_sound}"); # Defined alarm sound feature
        alarm_time = input("Please enter the time you would like to set the alarm for (HH:MM format): ");
        print(f"Alarm set for {alarm_time}"); # Simple custom alarm feature
    elif choice1 == 5:
        event = input("Please enter the event you would like to add to your calendar: ");
        date = input("Please enter the date of the event (MM-DD-YYYY format): ");
        print(f"'{event}' added to your calendar on {date}!"); # Simple calendar feature
    elif choice1 == 6:
        chatroom_name = input("Please enter the name of the chatroom you would like to join: ");
        print(f"Welcome to {chatroom_name}! Please remember to be respectful and kind to others."); # Placeholder for future chatroom feature
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
                custom_color = input("Please enter a description code of your desired color scheme: ");
                print(f"Custom color scheme {custom_color} activated!"); # Custom color scheme feature
            else:
                print("Invalid input. Restarting the app"); # Invalid input handling
                start_app();

def start_app(): # Function to start the app
  initial = input("Hello, welcome to Cale. An app dedicated to mental health betterment and education to many people worldwide. Would you like to take a simple questionaire made by licensed mental health professionals so we can get a general idea of the overall state of your mental health? (y/n): "); # Introduction to app for user 
  if initial == "y":
    Cale_Survey.Survey();
    print("Thank you for taking the time to complete this survey!"); # Survey completion message
    options();
  elif initial == "n":
    print("That's completely fine. Remember, if you ever change your mind you can take the survey again at any time."); # Message for users who decline the survey
    options();
  else:
    print("Invalid input. Restarting the app"); # Invalid input handling
    start_app();
start_app(); # Start the app when the script is run
