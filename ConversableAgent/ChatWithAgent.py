import os
from autogen import ConversableAgent, LLMConfig

# LLM Configuration for Helpful Agent
llm_config = LLMConfig(
    api_type="openai",
    model="gpt-4o-mini",
    api_key=os.environ["OPENAI_API_KEY"],
)

# Helpful Agent
helpful_agent = ConversableAgent(
    name="helpful_agent",
    llm_config=llm_config,
    system_message="You are a poetic AI assistant",
)

# Example Interaction
response = helpful_agent.run("Write a short poem about the ocean.")
print(response)
