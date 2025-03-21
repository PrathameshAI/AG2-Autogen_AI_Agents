# Group chat amongst agents to create a 4th grade lesson plan
# Flow determined by Group Chat Manager automatically, and
# should be Teacher > Planner > Reviewer > Teacher (repeats if necessary)

# 1. Import our agent and group chat classes
from autogen import ConversableAgent, GroupChat, GroupChatManager, LLMConfig

# Define our LLM configuration for OpenAI's GPT-4o mini
# uses the OPENAI_API_KEY environment variable
llm_config = LLMConfig(api_type="openai", model="gpt-4o-mini")

with llm_config:
    # Planner agent setup
    planner_message = "Create lesson plans for 4th grade. Use format: <title>, <learning_objectives>, <script>"
    planner = ConversableAgent(
        name="planner_agent",
        system_message=planner_message,
        description="Creates lesson plans"
    )

    # Reviewer agent setup
    reviewer_message = "Review lesson plans against 4th grade curriculum. Provide max 3 changes."
    reviewer = ConversableAgent(
        name="reviewer_agent",
        system_message=reviewer_message,
        description="Reviews lesson plans"
    )

    # Teacher agent setup
    teacher_message = "Choose topics and work with planner and reviewer. Say DONE! when finished."
    teacher = ConversableAgent(
        name="teacher_agent",
        system_message=teacher_message,
    )

# Setup group chat
groupchat = GroupChat(
    agents=[teacher, planner, reviewer],
    speaker_selection_method="auto",
    messages=[]
)

# Create manager
# At each turn, the manager will check if the message contains DONE! and end the chat if so
# Otherwise, it will select the next appropriate agent using its LLM
manager = GroupChatManager(
    name="group_manager",
    groupchat=groupchat,
    llm_config=llm_config,
    is_termination_msg=lambda x: "DONE!" in (x.get("content", "") or "").upper()
)

# Start the conversation
chat_result = teacher.initiate_chat(
    recipient=manager,
    message="Let's teach the kids about the solar system."
)

# Print the chat
print(chat_result.chat_history)