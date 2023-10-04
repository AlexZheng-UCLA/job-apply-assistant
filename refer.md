from datetime import datetime
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from role import Role


if role:
    st.title(f"Chat with {role.get_bot_name()}")
    st.session_state.messages = role.get_chat_history()
    if "history" not in st.session_state:
        st.session_state.history = ConversationBufferMemory(human_prefix=role.get_human_name(), ai_prefix=role.get_bot_name())

    # Create a button to clear chat history
    def clear_chat_history():
        st.session_state.messages = []
        role.save_chat_history([])
    if st.button("Clear Chat History"):
        clear_chat_history()
        
    # Create a PromptTemplate with input variables
    template = f"""
    [Character Settings]{bot.consolidated_info()}

    Current conversation:
    {{history}}
    {bot.human_name}: {{input}}
    {bot.bot_name}:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template,
    )

    # Create LLM & Conversation Chain
    if openai_api_key:
        # Create LLM model
        llm = OpenAI(temperature=0.3, openai_api_key=openai_api_key)

        # Create the ConversationChain object with the specified configuration
        conversation = ConversationChain(
            prompt=prompt,
            llm=llm,
            memory=st.session_state['history']
        )
        
        # Load previous chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
            
        # Print user input and LLM reply
        if user_input := st.chat_input():
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            response = conversation.predict(input=user_input)
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        # Save messages in the characters
        role.save_chat_history(st.session_state.messages)
        print(role.chat_history)
    else:
        st.warning('OpenAI API key required to test this app.')