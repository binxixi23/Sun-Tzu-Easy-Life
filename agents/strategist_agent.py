import random

class StrategistAgent:
    """The General: Formulates the 'Victory Plan' using the 13 Pillars of Sun Tzu."""
    
    def __init__(self):
        self.strategies = [
            "Win Without Fighting (Subdue the enemy through preparation)",
            "Dĩ Dật Đãi Lao (Wait for the enemy to tire themselves out)",
            "Bất Động Như Sơn (Remain unmoved until the opportunity is perfect)",
            "Adapt Like Water (Find the path of least resistance)"
        ]

    def formulate_plan(self, scout_report):
        """Combines Domain knowledge with Binh Phap logic."""
        domain = scout_report['domain']
        
        # Core Strategic Logic
        chosen_strategy = random.choice(self.strategies) # In RAG, this would be a DB lookup
        
        advice = {
            "assessment": f"In the theater of {domain}, the terrain is currently complex.",
            "core_directive": chosen_strategy,
            "maneuver": "Position your resources in the hollows where the opponent is weakest.",
            "warning": "Do not commit forces to a siege you cannot win."
        }
        return advice
