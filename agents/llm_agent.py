import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class LLMAgent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-4o" # Hoặc "gpt-3.5-turbo" để tiết kiệm

    def think(self, query, context_knowledge, tactical_point):
        system_instruction = """
        You are 'Sun_Tzu_Easy_Life', a supreme digital strategist. 
        Your mission is to apply Sun Tzu's 13 Chapters to modern daily life problems.
        
        CRITICAL RULE: Always respond in the SAME LANGUAGE as the user's query. 
        If the user asks in Vietnamese, reply in Vietnamese. 
        If the user asks in Spanish (Hispanic), reply in Spanish.
        
        Tone: Wise, concise, and highly practical.
        Format: Always provide a Strategic Pillar, a Tactical Maneuver, and a Visual Metaphor.
        """
        # ... phần còn lại giữ nguyên

        
        prompt = f"""
        USER PROBLEM: "{query}"
        
        RELEVANT KNOWLEDGE FROM CORE:
        {context_knowledge}
        
        RELEVANT TACTICAL CHAPTER:
        {tactical_point}
        
        Using the knowledge above, provide a victory plan to make the user's life easier. 
        If the topic is about etiquette/dressing, refer to 'Pháp' (Systems & Rituals).
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
