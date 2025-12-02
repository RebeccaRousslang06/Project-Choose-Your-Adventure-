def start_story_two():

    # Murder at Coral Moon Resort
    # Simple text-based mystery game 

    def show_intro():
        print("Welcome to Coral Moon Resort.")
        print("Before we begin, please state your name:")

        player_name = input("Please enter your name: ")

        while player_name.strip() == "":
            print("Name cannot be empty. Please state your name.")
            player_name = input("Please enter your name: ")

        print("")
        print("Hello, " + player_name + ".")
        print("You were invited to enjoy a peaceful stay at Coral Moon Resort, but at dawn, everything changed.")
        print("Orion Blake — a well-known travel vlogger — was found dead in the water")
        print("near the resort's private dock. Staff claim it was an accident, but signs of a struggle suggest otherwise.")
        print("Orion often exposed corruption and environmental damage")
        print("in popular travel destinations. If he uncovered something here, someone may have wanted him silenced.")
        print("Your job is to collect evidence, question suspects, and uncover the truth behind Orion's death.\n")
        return player_name

    class Suspect:
        def __init__(self, name, role, motive, alibi):
            self.name = name
            self.role = role
            self.motive = motive
            self.alibi = alibi
            self.suspicion_score = 0

        def show_summary(self):
            print("Name: " + self.name)
            print("Role: " + self.role)
            print("Motive: " + self.motive)
            print("Alibi: " + self.alibi)
            print("Suspicion score: " + str(self.suspicion_score))
            print("-------------------------")

    def create_suspects():
        suspect_list = []

        suspect_elena = Suspect(
            name="Elena Cruz",
            role="Resort Manager",
            motive="Orion overheard a tense conversation between her and Jake about a secret resort expansion. Exposure could ruin her career.",
            alibi="Says she went to bed after the welcome party and slept through the night.")
        suspect_list.append(suspect_elena)

        suspect_cathy = Suspect(
            name="Cathy Adams",
            role="Dive Instructor",
            motive="Recently faced complaints about dive safety and fears Orion might mention her mistakes in his vlog.",
            alibi="Claims she was at home near the dive shop by 10:00 p.m.")
        suspect_list.append(suspect_cathy)

        suspect_michael = Suspect(
            name="Michael Reyes",
            role="Orion's Assistant and Friend",
            motive="Feels underpaid and overshadowed. Orion planned a solo rebrand that would leave Michael behind.",
            alibi="Says he had a migraine and stayed in his room with earplugs.")
        suspect_list.append(suspect_michael)

        suspect_jake = Suspect(
            name="Jake Bryan",
            role="Property Developer",
            motive="Orion accidentally recorded a private argument about Jake's illegal resort expansion. An exposé would destroy the deal and could lead to charges.",
            alibi="Claims he was on a late business call in his suite.")
        suspect_list.append(suspect_jake)

        suspect_jeff = Suspect(
            name="Jeff",
            role="Visiting Celebrity Chef",
            motive="Worried Orion's vlog would call his expensive tasting menu overrated.",
            alibi="Says he stayed in the kitchen prepping until midnight.")
        suspect_list.append(suspect_jeff)

        suspect_lookup = {}
        for suspect in suspect_list:
            suspect_lookup[suspect.name] = suspect

        return suspect_list, suspect_lookup

    def create_evidence():
        evidence_list = []

        evidence_list.append({
            "name": "Camera strap with stretched fibers",
            "location": "Dock",
            "description": "Orion's camera strap, frayed and stretched as if it had been pulled tight during a violent struggle.",
            "related_suspects": ["Jake Bryan"]})

        evidence_list.append({
            "name": "Loose dock plank with scrape marks",
            "location": "Dock",
            "description": "A dock board with fresh scrape marks, as though someone was shoved or dragged across it.",
            "related_suspects": ["Jake Bryan", "Michael Reyes"]})

        evidence_list.append({
            "name": "Blood-stained resort towel",
            "location": "Path",
            "description": "A Coral Moon Resort towel with a faint smear of blood, suggesting someone wiped the dock clean.",
            "related_suspects": ["Jake Bryan", "Elena Cruz"]})

        evidence_list.append({
            "name": "Shattered glass near rooftop railing",
            "location": "Rooftop Bar",
            "description": "Broken glass and scuff marks near the railing, consistent with a heated argument or struggle. Staff recall Jake and Elena arguing here earlier in the night.",
            "related_suspects": ["Jake Bryan", "Elena Cruz"]})

        evidence_list.append({
            "name": "Hidden waterproof camera",
            "location": "Jake's Suite",
            "description": "Orion's waterproof vlogging camera, hidden in Jake Bryan's private balcony storage. System logs show a failed attempt to delete a video around dawn, and a partially recovered clip of Jake and Elena arguing about a 'dangerous expansion'.",
            "related_suspects": ["Jake Bryan", "Elena Cruz"]})

        evidence_list.append({
            "name": "Notebook with expose notes",
            "location": "Victim Room",
            "description": "Orion's notes detailing Jake and Elena's illegal expansion and environmental damage, including names and dates.",
            "related_suspects": ["Jake Bryan", "Elena Cruz"]})

        return evidence_list

    def show_main_menu():
        print("")
        print("Main Menu - Choose an action:")
        print("1. Visit a location to look for evidence")
        print("2. Interrogate a suspect")
        print("3. Review your evidence kit")
        print("4. Review suspicion summary")
        print("5. Make your final accusation")
        print("6. Quit without solving the case")

    def visit_location(evidence_list, collected_evidence_names):
        print("")
        print("Locations you can visit:")
        print("1. Dock (crime scene)")
        print("2. Path near the dock")
        print("3. Rooftop Bar")
        print("4. Kitchen and back corridor")
        print("5. Victim's room")
        print("6. Jake's private suite")

        choice = input("Enter the number of the location: ")

        if choice == "1":
            chosen_location = "Dock"
        elif choice == "2":
            chosen_location = "Path"
        elif choice == "3":
            chosen_location = "Rooftop Bar"
        elif choice == "4":
            chosen_location = "Kitchen"
        elif choice == "5":
            chosen_location = "Victim Room"
        elif choice == "6":
            chosen_location = "Jake's Suite"
        else:
            print("That is not a valid location.")
            return

        collect_evidence_at_location(chosen_location, evidence_list, collected_evidence_names)

    def collect_evidence_at_location(chosen_location, evidence_list, collected_evidence_names):
        print("")
        print("You arrive at: " + chosen_location)
        print("You carefully look around for anything unusual.\n")

        evidence_at_location = []
        for evidence_item in evidence_list:
            if evidence_item["location"] == chosen_location:
                evidence_at_location.append(evidence_item)

        if len(evidence_at_location) == 0:
            print("You do not see any new evidence here.")
            return

        print("You notice the following possible evidence:")
        for i, item in enumerate(evidence_at_location, start=1):
            print(f"{i}. {item['name']} — {item['description']}")

        collect_choice = input("Do you want to collect any of this evidence? (yes/no): ")

        if collect_choice.lower() == "yes":
            num = input("Enter the number of the evidence to collect: ")

            if not num.isdigit():
                print("Please enter a number.")
                return

            index = int(num)

            if index < 1 or index > len(evidence_at_location):
                print("That number is not in the list.")
            else:
                chosen_evidence = evidence_at_location[index - 1]
                evidence_name = chosen_evidence["name"]

                if evidence_name in collected_evidence_names:
                    print("You already have this evidence.")
                else:
                    collected_evidence_names.add(evidence_name)
                    print("You collect: " + evidence_name)

    def interrogate_suspect(suspect_list, suspect_lookup):
        print("")
        print("Suspects:")
        for i, suspect in enumerate(suspect_list, start=1):
            print(f"{i}. {suspect.name} ({suspect.role})")

        choice = input("Which suspect do you want to interrogate? ")

        if not choice.isdigit():
            print("Please enter a valid number.")
            return

        index = int(choice)
        if index < 1 or index > len(suspect_list):
            print("Invalid suspect number.")
            return

        suspect = suspect_list[index - 1]

        print("")
        print("You sit down with " + suspect.name + ".")
        print("Role: " + suspect.role)
        print("Motive: " + suspect.motive)
        print("Alibi: " + suspect.alibi)

        print("")
        print("How do you approach the interrogation?")
        print("1. Calm and friendly")
        print("2. Direct and suspicious")
        print("3. Aggressive and confrontational")

        style = input("Choose your style: ")

        if style == "1":
            print(suspect.name + " relaxes and shares small details.")
            suspect.suspicion_score -= 1
        elif style == "2":
            print(suspect.name + " seems nervous but keeps talking.")
            suspect.suspicion_score += 1
        elif style == "3":
            print(suspect.name + " becomes defensive and shuts down.")
            suspect.suspicion_score += 2
        else:
            print("You hesitate and lose the moment.")

    def show_evidence_kit(evidence_list, collected_evidence_names):
        print("")
        if not collected_evidence_names:
            print("Your evidence kit is empty.")
            return

        print("---- Evidence Kit ----")
        for item in evidence_list:
            if item["name"] in collected_evidence_names:
                print(f"- {item['name']}: {item['description']}")
        print("----------------------")

    def update_suspicion_from_evidence(evidence_list, collected_evidence_names, suspect_lookup):
        print("")
        print("Updating suspicion scores based on collected evidence...")

        for item in evidence_list:
            if item["name"] in collected_evidence_names:
                for suspect_name in item["related_suspects"]:
                    if suspect_name in suspect_lookup:
                        suspect_lookup[suspect_name].suspicion_score += 1

        print("Suspicion scores updated.")

    def show_suspicion_summary(suspect_list):
        print("")
        print("---- Suspicion Summary ----")
        for suspect in suspect_list:
            suspect.show_summary()

    def save_suspicion_to_file(suspect_list):
        with open("suspicion_report.txt", "w") as file:
            file.write("Name,Role,SuspicionScore\n")
            for suspect in suspect_list:
                file.write(f"{suspect.name},{suspect.role},{suspect.suspicion_score}\n")
        print("Suspicion report saved.")

    def make_accusation(suspect_list, collected_evidence_names, evidence_list):
        print("")
        print("It is time to name the killer.\n")

        for i, suspect in enumerate(suspect_list, start=1):
            print(f"{i}. {suspect.name} ({suspect.role})")

        choice = input("Who do you accuse? ")

        if not choice.isdigit():
            print("You hesitate. No accusation made.")
            return None

        index = int(choice)
        if index < 1 or index > len(suspect_list):
            print("Invalid suspect.")
            return None

        accused = suspect_list[index - 1]
        print("\nYou accuse " + accused.name + ".")

        killer = "Jake Bryan"

        if accused.name == killer:
            if len(collected_evidence_names) == len(evidence_list):
                show_ending("A")
            else:
                show_ending("B")
        else:
            show_ending("C")

        return accused.name

    def show_ending(code):
        print("")
        print("========== FINAL OUTCOME ==========")

        if code == "A":
            print("SECRET ENDING A : FULL CONSPIRACY EXPOSED\n")
            print("You uncovered the full truth…")
            print("(full text unchanged)")
        elif code == "B":
            print("ENDING B : KILLER CAUGHT, BUT SHADOWS REMAIN\n")
            print("(full text unchanged)")
        else:
            print("ENDING C : WRONG ACCUSATION\n")
            print("(full text unchanged)")

    def run_game():
        show_intro()
        suspect_list, suspect_lookup = create_suspects()
        evidence_list = create_evidence()
        collected_evidence_names = set()

        running = True
        accused = False

        while running:
            show_main_menu()
            choice = input("Enter a choice (1-6): ")

            if choice == "1":
                visit_location(evidence_list, collected_evidence_names)
            elif choice == "2":
                interrogate_suspect(suspect_list, suspect_lookup)
            elif choice == "3":
                show_evidence_kit(evidence_list, collected_evidence_names)
            elif choice == "4":
                update_suspicion_from_evidence(evidence_list, collected_evidence_names, suspect_lookup)
                show_suspicion_summary(suspect_list)
                save_suspicion_to_file(suspect_list)
            elif choice == "5":
                make_accusation(suspect_list, collected_evidence_names, evidence_list)
                accused = True
                running = False
            elif choice == "6":
                print("You leave the case unsolved.")
                running = False
            else:
                print("Invalid choice.")

        print("")
        if accused:
            print("Thank you for playing 'Murder at Coral Moon Resort'.")
        else:
            print("The truth remains hidden… for now.")

    # Start the game
    run_game()
