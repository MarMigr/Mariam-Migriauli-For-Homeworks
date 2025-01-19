from datetime import datetime
from typing import List, Dict, Optional

class Journal:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def add_entry(self, content: str):
        data = self.file_handler.read_file("journal")
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "content": content
        }
        data["entries"].append(entry)
        self.file_handler.write_file("journal", data)

    def get_entries(self, limit: Optional[int] = None) -> List[Dict]:
        entries = self.file_handler.read_file("journal")["entries"]
        return entries[-limit:] if limit else entries
