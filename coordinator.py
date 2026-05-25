from agents import (
    SummarizerAgent,
    InsightAgent,
    RiskAgent,
    RecommendationAgent,
    SoftwareEngineerAgent
)

class Coordinator:
    def __init__(self):
        self.agents = {
            "📄 Summary Agent": SummarizerAgent(),
            "🧠 Insight Agent": InsightAgent(),
            "⚠️ Risk Analyzer Agent": RiskAgent(),
            "💡 Recommendation Agent": RecommendationAgent(),
            "🧑‍💻 Software Engineer Agent": SoftwareEngineerAgent()
        }

    def run_all(self, text):
        results = {}

        for name, agent in self.agents.items():
            try:
                results[name] = agent.run(text)
            except Exception as e:
                results[name] = f"Error: {str(e)}"

        return results