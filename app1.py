import streamlit as st
import webbrowser

col1, col2 = st.columns([1,2])
with col1:
    st.write("") 
    st.image("profile-pic.png", width=200)
    
with col2:
    st.markdown("### </u>Harshini Vutukuri</u> ", unsafe_allow_html=True)
    st.markdown("**`human = True`** Fueled by a deep-seated passion for Artificial Intelligence, I am an AI/ML developer dedicated to transform innovative ideas into impactful solutions.  **Let’s connect!**")
    st.markdown("**Code Train Fine-tune Repeat❤️**")
    st.markdown("**📄[Resume](https://drive.google.com/file/d/1ghvEyz3WS45hs4luqWc-vtjWhArL2gM2/view?usp=sharing) &nbsp; &nbsp;  🌎[LinkedIn](https://www.linkedin.com/in/harshini1v/) &nbsp; &nbsp; 👩🏻‍💻[GitHub](https://github.com/Harshin1V)**")

st.markdown("---")
st.markdown("### Projects🏅")

st.write("""
         #### 🧠 **Autonomous Agent System** [GitHub](https://github.com/Harshin1V/CodeAgents)
        - Designed code agents using **Hugging Face SmolAgents**, integrating **sandboxing** (E2B), multi-agent systems, and performance evaluation to autonomously execute complex tasks like web browsing, data extraction and multi-step reasoning.
        """)

st.write("""
         #### 📄 **Advanced RAG System with Feedback Integration** [GitHub](https://github.com/Harshin1V/Hybrid-RAG)
         - Developed and deployed a document Q&A system on Streamlit Cloud, integrating hybrid retrieval (semantic embeddings + BM25) with real-time feedback loops, utilizing ngrok to expose the Ollama LLM backend for dynamic retriever adjustment and performance monitoring.
        """)

st.markdown("""
            #### 🏆 **Efficient Lottery Ticket Pruning with Optimization** [GitHub](https://github.com/Harshin1V/Lottery-Ticket-Hypothesis)
            - Optimized neural network training using Lottery Ticket Hypothesis (LTH), gradient clipping, dropout regularization, and AdamW optimizer, improving model stability, generalization, and performance analysis via Seaborn visualizations.
            """)

# 2
st.markdown("""
            #### 📝 **Meeting Minutes Generator using Whisper** [GitHub](https://github.com/Harshin1V/Meeting-Minutes)
            -  Developed an application to **generate meeting minutes** from audio recordings using **OpenAI's Whisper** for speech-to-text transcription and **Meta's LLaMA 3.1** for summarization. Designed an **interactive Streamlit interface** for audio upload, real-time transcription, and AI-powered summary")
            """)
# 2
# st.markdown("""
#             #### 📝 **Blog-Post-Generator** [GitHub](https://github.com/Harshin1V/Meeting-Minutes)
#             -  Developed an AI application to **generate meeting minutes** from audio recordings using **OpenAI's Whisper** for speech-to-text transcription and **Meta's LLaMA 3.1** for summarization. Designed an **interactive Streamlit interface** for audio upload, real-time transcription, and AI-powered summary")
#             """)

# 3


# 4
st.markdown("""
            #### 🤖 **Machine Learning Algorithms from Scratch** [GitHub](https://github.com/Harshin1V/MLfromscratch/blob/main/README.md)
            - Implemented key machine learning algorithms from the ground up, including <u> KNN, Linear Regression, Logistic Regression, Naive Bayes, Perceptron, SVM, Decision Tree, Random Forest, PCA, K-Means, AdaBoost, and LDA.</u>.
            """,unsafe_allow_html=True)  



st.markdown("---")

st.markdown("### **Skills👩‍💻**")
col1, col2 = st.columns([1, 1])  
with col1:
    st.markdown("""
                ##### 🖥️ **Programming and Development**
                - Python
                - NumPy, Pandas, SciPy
                - FastAPI, Django
                - RESTful API Development
                - Object-Oriented Programming (OOP)
                - Data Structures and Algorithms
                """)
with col2:
    st.markdown("""
                ##### 📊 **Machine Learning**
                - Supervised and Unsupervised Learning
                - Regression, Classification, Clustering
                - Scikit-Learn, XGBoost, LightGBM  
                - Ensemble Methods (Bagging, Boosting)
                - Feature Engineering and Model Selection
                - Model Evaluation Metrics
                """)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("""
                ##### 🧠 **Deep Learning**
                - Neural Networks (CNNs, RNNs, LSTMs, GRUs)
                - Transformer Models (BERT, GPT, LLaMA)
                - PyTorch, TensorFlow, Keras
                - Natural Language Processing (NLP)
                - Audio and Speech Recognition
                - Computer Vision (CV)
                 """)
with col2:
    st.markdown("""
                ##### 🚀 **Generative AI**
                - Large Language Models (LLMs)
                - Fine-Tuning and Prompt Engineering
                - Generative Adversarial Networks (GANs)
                - Retrieval-Augmented Generation (RAG) 
                - LangChain, Hugging Face Transformers 
                - LLaMA, Mistral, Mixtral
                 """)


col1, col2 = st.columns([1, 1])  
with col1:
    st.markdown("""
                ##### 📦 **AI Model Deployment**
                - Model Deployment with FastAPI, Django
                - Streamlit for Interactive AI Applications
                - Containerization (Docker)
                - Model Monitoring and Evaluation
                 """)
with col2:
    st.markdown("""
                ##### 🗄️ **Data Management and Engineering** 
                - SQL, NoSQL (MongoDB, Cassandra)
                - ETL (Extract, Transform, Load)  
                - Data Preprocessing and Cleaning
                - Version Control, Git, GitHub
                """) 


st.write("---")
# 5
st.markdown("""
                #### 💼 **Work Experience:**
                **Software Developer**<br>*IBM, Bangalore, India | Jan 2024 – Present*
                - Automated 65% of Z-system test cases using Robot Framework, reducing regression test cycles.
                - Built and optimized CI/CD pipelines with Jenkins and Groovy, accelerating integration frequency.
                - Collaborated with accessibility and security teams to ensure compliance with enterprise standards.
                - Streamlined issue resolution workflows, cutting debugging and defect tracking tools turnaround by 40%.
                
            """, unsafe_allow_html=True)
