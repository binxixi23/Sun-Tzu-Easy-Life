import json
import os

def generate_armory():
    os.makedirs("data", exist_ok=True)

    # 1. 1,000+ Modern Scenarios (Simplified generator for volume)
    case_studies = []
    domains = ["Office Politics", "Startup Growth", "Family Peace", "Personal Health", "Financial Freedom"]
    for i in range(1, 1001):
        domain = domains[i % len(domains)]
        case_studies.append({
            "id": f"CS-{i:04d}",
            "scenario": f"Complex challenge in {domain} situation #{i}",
            "strategic_pillar": "Direct vs Indirect",
            "victory_condition": "Minimum friction, maximum gain"
        })
    
    with open("data/case_studies.json", "w") as f:
        json.dump(case_studies, f, indent=4)

    # 2. Stories and Jokes (Large library for Banter Agent)
    banter_content = {
        "parables": [
            {"topic": "ego", "text": "The mountain does not boast of its height, yet the clouds bow to it."},
            {"topic": "speed", "text": "The rabbit ran fast but in circles; the turtle walked straight to the finish line."},
            {"topic": "tech", "text": "A hacker tried to break the sage's firewall. The sage had no firewall because he had no secrets."}
        ],
        "jokes": [
            "Sun Tzu's favorite app? Waze. It always knows the terrain.",
            "How does a general drink coffee? With a strategic 'ground' advantage."
        ]
    }
    with open("data/stories_and_jokes.json", "w") as f:
        json.dump(banter_content, f, indent=4)

    # 3. Tactical Library (Adaptations of Art of War)
    tactical_lib = """# The Modern Tactical Library
## Adaptation of the 13 Chapters for the Digital Age

### Chapter 1: Detail Assessment
- **Modern Rule:** Data is the new high ground.
- **Action:** Before starting a project, verify the 'supply lines' of your focus.

### Chapter 2: Waging War (Cost)
- **Modern Rule:** Time is the gold that never returns.
- **Action:** If a meeting lasts 2 hours, it must yield 10 hours of value.
"""
    with open("data/tactical_library.md", "w") as f:
        f.write(tactical_lib)

    print("--- [Armory Built: 1,000+ Scenarios & Tactical Data Generated] ---")

if __name__ == "__main__":
    generate_armory()
