
import os
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="" #groq api key
)

class BaseAgent:
    def run(self, text):
        return "Base agent"

# 📄 Summarizer Agent
class SummarizerAgent(BaseAgent):
    def run(self, text):
        response = llm.invoke(f"Summarize the following document in short:\n{text}")
        return response.content

# 🧠 Insight Agent
class InsightAgent(BaseAgent):
    def run(self, text):
        response = llm.invoke(f"Extract key insights from the document:\n{text}")
        return response.content

# ⚠️ Risk Analyzer Agent
class RiskAgent(BaseAgent):
    def run(self, text):
        response = llm.invoke(f"Identify risks, issues, or problems in the document:\n{text}")
        return response.content

# 💡 Recommendation Agent
class RecommendationAgent(BaseAgent):
    def run(self, text):
        response = llm.invoke(f"Give recommendations and improvements:\n{text}")
        return response.content

# 🧑‍💻 Software Engineer Agent
class SoftwareEngineerAgent(BaseAgent):
    def run(self, text):
        response = llm.invoke(
            f"As a software engineer, analyze this and suggest technical improvements:\n{text}"
        )
        return response.content