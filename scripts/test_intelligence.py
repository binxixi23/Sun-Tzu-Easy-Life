import json
import os

def test_intelligence(query):
    """
    Simulates the Scout Agent's ability to retrieve specific intelligence 
    from the 1,000 situational data points in data/case_studies.json.
    """
    file_path = 'data/case_studies.json'
    
    if not os.path.exists(file_path):
        return "❌ Error: Armory is empty. Please run 'expand_armory.py' first."

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    query_words = set(query.lower().split())
    best_match = None
    max_score = -1

    # Search Algorithm: Scoring based on keyword overlap
    for entry in data:
        score = 0
        context_words = set(entry['context'].lower().split())
        domain_words = set(entry['domain'].lower().split())
        
        # Overlap with context is weighted higher (Intelligence)
        score += len(query_words.intersection(context_words)) * 3
        score += len(query_words.intersection(domain_words))

        if score > max_score:
            max_score = score
            best_match = entry

    if best_match and max_score > 0:
        return {
            "Status": "✅ Match Found",
            "Target_ID": best_match['id'],
            "Detected_Scenario": best_match['context'],
            "Strategic_Pillar": best_match['sun_tzu_pillar'],
            "Victory_Condition": best_match['victory_condition']
        }
    
    return "🌫️ The fog of war is too thick. No strategic match found."

if __name__ == "__main__":
    # TEST CASE: Office Politics / Communication
    test_query = "A rival is undermining me in group emails"
    result = test_intelligence(test_query)
    print(json.dumps(result, indent=4, ensure_ascii=False))
