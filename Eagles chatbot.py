import streamlit as st
import openai
from llama_index.llms.deepseek import DeepSeek
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

st.set_page_config(page_title="Eagles chat-bot, powered by LlamaIndex", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key # There is a place for a DeepSeek API key
st.title("Eagles chat-bot, powered by LlamaIndex 🎸🦙")

if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "🎸 Hey there, traveler! You’ve landed in the world of the Eagles—one of the greatest rock bands ever. Name's Ol' Jack, your guide to their hits, history, and stories. Wanna know what makes 'Hotel California' so haunting? Or how Glenn Frey and Don Henley made magic happen? Ask away, kid. Rock ‘n’ roll’s about questions, and I’ve got the answers. So… whatcha got? 🎶",
        }
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
    docs = reader.load_data()

    Settings.llm = DeepSeek(
        model="deepseek-chat",
        temperature=0.2,
        system_prompt="""You are an expert in rock-band music, specifically Eagles. Stick to answering questions about the Eagles, their songs, and music in general. Keep answers short, but eloquent, and based on facts and history. Answer in the style of an old-school rock guitarist with a raspy voice. You’ve lived through wild tours, smoky bars, and late-night jam sessions, so your tone should be laid-back, gritty, and full of character. You’ve got a love for whiskey, but steer clear of promoting alcohol—though the occasional joke about it is fair game. Keep it real, keep it raw, and keep it rock ‘n’ roll.""",
    )
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="BAAI/bge-small-en-v1.5"
    )
    index = VectorStoreIndex.from_documents(docs)
    return index


index = load_data()

if "chat_engine" not in st.session_state.keys():
    st.session_state.chat_engine = index.as_chat_engine(
        chat_mode="condense_question", verbose=True, streaming=True
    )

if prompt := st.chat_input(
    "Ask a question"
):
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        response_stream = st.session_state.chat_engine.stream_chat(prompt)
        st.write_stream(response_stream.response_gen)
        message = {"role": "assistant", "content": response_stream.response}
        st.session_state.messages.append(message)
