# Chatbot as a tool for humanities research

***Introduction***

The collaboration of artificial intelligence and humanities researchers has opened new perspectives for the Digital Humanities and Humanities in general (it seems that sooner or later all humanities will inevitably become digital by some percentage).

Recently, chatbots have caught everyone's attention in the field of AI. They are powerful tools which provide information retrieval, textual analysis, and user engagement. As conversational agents, chatbots can assist researchers in navigating vast amounts of information, helping to find fruitful insights, making materials more accessible. Moreover, chatbots can play an important role bridging the gap between complex academic content and broad public engagement.

In the context of the increasing personalization of data handling styles, chatbots, and especially custom chatbots, can play a significant role in both educational and research processes. For instance Labadze, L., Grigolia, M. & Machaidze, L. write about that from the educational point of view in a systematic literature review devoted to AI chatbots in education: “While many chatbots follow predetermined conversational paths, some employ personalized learning approaches tailored to individual student needs, incorporating experiential and collaborative learning principles”[^1].
[^1]: Labadze, L., Grigolia, M. & Machaidze, L. Role of AI chatbots in education: systematic literature review. Int J Educ Technol High Educ 20, 56 (2023). https://doi.org/10.1186/s41239-023-00426-1. P. 6. Accessed 1 Jan. 2025.

For me, an interesting area of application for a custom chatbot is the analysis of song lyrics. Song lyrics are something of a canonical example for a small corpus study[^2]. However, the methods of corpus research on lyrics are rather limited and, for example, if we are interested not only in the lyrics themselves, but also in the wider context (intertextuality) and the musical component, the researcher is inevitably faced with the need for a lot of “manual” work. This is where an AI-tool like a custom chatbot can be very useful.
[^2]: And this type of study is still quite popular. Here, for example, are a few examples of recent articles:
Corpus linguistic analysis of lyrics and connection to suicide: https://ir.library.oregonstate.edu/concern/graduate_thesis_or_dissertations/bz60d4942. Accessed 1 Jan. 2025.
Corpus-Based Studies on Hip-Hop Lyrics: https://ir.library.oregonstate.edu/concern/graduate_thesis_or_dissertations/0r967c68d. Accessed 1 Jan. 2025.


The main and potential objectives of the project with an emphasis on reducing “manual and routine” work can be briefly summarized as follows:
* Accurate lyric analysis 
* Intertextuality research
* Musical feature and text collaboration analysis 
* Historical and cultural context  description
* Fan engagement and education (+ my mental support)
 * Data-driven insights 

***Project key points***

For the project I tried making a custom chatbot[^3] designed to provide context-aware knowledge about the rock band Eagles and their texts.
[^3]: Guide, provided by Streamlit community, was used to create the bot: https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/ Accessed 1 Jan. 2025.

**User Interface: Streamlit**

The interface of the chatbot is made with Streamlit, a Python framework for interactive web applications. Streamlit provides a chat-based interface where users can input queries and receive responses in real-time. 

**Language Model: DeepSeek (via LlamaIndex)**

At the “heart” of the chatbot is DeepSeek (via API key). Integrated via LlamaIndex, DeepSeek is configured with a system prompt that shapes the chatbot’s responses to act as a seasoned rock guitarist. The model operates with a low temperature setting (0.2), ensuring factual accuracy and preservation of the engaging and optimistic tone at the same time.

**Embedding Model: HuggingFace for Vector Search**

To be able to use DeepSeek the bot utilizes HuggingFaceEmbedding with the BAAI/bge-small-en-v1.5 model. This model converts text into embeddings, which are then used to index documents efficiently. By leveraging these embeddings, the chatbot can perform semantic search, retrieving the most relevant information from Eagles-related knowledge base.

**Document Retrieval: LlamaIndex & VectorStoreIndex**

The bot uses LlamaIndex’s VectorStoreIndex. The SimpleDirectoryReader loads and preprocesses Eagles-related texts from a local directory, allowing the chatbot to reference structured knowledge rather than relying on generative AI only. 

The project was not deployed and run only locally (as some kind of home assistant).

Chat-GPT4 was used as an assistant in creating of the system prompt and problem-solving (for example, it turned out that PyTorch does not work with all versions of the Python interpreter…)

***Some final remarks***

Overall, it seems that this project can be used as a “basement” of any custom chatbot. With quality filling of the knowledge base and thoughtful system prompt, customization can be changed to suit more relevant research goals of the chatbot owner.

In my opinion the chatbot works quite well and gives accurate answers (especially if you add something relevant to the base, I have tried different knowledge base stuffing). In my trial knowledge base there was a dataset[^4]: with Spotify data about specific musical characteristics dedicated to 94 tracks of the band  (where among the attributes were, for example, danceability, volume, tempo etc.), lyrics of these songs, and 3 articles devoted to the related topics.
[^4]: The Bumpkin. (n.d.). 94 Eagles album tracks with Spotify data [Dataset]. Kaggle. https://www.kaggle.com/datasets/thebumpkin/94-eagles-album-tracks-with-spotify-data. Accessed 1 Jan. 2025.

However, apart from my own impressions, I have no accurate tool to measure the quality of answers to complex questions. Also, of course, hallucinations cannot be ruled out, although the knowledge base reduces this probability. All work with chat requires a critical eye and a double check anyway.

Still, in general, a custom chat bot seems like a good additional tool or home assistant and has promise in tasks connected to popularizing scientific content as well.

***Bibliography***:

* Frasca, Caroline, Krista Muir, and Yi Ding. "Build a Chatbot with Custom Data Sources, Powered by LlamaIndex." Streamlit Blog, August 23, 2023. Available at: https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/
* Gonzalez, Leo. Corpus-Based Studies on Hip-Hop Lyrics. Doctoral dissertation, Oregon State University, 2023. Available at: https://ir.library.oregonstate.edu/concern/graduate_thesis_or_dissertations/0r967c68d
* Labadze, L., Grigolia, M. & Machaidze, L. Role of AI chatbots in education: systematic literature review. Int J Educ Technol High Educ 20, 56 (2023). Available at: https://doi.org/10.1186/s41239-023-00426-1. 
* Walters, Holly. A Corpus Linguistic Analysis of Lyrics and Suicide. Master's thesis, Oregon State University, 2023. Available at: https://ir.library.oregonstate.edu/concern/graduate_thesis_or_dissertations/0r967c68d
* The Bumpkin. (n.d.). 94 Eagles album tracks with Spotify data [Dataset]. Kaggle. https://www.kaggle.com/datasets/thebumpkin/94-eagles-album-tracks-with-spotify-data. Accessed 1 Jan. 2025.



