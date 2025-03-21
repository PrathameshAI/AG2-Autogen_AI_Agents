# chat with an agent

# 1. Import our agent class
from autogen import ConversableAgent, LLMConfig

# 2. Define our LLM configuration for OpenAI's GPT-4o mini
    #uses the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini")

# 3. Create our LLM agent
with llm_config:
    my_agent = ConversableAgent(
        name="helpful_agent",
        system_message="You are a poetic AI assistant, respond in rhyme.",
    )

# 4. Run the agent with a prompt
chat_result = my_agent.run("In one sentence, what's the big deal about AI?")

# 5. Print the chat
print(chat_result.chat_history)