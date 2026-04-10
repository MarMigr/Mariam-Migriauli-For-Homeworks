import random
import time
from typing import List

class TherapeuticElements:
    
    def __init__(self):
        self.affirmations = [
            "I am worthy of love and respect",
            "My feelings are valid",
            "I am becoming stronger every day",
            "I trust in my ability to make positive changes",
            "I am enough, just as I am",
            "I am getting better and better every day",
            "I am grateful for everything I have in my life",
            "I am not defined by my past; I am driven by my future",
            "I use obstacles to motivate me to learn and grow",
            "Today will be a productive day",
            "Each and every day, I am getting closer to achieving my goals",
            "I am constantly growing and evolving into a better person",
            "Note to self: I am going to make you so proud",
            "Happiness is a choice, and today I choose to be happy"
        ]
        self.coping_strategies = [
            "Take a walk outside",
            "Practice deep breathing",
            "Listen to calming music",
            "Write in your journal",
            "Talk to a friend",
            "Do some stretching (jumping, jogging, muscle stretching)",
            "Look through old photographs",
            "Light a candle (better with a relaxing scent)",
            "Do something nice for someone else",
            "Put on an outfit you love",
            "Go to sleep",
            "Take a contrast shower",
            "Turn off your phone for 15 minutes to reduce digital overstimulation.",
            "Spend some time with pets",
            "Do a meditation session"
        ]

    def get_grounding_exercise(self) -> List[str]:
        return [
            "Name 5 things you can see 👁️",
            "Name 4 things you can touch 🖐️",
            "Name 3 things you can hear 👂",
            "Name 2 things you can smell 👃",
            "Name 1 thing you can taste 👅"
        ]        

    def breathing_exercise(self):
        while True:
            try:
                cycles = int(input("How many breathing cycles would you like to do? "))
                if cycles <= 0:
                    print("Please enter a positive integer for the number of cycles.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number for the cycles.")

        print("\nWelcome to the Guided Breathing Exercise!")
        print(f"We will do {cycles} breathing cycles. Follow the instructions below.\n")
        print("Get comfortable, sit upright, and let's begin...\n")
    
        inhale_time = 6
        hold_time = 5
        exhale_time = 6
    
        for i in range(1, cycles + 1):
            print(f"Cycle {i} of {cycles}")
        
            # Inhale
            print("🌬️  Inhale slowly...")
            for sec in range(inhale_time, 0, -1):
                print(f"Inhale: {sec} seconds remaining", end="\r")
                time.sleep(1)
        
            # Hold
            print("🛑 Hold your breath...")
            for sec in range(hold_time, 0, -1):
                print(f"Hold: {sec} seconds remaining", end="\r")
                time.sleep(1)
        
            # Exhale
            print("😮‍💨 Exhale slowly...")
            for sec in range(exhale_time, 0, -1):
                print(f"Exhale: {sec} seconds remaining", end="\r")
                time.sleep(1)
        
            if cycles > 1:
                print("\nGreat! Let's move to the next cycle.\n")
    
        print("🎉 You’ve completed the breathing exercise! Take a moment to enjoy the calmness.\n")

    def get_daily_affirmation(self) -> str:
        return random.choice(self.affirmations)

    def get_coping_strategy(self) -> str:
        return random.choice(self.coping_strategies)
    
    def get_breathing_exercise(self) -> str:
        return self.breathing_exercise

