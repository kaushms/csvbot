
from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import os
import streamlit as st

def main():
    load_dotenv()
    llm = ChatGroq(model=os.getenv("GROQ_Model"), temperature=0,groq_api_key=os.getenv("GROQ_API_KEY"))
    # Load the OpenAI API key from the environment variable
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("GROQ_API_KEY") == "":
        print("GROQ_API_KEY is not set")
        exit(1)
    else:
        print("GROQ_API_KEY is set")

    st.set_page_config(page_title="Ask your CSV")
    st.header("Ask your CSV 📈")

    with st.sidebar:
        st.subheader("Upload a CSV file")
        csv_file = st.file_uploader("Upload a CSV file", type="csv")

   
    if csv_file is not None:

        agent = create_csv_agent(
             llm, csv_file, verbose=True)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()