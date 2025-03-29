import streamlit as st
import webbrowser

col1, col2 = st.columns([1, 1])
with col1:
    st.write("") 
    st.image("profile-pic.png", width=200)
    st.markdown("📄[Resume](https://drive.google.com/file/d/15J8CczzIFw2rpGkdoJMwardi06IAYz6H/view?usp=sharing)")
    st.markdown("🌎[LinkedIn](https://www.linkedin.com/in/harshini1v/)")
    st.markdown("👩🏻‍💻[GitHub](https://github.com/Harshin1V)")
with col2:
    st.markdown("### </u>Harshini Vutukuri</u> ", unsafe_allow_html=True)
    st.markdown("**`human = True`** Fueled by a relentless passion for Artificial Intelligence.")
    st.markdown("I’m passionate about pushing the boundaries of AI innovation. Whether it’s building intelligent systems that understand human conversations or deploying scalable AI solutions, I’m constantly exploring how technology can be harnessed to solve real-world challenges.") 
    st.markdown("**Let’s build the future — one algorithm at a time.**")
    


st.markdown("## **Skills👩‍💻**")
col1, col2 = st.columns([1, 1])  
with col1:
    st.markdown("### 🖥️ **Programming and Development**")  
    st.markdown("- Python")  
    st.markdown("- NumPy, Pandas, SciPy")  
    st.markdown("- FastAPI, Django")  
    st.markdown("- RESTful API Development")  
    st.markdown("- Object-Oriented Programming (OOP)")  
    st.markdown("- Data Structures and Algorithms")
with col2:
    st.markdown("### 📊 **Machine Learning**")  
    st.markdown("- Supervised and Unsupervised Learning")  
    st.markdown("- Regression, Classification, Clustering")  
    st.markdown("- Scikit-Learn, XGBoost, LightGBM")  
    st.markdown("- Ensemble Methods (Bagging, Boosting)")  
    st.markdown("- Feature Engineering and Model Selection")  
    st.markdown("- Model Evaluation Metrics")  

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### 🧠 **Deep Learning**")
    st.markdown("- Neural Networks (CNNs, RNNs, LSTMs, GRUs)")
    st.markdown("- Transformer Models (BERT, GPT, LLaMA)")
    st.markdown("- PyTorch, TensorFlow, Keras")
    st.markdown("- Natural Language Processing (NLP)")
    st.markdown("- Audio and Speech Recognition")
    st.markdown("- Computer Vision (CV)")
with col2:
    st.markdown('### 🚀 **Generative AI**')
    st.markdown('- Large Language Models (LLMs)')
    st.markdown('- Fine-Tuning and Prompt Engineering')
    st.markdown('- Generative Adversarial Networks (GANs) ')
    st.markdown('- Retrieval-Augmented Generation (RAG)') 
    st.markdown('- LangChain, Hugging Face Transformers') 
    st.markdown('- LLaMA, Mistral, Mixtral')


col1, col2 = st.columns([1, 1])  
with col1:
    st.markdown("### 📦 **AI Model Deployment**")
    st.markdown("- Model Deployment with FastAPI, Django")  
    st.markdown("- Streamlit for Interactive AI Applications") 
    st.markdown("- Containerization (Docker)") 
    st.markdown("- Model Monitoring and Evaluation")
with col2:
    st.markdown("### 🗄️ **Data Management and Engineering**") 
    st.markdown("- SQL, NoSQL (MongoDB, Cassandra)")
    st.markdown("- ETL (Extract, Transform, Load)")  
    st.markdown("- Data Preprocessing and Cleaning") 
    st.markdown("- Version Control, Git, GitHub") 


st.markdown("---")


st.markdown("## Projects🏅")


# 1+1

st.markdown("### 📄 **Advanced RAG System with Feedback Integration** [GitHub](https://github.com/Harshin1V/Hybrid-RAG)")
st.markdown("- Developed an **AI-powered document Q&A system** using **Streamlit** with **hybrid retrieval** combining **semantic embeddings** and **BM25** retrieval methods using a weighted ensemble.")  
st.markdown("- Implemented a **feedback loop** to dynamically adjust retriever weights based on user feedback, improving response accuracy.")  
st.markdown("- Built a **feedback dashboard** for real-time monitoring and analysis of system performance.")  
st.write(" ")

# 2
st.markdown("### 📝 **AI-Powered Meeting Minutes Generator** [GitHub](https://github.com/Harshin1V/Meeting-Minutes)")
st.markdown("- Developed an AI application to **generate meeting minutes** from audio recordings using **OpenAI's Whisper** for speech-to-text transcription and **Meta's LLaMA 3.1** for summarization.")
st.markdown("- Designed an **interactive Streamlit interface** for audio upload, real-time transcription, and AI-powered summary generation in a professional markdown format.")
st.markdown("- Implemented a **download feature** to export meeting minutes with clear sections, including executive summaries, action items, key decisions, and next steps.")
st.write(" ")

# 3
st.markdown("### 🏆 **Efficient Lottery Ticket Pruning with Advanced Optimization** [GitHub](https://github.com/Harshin1V/Lottery-Ticket-Hypothesis)")
st.markdown("- Enhanced neural network pruning using LTH with **gradient clipping** and **dropout regularization** for improved model stability and generalization.", unsafe_allow_html=True)
st.markdown("- Applied **Kaiming initialization** and adopted the **AdamW optimizer** for faster convergence and better training performance.", unsafe_allow_html=True)
st.markdown("- Ensured reproducibility with **fixed seeds** and conducted detailed performance analysis using **Seaborn visualizations**, achieving high accuracy at reduced model size.", unsafe_allow_html=True)  
st.write(" ")


# 4
st.markdown("### 🤖 **Machine Learning Algorithms from Scratch** [GitHub](https://github.com/Harshin1V/MLfromscratch/blob/main/README.md)")
st.markdown("- Implemented key machine learning algorithms from the ground up, including KNN, Linear Regression, Logistic Regression, Naive Bayes, Perceptron, SVM, Decision Tree, Random Forest, PCA, K-Means, AdaBoost, and LDA.")
st.markdown("- Developed and tested algorithms by working directly with datasets, showcasing strong understanding of underlying principles and improving debugging and optimization skills.")
st.markdown("- Utilized NumPy for mathematical implementation, Scikit-learn for data generation and testing, Pandas for data loading, and Matplotlib for data visualization.")
st.write("---")
# 5
st.markdown(" ### **Work Experience:** ")
st.markdown("**Software Developer** | **IBM z-Firmware (1.5+ years)**")
st.markdown("- Developed Infrastructure as Code (IaC) using Terraform and Ansible, modernizing pipelines and enhancing operational efficiency. Managed Jenkins-based driver pipelines for daily builds and regression testing, ensuring timely issue resolution and build continuity.")  
st.markdown("- Collaborated cross-functionally with global teams, proactively resolving issues, providing updates, and driving continuous improvements.")  
