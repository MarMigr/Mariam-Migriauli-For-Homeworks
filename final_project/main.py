from file_handler import FileHandler
from mood_tracker import MoodTracker
from journal import Journal
from therapeutic import TherapeuticElements
import webbrowser
import random

class Therapp:
    def __init__(self):
        self.file_handler = FileHandler()
        self.mood_tracker = MoodTracker(self.file_handler)
        self.journal = Journal(self.file_handler)
        self.therapeutic = TherapeuticElements()

    def display_welcome(self):
        print("\n🌟 Welcome to TherApp 🧠  🌟")
        print("Your daily mental health companion 🌿\n")
        print(f"Today's affirmation ✨: \"{self.therapeutic.get_daily_affirmation()}\"")
        print("\n===========================\n")

    def main_menu(self):
        while True:
            print("\nWhat would you like to do? 💚")
            print("1. Track your Mood 😌")
            print("2. Write in Journal 📝")
            print("3. View Journal 📖")
            print("4. View Mood History 🎭")
            print("5. Get Self-Care Tip 🌸")
            print("6. Try Breathing Exercise 🫁")
            print("7. Try Grounding Exercise 🌱")
            print("8. Online Resources for meditation 🧘")
            print("9. Exit 🔚")

            choice = input("\nEnter your choice (1-9): ")

            match choice:
                case "1":
                    self.log_mood()
                case "2":
                    self.add_journal_entry()
                case "3":
                    self.view_journal()
                case "4":
                    self.display_mood_analysis()
                case "5":
                    self.display_coping_strategy()
                case "6":
                    self.display_breathing_exercise()
                case "7":
                    self.display_grounding_exercise()
                case "8":
                    self.display_meditation_resources() 
                case "9":
                    print("\nThank you for using TherApp. Take care! 🤗")
                    break
                case _:
                    print("\n❌ Please enter a valid option (1-9) ❌")



    def log_mood(self):
        print("\n=== Mood Tracker ===")
        print("Rate your mood from 1-5:")
        for score, desc in self.mood_tracker.mood_scale.items():
            print(f"{score}: {desc}")

        try:
            mood = int(input("\nYour mood: "))
            if mood in self.mood_tracker.mood_scale:
                notes = input("Any notes? (optional): ")
                self.mood_tracker.add_mood(mood, notes)
                print("\n✅ Mood logged successfully! ✅")
            else:
                print("\n❌ Please enter a number between 1 and 5 ❌")
        except ValueError:
            print("\n❌ Please enter a valid number ❌")

    def add_journal_entry(self):
        print("\n=== New Journal Entry ===")
        reflective_prompts = [
            "What is one thing that made you happy today?",
            "Describe a challenge you faced and how you handled it.",
            "What are you looking forward to tomorrow?",
            "Write about someone or something you are grateful for."
        ]
        print(f"Reflective prompt: {random.choice(reflective_prompts)}")

        content = input("Your thoughts: ")

        if content:
            self.journal.add_entry(content)
            print("\n✅ Journal entry saved! ✅")
        else:
            print("\n❌ Entry cannot be empty ❌")

    def view_journal(self):
        print("\n=== Recent Journal Entries ===")
        entries = self.journal.get_entries(limit=5) # 5 is just my choice, this can be removed, or changed and all journal entries will be printed

        if not entries:
            print("No journal entries yet")
            return

        for entry in entries:
            print(f"\n📅 Date: {entry['date']}")
            print(f"✍️  Entry: {entry['content']}")
            print("-" * 30)

    def display_mood_analysis(self):
        print("\n=== Mood Analysis ===")
        analysis = self.mood_tracker.display_mood_analysis()

        if "message" in analysis: #if we don't have data to analyze
            print(analysis["message"])
        else:
            print(f"\n 📊 Average mood: {analysis['average_mood']}/5")
            print(f"🕰 Total entries: {analysis['total_entries']}")
            print(f"🕑 Latest mood: {analysis['latest_mood']}")

    def display_coping_strategy(self):
        print("\n=== Self-Care Tip ===")
        print(f"💡 Try this: {self.therapeutic.get_coping_strategy()}")

    def display_breathing_exercise(self):
        print("\n=== Breathing Exercise ===")
        self.therapeutic.breathing_exercise()
        print("\n🎉 Great job completing the exercise! 🎉")
        
    def display_grounding_exercise(self):
        print("\n=== Grounding Exercise ===")
        grounding_exercises = self.therapeutic.get_grounding_exercise()
        for exercise in grounding_exercises:
            print(exercise) 
            input("\nPress Enter to go to the next step...") 
        print("\n🎉 Great job completing the exercise! 🎉") 


    def display_meditation_resources(self):
        print("\n=== Free Meditation Resources ===")
        resources = [
        "1.10-Minute Guided Meditation: https://www.youtube.com/watch?v=inpok4MKVLM",
        "2.Mindfulness for Beginners: https://www.youtube.com/watch?v=ZToicYcHIOU",
        "3.Relaxing Sounds and Visuals: https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "4.Deep Breathing Exercise Video: https://www.youtube.com/watch?v=7Ep5mKuRmAA"
        ]
    
        for resource in resources:
            title = resource.split(":")[0].strip()  # Extract title before the link
            print(f"✨ {title}")

        open_link = input("\nWould you like to open one of these links now? Enter the number (1-4) or 'n' to skip: ")
        if open_link in ['1', '2', '3', '4']:
            link = resources[int(open_link) - 1].split(': ')[1]
            webbrowser.open(link)
            print("\n🌟 Opening the resource in your browser! 🌟")
        else:
            print("\nNo link opened. You can explore these anytime! 🌿")


if __name__ == "__main__":
    app = Therapp()
    app.display_welcome()
    app.main_menu()
