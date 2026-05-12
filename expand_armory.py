import json
import os
import random

def expand_scenarios():
    scenarios = []
    
    # Professional Domains for the Digital Military Academy
    domains = {
        "Office Politics": [
            "A rival is subtly undermining your authority in group emails.",
            "The CEO favors a department that is less productive than yours.",
            "A sudden reorganization leaves your team without a clear mandate.",
            "Information is being withheld by a gatekeeper to stall your project."
        ],
        "Communication (Giao tiếp)": [
            "A high-stakes negotiation where the other party is using aggressive silence.",
            "Resolving a deep-seated misunderstanding with a long-term business partner.",
            "Persuading a skeptical board of directors to adopt a radical new strategy.",
            "Managing a public relations crisis where every word is being scrutinized."
        ],
        "Social Influence": [
            "Gaining the trust of a new neighborhood community after a dispute.",
            "Navigating complex family dynamics during a large inheritance discussion.",
            "Building a personal brand in a saturated digital market."
        ]
    }

    strategies = [
        "Ch. 3: Win without Fighting", 
        "Ch. 6: Avoid Strength, Strike Weakness", 
        "Ch. 13: Use of Spies (Networking)",
        "Ch. 11: Death Ground (Total Focus)"
    ]

    for i in range(1, 1001):
        domain_name = random.choice(list(domains.keys()))
        base_scenario = random.choice(domains[domain_name])
        
        scenarios.append({
            "id": f"STRAT-{i:04d}",
            "domain": domain_name,
            "context": f"{base_scenario} (Simulation Variation #{i})",
            "intel_report": f"Detected friction in {domain_name}. Terrain is unstable.",
            "sun_tzu_pillar": random.choice(strategies),
            "victory_condition": "Strategic repositioning resulting in zero-conflict resolution."
        })

    os.makedirs("data", exist_ok=True)
    with open("data/case_studies.json", "w", encoding="utf-8") as f:
        json.dump(scenarios, f, indent=4, ensure_ascii=False)

    print(f"--- [Success: 1,000 Detailed Intelligence Points Generated] ---")

if __name__ == "__main__":
    expand_scenarios()
