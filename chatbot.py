import streamlit as st

st.set_page_config(page_title="Chatbot", page_icon="🤖")

st.title("🤖 Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

def get_bot_response(user_input):
    text = user_input.lower()  # normalize to lowercase

    if "hi" in text or "hello" in text:
        return "Hello! 👋 How can I help you today?"
    elif "i need your help" in text:
        return "Yes I am always ready to help!!!"
    elif "statistics"in text:
        return "Statistics is a branch of mathematics which is used in data analysis,machine learning,etc."
    elif "ai" in text:
        return "AI stands for Artificial Intelligence. It enables machines to mimic human intelligence."
    elif "data science" in text:
        return "Data Science is about analyzing data and extracting meaningful insights."
    elif "array" in text:
        return "An array is a collection of elements stored at contiguous memory locations."
    elif "python" in text:
        return "Python is a versatile programming language popular for AI, ML, and web apps."
    elif "bye" in text:
        return "Goodbye! 👋 Have a great day!"
    else:
        return f"I didn’t quite understand: **'{user_input}'** 🤔. Could you try asking in another way?"

# Chat input
user_input = st.text_input("Ask me something:")

if user_input:
    st.session_state["messages"].append(("You", user_input))
    bot_reply = get_bot_response(user_input)
    st.session_state["messages"].append(("Bot", bot_reply))

# Display conversation
st.write("### Chat History")
for sender, msg in st.session_state["messages"]:
    if sender == "You":
        st.markdown(f"**👤 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
