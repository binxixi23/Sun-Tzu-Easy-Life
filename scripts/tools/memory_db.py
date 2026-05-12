import json
import os

class StrategyMemory:
    def __init__(self, file_path="data/battle_history.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f: json.dump([], f)

    def record_victory(self, query, strategy, outcome="Pending"):
        """Records a strategic decision to avoid repeating mistakes."""
        with open(self.file_path, 'r+') as f:
            history = json.load(f)
            history.append({"query": query, "strategy": strategy, "outcome": outcome})
            f.seek(0)
            json.dump(history, f, indent=4)

    def recall_experience(self, query):
        """Finds if a similar 'Battle' was fought before."""
        with open(self.file_path, 'r') as f:
            history = json.load(f)
            # Simple keyword matching for memory
            for past in history:
                if any(word in query.lower() for word in past['query'].lower().split()):
                    return past
        return None
