from datetime import datetime
import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from role import Role

# Initialize a list to store character objects
if "roles" not in st.session_state:
    st.session_state.roles = []
if "fullname" not in st.session_state:
    st.session_state.fullname = None

# Function to add a new character

def add_role(role_title, experience, projects, tech_stacks):
    new_role = Role(
        role_title=role_title,
        experience=experience,
        projects=projects,
        tech_stacks=tech_stacks,
        last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    st.session_state.roles.append(new_role)
    return new_role

with st.sidebar:
    if st.session_state.fullname is None:
        st.session_state.fullname = st.text_input('input your name')
    else:
        st.title(f"{st.session_state.fullname}")

    openai_api_key = st.text_input("OpenAI API Key", key="openai_api_key", type="password")
    # Display a list of characters sorted by last talked date
        
    if st.button("Add a New Role"):
        st.session_state.show_form = True


if st.session_state.get("show_form", False):
    # Show a form to collect role details
    st.subheader("Add a New Role")
    
    role_title = st.text_input("Role Title")
    experience = st.text_area("Experience")
    projects = st.text_area("Projects")
    tech_stacks = st.text_input("Tech Stacks (e.g., Python, Django, React)")
    
    # Check if the user has filled in the required fields
    if st.button("Submit Role"):
        role = add_role(role_title, experience, projects, tech_stacks)
        st.session_state.show_form = False
        st.session_state.role_added = True

# if st.session_state.get("role_added", False):
#     # Reset the role_added state to refresh the sidebar
#     st.session_state.role_added = False
#     # Use this trick to refresh the sidebar
#     st.experimental_rerun()

# This will display the roles if they exist in the session state
if 'roles' in st.session_state:
    for role in st.session_state.roles:
        st.write(role.consolidated_info())
        

