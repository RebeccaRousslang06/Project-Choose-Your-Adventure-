def start_story_one():
    class CrewMember:
        def __init__(self, _name, _role, _knowledge):
            self.name = _name
            self.role = _role
            self.knowledge = _knowledge
        
        #returns what each crew member knows about the crime 
        def release_knowledge(self):
            return f'{self.name} knows: {self.knowledge}'

        #returns a response based on the type of question
        def question(self, interrogate_type):
            if interrogate_type == 'alibi':
                return f"{self.name} says: 'I don't know. I was back in my sector double checking my work when the alarm rang.'"
            elif interrogate_type == "logs":
                if 'log' in self.knowledge:
                    return f'{self.name} says: {self.knowledge}'
                else: 
                    return f"{self.name} says: 'I don't know about the logs.'"
            elif interrogate_type == "argument":
                if 'argue' in self.knowledge or 'argument' in self.knowledge:
                    return f"{self.name} says: '{self.knowledge}'"
                else:
                    return f"{self.name} says: 'I didn't hear any arguments.'"
            else:
                return f"{self.name} is too scared to look you in the eye."
    
    #initializes the crew
    jacob = CrewMember("Jacob", "Captain", "He knows the protocol and the procedures")
    sophia = CrewMember("Sophia", "Engineer", "She overheard Rebecca and Julie having an argument about the logs")
    evan = CrewMember("Evan", "Technician", "He overlooked the system logs and saw Julie's name in them multiple times")
    julie = CrewMember("Julie", "Researcher", "She accepts the truth that Rebecca found out her data was wrong")
    rebecca = CrewMember("Rebecca", "Biologist", "She found out Julie's data was incorrect")
    crew = [jacob, rebecca, julie, evan, sophia] #stores crew in a list

    #dictionary that tracks each member's status and location
    crew_status = {
        "Jacob": "In his quarters",
        "Sophia": "Checking engineering systems",
        "Julie": "In the lab",
        "Evan": "Looking over the logs",
        "Rebecca" : "In the oxygen sector"
    }

    #starts the game, prints the introduction and shows a choice to the player on what to investigate
    def start():
        questioned = set()
        print("Murder On the Starline Odyssey")
        print("You are a medic aboard the spaceship Starline Odyssey, orbiting Mars.")
        print("Your crew: Jacob, Sophia, Evan, Rebecca, and Julie") 
        print("After a year in space, you've become a family. But tonight, something terrible happens.")
        input("Press Enter to continue")
        print("An alarm suddenly blares! Oxygen levels are dropping fast from Rebecca's sector!")
        print("Jacob yells over the intercom: 'Everyone, stay calm!'")
        
        #player choice 
        print("\nDo you:")
        print("1. Go to the airlock to investigate.")
        print("2. Stay behind and check the system logs.")
        choice1 = input("Enter 1 or 2:")
        if choice1 == "1":
            airlock_scene(questioned)
        else: 
            logs_scene(questioned)

    #player looks at the airlock
    def airlock_scene(questioned):
        print()
        print("You float toward the airlock. Red lights flash everywhere.")
        print("Rebecca is there, motionless. Her suit regulator is cut.")
        print("Jacob locks down the ship and orders everyone to stay in their rooms.")
        print("Someone on this ship is a murderer.")
        print()

        #updates Rebecca's status from the event 
        crew_status["Rebecca"] = "Found at the airlock, deceased"

        #prints out to the player the current status of the crew members
        print("\nCrew Status: ")
        for name, status in crew_status.items():
            print(f"{name}: {status}")
        
        investigate(questioned)
        accuse(questioned)

    #player checks the logs
    def logs_scene(questioned):
        print()
        print("You pull up the system logs on the main console.")
        print("There are three strange edits to the oxygen system, all under Julie's name...")
        print("Before you can ask, Jacob locks down the ship.")
        print("Someone on this ship is a murderer.")
        print()
        investigate(questioned)
        accuse(questioned)

    #player questions the crewmates 
    def investigate(questioned):
        while True:
            print("Hours have passed as the Odyssey drifts silently. You decide to question the others.")
            print()
            print("Who do you talk to first?")
            print("1. Julie")
            print("2. Evan")
            print("3. Sophia")
            print("4. No more questions and accuse someone")
            choice2 = input("Enter 1, 2, 3 or 4: ")

            if choice2 == "1":
                print("\nJulie is shaking. What should you ask her?")
                print("1. Ask about the logs")
                print("2. Ask about where she was when the emergency rang.")
                second_choice = input("Enter 1 or 2: ")
            
                if second_choice == "1":
                    interrogate_type = "logs"
                else: 
                    interrogate_type = "alibi"
            
                print("\n"+ julie.question(interrogate_type))
                questioned.add("Julie")
                print("Already questioned:", questioned)
    
            elif choice2 == "2":
                print("\nEvan is reviewing the logs. What should you ask him?")
                print("1. Ask about Julie.")
                print("2. Ask about where he was when the alarm rang.")
                second_choice = input("Enter 1 or 2: ")

                if second_choice == "1":
                    interrogate_type = "logs"
                else:
                    interrogate_type = "alibi"
            
                print("\n" + evan.question(interrogate_type))
                questioned.add("Evan") #add Evan to the question set
                print("Already questioned:", questioned)

            elif choice2 == "3":
                print("\nSophia looks afraid. What should you ask her?")
                print("1. Ask about the argument she overheard.")
                print("2. Ask about what has been going on in the crew lately.")
                second_choice = input("Enter 1 or 2: ")

                if second_choice == "1":
                    interrogate_type = "argument"
                else: 
                    interrogate_type = "alibi"
            
                print("\n" + sophia.question(interrogate_type))
                questioned.add("Sophia")
                print("Already questioned:", questioned)
            
            elif choice2 == "4":
                print("\nIt's time to accuse someone.")
                return 
            else: 
                print("Invalid choice.")

    #player is allowed a chance to accuse the murderer
    def accuse(questioned):
        print("All members gather in the control room")
        print("The captain, Jacob, looks at you and says, We need to know who killed Rebecca")

        print()
        print("Information Gathered.")
        for member in crew:
            if member.name in questioned:
                print(member.release_knowledge())
        print()

        print("Who are you accusing?")
        print("1. Sophia")
        print("2. Julie")
        print("3. Evan")
        print()
        guilty = input("Enter 1, 2, 3: ")

        if guilty == "2":
            correct_ending()
        else: 
            wrong_ending()

    #if the player guesses correctly
    def correct_ending():
        print()
        print("Julie panics and says, I didn't mean for this to happen")
        print("My data was wrong and I didn't want her to tell everyone. I only meant to scare her!")
        print()
        print("Report: Rebecca deceased")
        print("Cause: Oxygen sabotage")
        print("Culprit: Julie")
        print("The stars didn't mourn. They simply kept burning — distant, cold, eternal.")
        print("End: Justice was served.")

    #wrong ending for the player
    def wrong_ending():
        print()
        print("Jacob looks at you and says 'Are you sure?'")
        print("That night, the alarms are blaring you look around")
        print("The oxygen levels dropped and you realized that you accused the wrong person")
        print()
        print("End: Lost in Space.")

    #start the story once
    start()

