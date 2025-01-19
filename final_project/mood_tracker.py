from datetime import datetime

class MoodTracker:
    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.mood_scale = {
            1: "Very Low 😔",
            2: "Low 😕",
            3: "Neutral 😐",
            4: "Good 😊",
            5: "Excellent 🥳"
        }

    def add_mood(self, mood_score: int, notes: str = ""):
        data = self.file_handler.read_file("mood_tracker")
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), #converting time 
            "mood": mood_score, # Get the score from mood entry 
            "mood_text": self.mood_scale[mood_score], # Get the text corresponding to the mood score from the mood_scale (e.g., Very low, low, etc.).
            "notes": notes
        }
        data["moods"].append(entry)
        self.file_handler.write_file("mood_tracker", data)

    def display_mood_analysis(self):
        analysis = self.get_mood_analysis()
        if not analysis:
            return {"message": "No mood data available to analyze."}
        return analysis

    def get_mood_analysis(self):
        data = self.file_handler.read_file("mood_tracker")
        if not data["moods"]:
            return None
        
        moods = [entry["mood"] for entry in data["moods"]]
        average_mood = sum(moods) / len(moods)
        latest_mood = data["moods"][-1]["mood_text"] # Retrieves the "mood_text" from the most recent mood entry in the "moods" list

        total_entries = len(moods)

        return {
            "average_mood": round(average_mood, 2),
            "latest_mood": latest_mood,
            "total_entries": total_entries
        }

