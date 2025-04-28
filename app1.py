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
    st.markdown("**📄[Resume](https://drive.google.com/file/d/15J8CczzIFw2rpGkdoJMwardi06IAYz6H/view?usp=sharing) &nbsp; &nbsp;  🌎[LinkedIn](https://www.linkedin.com/in/harshini1v/) &nbsp; &nbsp; 👩🏻‍💻[GitHub](https://github.com/Harshin1V)**")

st.markdown("---")
st.markdown("### Projects🏅")

st.write("""
         #### 📄 **AGENTIC** [GitHub](https://github.com/Harshin1V/Hybrid-RAG)
         - Developed an **AI-powered document Q&A system** using **Streamlit** with **hybrid retrieval** combining **semantic embeddings** and **BM25** retrieval methods using a weighted ensemble.Implemented a **feedback loop** to dynamically adjust retriever weights based on user feedback, improving response ace.
         """)

st.write("""
         #### 📄 **Advanced RAG System with Feedback Integration** [GitHub](https://github.com/Harshin1V/Hybrid-RAG)
         - Developed an **AI-powered document Q&A system** using **Streamlit** with **hybrid retrieval** combining **semantic embeddings** and **BM25** retrieval methods using a weighted ensemble.Implemented a **feedback loop** to dynamically adjust retriever weights based on user feedback, improving respormance.
         """)

# 2
st.markdown("""
            #### 📝 **Meeting Minutes Generator using Whisper** [GitHub](https://github.com/Harshin1V/Meeting-Minutes)
            -  Developed an AI application to **generate meeting minutes** from audio recordings using **OpenAI's Whisper** for speech-to-text transcription and **Meta's LLaMA 3.1** for summarization. Designed an **interactive Streamlit interface** for audio upload, real-time transcription, and AI-powered summary")
            """)
# 2
st.markdown("""
            #### 📝 **Blog-Post-Generator** [GitHub](https://github.com/Harshin1V/Meeting-Minutes)
            -  Developed an AI application to **generate meeting minutes** from audio recordings using **OpenAI's Whisper** for speech-to-text transcription and **Meta's LLaMA 3.1** for summarization. Designed an **interactive Streamlit interface** for audio upload, real-time transcription, and AI-powered summary")
            """)

# 3
st.markdown("""
            #### 🏆 **Efficient Lottery Ticket Pruning with Optimization** [GitHub](https://github.com/Harshin1V/Lottery-Ticket-Hypothesis)
            - Enhanced neural network pruning using LTH with **gradient clipping** and **dropout regularization** for improved model stability and generalization.Ensured reproducibility with **fixed seeds** and conducted detailed performance analysis using **Seaborn visualizations**, achieving high accuracy at reduced model size.
            """)

# 4
st.markdown("""
            #### 🤖 **Machine Learning Algorithms from Scratch** [GitHub](https://github.com/Harshin1V/MLfromscratch/blob/main/README.md)
            - Implemented key machine learning algorithms from the ground up, including <u> KNN, Linear Regression, Logistic Regression, Naive Bayes, Perceptron, SVM, Decision Tree, Random Forest, PCA, K-Means, AdaBoost, and LDA.</u> Developed and tested algorithms by working directly with datasets, showcasing strong understanding of underlying principles and improving debugging and optimization skills.
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
st.markdown(" ### **Work Experience:** ")
st.markdown("**Software Developer** | **IBM z-Firmware (1.5+ years)**")
st.markdown("- Developed Infrastructure as Code (IaC) using Terraform and Ansible, modernizing pipelines and enhancing operational efficiency. Managed Jenkins-based driver pipelines for daily builds and regression testing, ensuring timely issue resolution and build continuity.")  
st.markdown("- Collaborated cross-functionally with global teams, proactively resolving issues, providing updates, and driving continuous improvements.")  
