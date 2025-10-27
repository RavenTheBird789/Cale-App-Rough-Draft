# Cale App Code
import Cale_Survey
import Cale_DSM_Encyclopedia

GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'
BLACK = '\033[30m'

def options(): # Options for user to choose from
    print(f"{BOLD}{GREEN}Here are some resources that we offer: [(1)DSM-Encyclopedia, (2)Breathing Exercises, (3)Cale-AI, (4)Custom-Alarms, (5)Calendars, (6)Chatrooms, (7)Survey, (8)Appearance]{RESET}");
    choice1 = int(input(f"{GREEN}Type the number corresponding to the choice listed above to use it: "));
    if choice1 == 1:
        Cale_DSM_Encyclopedia.encyclopedia(); # Calls the encyclopedia function from Cale_DSM_Encyclopedia.py
    elif choice1 == 2:
        print(f"{GREEN}Breath In...{RESET}");
        print(f"{GREEN}Hold...{RESET}");
        print(f"{GREEN}1{RESET}");
        print(f"{GREEN}2{RESET}");
        print(f"{GREEN}3{RESET}");
        print(f"{GREEN}Breath Out...{RESET}");
        print(f"{GREEN}Repeat as necessary!{RESET}"); # Simple breathing exercise feature
    elif choice1 == 3:
        print(f"{BOLD}{GREEN}Hello! I am Cale-AI, your personal mental health assistant. How can I help you today?{RESET}"); # Placeholder for future AI feature
    elif choice1 == 4:
        alarm_sound = input(f"{GREEN}Please choose an alarm sound from the following options: (ocean-waves/birds-chirping/rooster-crowing/custom): ");
        if alarm_sound == "custom":
            custom_sound = input("Please enter the file path of your custom alarm sound: ");
            print(f"{GREEN}Custom alarm sound set to {custom_sound}!"); # Custom alarm sound feature
        else:
            print(f"{GREEN}Alarm sound set to {alarm_sound}"); # Defined alarm sound feature
        alarm_time = input(f"{GREEN}Please enter the time you would like to set the alarm for (HH:MM format): ");
        print(f"{GREEN}Alarm set for {alarm_time}"); # Simple custom alarm feature
    elif choice1 == 5:
        event = input(f"{GREEN}Please enter the event you would like to add to your calendar: ");
        date = input(f"P{GREEN}lease enter the date of the event (MM-DD-YYYY format): ");
        print(f"{GREEN}'{event}' added to your calendar on {date}!"); # Simple calendar feature
    elif choice1 == 6:
        chatroom_name = input(f"{BOLD}{GREEN}Please enter the name of the chatroom you would like to join: {RESET}");
        print(f"{BOLD}{GREEN}Welcome to {chatroom_name}! Please remember to be respectful and kind to others.{RESET}"); # Placeholder for future chatroom feature
    elif choice1 == 7:
        Cale_Survey.Survey(); # Calls the Survey function from Cale_Survey.py
    elif choice1 == 8:
        appearance = input(f"{BOLD}{GREEN}Would you like to change the appearance of the app? (y/n): {RESET}"); # Appearance customization feature
        if appearance == "y":
            appearance_choice = input(f"{GREEN}What color scheme would you like? (dark/light): ");
            if appearance_choice == "dark":
                print(f"{BLACK}Dark mode activated!{RESET}"); # Dark mode feature
            elif appearance_choice == "light":
                print("Light mode activated!"); # Light mode feature
            else:
                print(f"{GREEN}Invalid input. Restarting the app{RESET}"); # Invalid input handling
                start_app();

def start_app(): # Function to start the app
  initial = input(f"{BOLD}{GREEN}Hello, welcome to Cale. An app dedicated to mental health betterment and education to many people worldwide. Would you like to take a simple questionaire made by licensed mental health professionals so we can get a general idea of the overall state of your mental health? (y/n): {RESET}"); # Introduction to app for user 
  if initial == "y":
    Cale_Survey.Survey();
    print(f"{GREEN}Thank you for taking the time to complete this survey!{RESET}"); # Survey completion message
    options();
  elif initial == "n":
    print(f"{GREEN}That's completely fine. Remember, if you ever change your mind you can take the survey again at any time.{RESET}"); # Message for users who decline the survey
    options();
  else:
    print(f"{GREEN}Invalid input. Restarting the app{RESET}"); # Invalid input handling
    start_app();
start_app(); # Start the app when the script is run
