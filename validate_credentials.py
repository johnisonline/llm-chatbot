import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]
#openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "What is Streamlit?"}
  ]
)


st.write(completion.choices[0].message.content)

st.write("below content is from snowflake")
# connect to snowflake and get data thru streamlit
# get data from snowflake
conn = st.experimental_connection("snowpark")
df = conn.query("SELECT  current_warehouse()")
st.write(df)
