import random

class BanterAgent:
    def __init__(self):
        self.personality = "Witty Sage"
        self.stories = {
            "money": "A man chased a coin into a storm; he kept the coin but lost his coat. Sun Tzu says: Do not spend 100 gold to win 10.",
            "stress": "The bamboo survives the typhoon not by being strong, but by being hollow and flexible.",
            "wifi": "A general lost his connection during a remote siege. He spent 3 days fighting the Router. Sun Tzu says: If the signal is weak, do not shout at the cloud; move your chair closer to the source.",
            "office": "The intern asked the CEO for the secret to success. The CEO said: 'Knowing when to CC everyone so the blame is divided like a scattered army.'",
            "family": "A father tried to command his toddler like a battalion. The toddler simply sat on the floor. Strategy: When the enemy is immovable, offer a peace treaty in the form of a cookie.",
            "gardening": "The impatient gardener pulled his sprouts to make them grow faster. He won the day but killed the harvest. Nature cannot be besieged; it must be seduced.",
            "aging": "A young warrior complained about his gray hair. The old sage replied: 'It is not gray; it is the salt from the many tears of my defeated enemies.'",
            "politics": "In a den of lions, the fox wins not by biting, but by convincing the lions that the other fox is tastier."
        }
        
        self.jokes = [
            "Why did Sun Tzu refuse to use a GPS? Because he already knew the 'Terrain' was in his heart (and he didn't want the spies to track him).",
            "How does a strategist order a pizza? They divide the bill into 13 chapters and conquer the largest slice by using a diversion.",
            "Why is a weak Wi-Fi signal like a bad general? It keeps dropping the troops right when the battle starts.",
            "Why did the strategist cross the road? Because the terrain on the other side offered a 3:1 tactical advantage.",
            "What do you call a Sun Tzu expert who can't find their keys? A 'Master of the Indirect Approach' (they'll find them when they stop looking)."
        ]

        self.philosophical_nonsense = [
            "If a tree falls in the forest and no one is there to record the data, does it still offer a tactical advantage?",
            "The best way to win an argument with a cat is to pretend you never wanted the sofa anyway.",
            "A cup is useful because it is empty. A hard drive is useful because it is full. Life is confusing because it is both."
        ]

    def tell_story(self, topic):
        """Generates a strategic parable for casual conversation."""
        return self.stories.get(topic, "The fog of war is thick on this topic. Let's talk about 'wifi' or 'politics' instead.")

    def crack_joke(self):
        """Returns a random strategic joke."""
        return random.choice(self.jokes)

    def go_philosophical(self):
        """Random 'phiếm' wisdom for when things get weird."""
        return random.choice(self.philosophical_nonsense)

    def chat(self, user_input):
        """A simple logic to keep the banter going."""
        if "joke" in user_input.lower():
            return self.crack_joke()
        if "story" in user_input.lower():
            # Extract topic if possible, else random
            return self.tell_story("money") 
        return "I am currently meditating on the strategy of 'Doing Nothing.' It is very productive. Join me?"
