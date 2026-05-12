class VisualizerAgent:
    """The Signal Officer: Converts strategy into visual charts and diagrams."""
    
    def generate_mermaid(self, plan):
        """Creates a Mermaid.js flowchart code block."""
        mermaid_code = f"""
graph TD
    A[Problem Identified] --> B{{Analyze Terrain: {plan['assessment'][:15]}...}}
    B --> C[Strategy: {plan['core_directive'][:20]}...]
    C --> D[Result: Easy Victory]
    style D fill:#f9f,stroke:#333,stroke-width:4px
        """
        return f"```mermaid\n{mermaid_code}\n```"

    def provide_metaphor(self):
        return "Visualizing the 'Flow of Water' against the 'Solid Rock' of the obstacle."
