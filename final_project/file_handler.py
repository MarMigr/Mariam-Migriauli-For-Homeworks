import json
from pathlib import Path
from typing import Dict

class FileHandler:
    def __init__(self, base_path: str = "mindfulme_data"):
        # Initialize the base path and set up file paths for the different data files
        self.base_path = Path(base_path)
        self.files = {
            "mood_tracker": self.base_path / "mood_tracker.json",
            "journal": self.base_path / "journal.json"
            }
        # Initialize the files with default structures if they do not exist
        self._initialize_files()

    def _initialize_files(self):
        # Create the base directory if it doesn't exist
        self.base_path.mkdir(exist_ok=True)
        
        # Define the default structures for the files
        default_structures = {
            "mood_tracker": {"moods": []},
            "journal": {"entries": []}
        }

        # Loop through each file and check if it exists, if not, create it with default data
        for name, path in self.files.items():
            if not path.exists():
                self.write_file(name, default_structures[name])

    def read_file(self, file_name: str) -> Dict:
        file_path = self.files[file_name]  # Get the file path based on the file name
        with open(file_path, 'r') as f:
            return json.load(f) 
        
    def write_file(self, file_name: str, data: Dict):
        file_path = self.files[file_name] 
        with open(file_path, 'w') as f: 
            json.dump(data, f, indent=4)
