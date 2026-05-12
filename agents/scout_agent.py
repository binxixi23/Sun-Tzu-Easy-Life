import re

class ScoutAgent:
    """The Intelligence Officer: Analyzes the 'Terrain' and 'Weather' of the user's problem."""
    
    def __init__(self):
        self.domains = {
            "financial": ["money", "wealth", "investment", "debt", "gold"],
            "social": ["politics", "influence", "neighbors", "status", "reputation"],
            "internal": ["health", "stress", "sleep", "mindset", "spirit"],
            "relational": ["love", "family", "kids", "elders", "ancestors"]
        }

    def conduct_reconnaissance(self, user_input):
        """Scans the query for keywords to determine which folder to pull from."""
        found_domain = "general_human_affairs"
        urgency = "normal"
        
        # Check for Urgency (The 'Climate')
        if any(x in user_input.lower() for x in ["urgent", "emergency", "immediately", "asap"]):
            urgency = "storm_weather"
            
        # Determine Domain (The 'Terrain')
        for domain, keywords in self.domains.items():
            if any(key in user_input.lower() for key in keywords):
                found_domain = domain
                break
                
        return {"domain": found_domain, "urgency": urgency, "intel": user_input}
