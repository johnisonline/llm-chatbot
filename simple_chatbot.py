import openai
import streamlit as st

st.title(" Aisi")
st.subheader("A chatbot that can answer your questions about your Snowflake")

#Initialize the chat messages history
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", 
                                  "content": "Hi, I'm Aisi, a chatbot that can answer your questions about this strategic platform. How can I help you today?"}]

#Prompt for user input and save
if prompt := st.chat_input():
    st.session_state.messages.append({"role":"user", "content":prompt})

#display the prior chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

#Send the chat messages to OpenAI and save the response
if st.session_state.messages[-1]["role"] != "assistant":
    #call LLM
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            r = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            )
            response = r.choices[0].message.content
            st.write(response)

    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
