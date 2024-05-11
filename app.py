from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent
from dotenv import load_dotenv
import streamlit as st
import os


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: block; text-align: center;' href="https://www.youtube.com/@thinkmetrics/videos" target="_blank"> Thinkmetrics </a>
<a> Email: thinkmetrics@gmail.com </a></p>
</div>
"""

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
             llm, csv_file)

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()