import os
import json
from pydantic import BaseModel
from autogen import ConversableAgent, LLMConfig

#chat with an agent but it provies the output in a structured JSON format
# Define Lesson Plan Structure
class LearningObjective(BaseModel):
    title: str
    description: str

class LessonPlan(BaseModel):
    title: str
    learning_objectives: list[LearningObjective]
    script: str

# LLM Configuration for Lesson Agent
llm_config = LLMConfig(
    api_type="openai",
    model="gpt-4o-mini",
    api_key=os.environ["OPENAI_API_KEY"],
    response_format=LessonPlan,
)

# Lesson Agent
lesson_agent = ConversableAgent(
    name="lesson_agent",
    llm_config=llm_config,
    system_message="You are a classroom lesson agent. Given a topic, write a lesson plan for a fourth-grade class."
)

# Example Interaction
chat_result = lesson_agent.run("Create a lesson plan on the water cycle.")

# Get and print the lesson plan
lesson_plan_json = json.loads(chat_result.chat_history[-1]["content"])
print(json.dumps(lesson_plan_json, indent=2))
