import streamlit as st
import webbrowser

st.set_page_config(
    page_title="Harshini Vutukuri",
    page_icon="profile-pic.png"
)

# CSS 
st.markdown("""
    <style>
        body{
            max-width: 800px;
            background-color: #000000 !important;
        }
        .block-container, {
            max-width: 800px;
            background-color: #000000 !important;
        }
        .main {
            max-width: 800px
            background-color: #000000;
            padding: 2rem;
            font-family: 'Segoe UI', sans-serif;
            color: #f5f5f5;
        }
        .profile-pic {
            border-radius: 50%;
            box-shadow: 0 4px 8px rgba(0,0,0,0.6);
            margin-top: 1rem;
        }
        .header-title {
            font-size: 2.2rem;
            font-weight: 600;
            color: #f5f5f5;
        }
        .intro {
            font-size: 1.1rem;
            margin-top: 0.8rem;
            color: #cccccc;
        }
        .links a {
            margin-right: 15px;
            text-decoration: none;
            color: #66ccff;
            font-weight: bold;
        }
        .highlight-box {
            background: #141617;
            padding: 1rem;
            border-radius: 12px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.5);
            margin-bottom: 1.5rem;
        }
        .project-title {
            font-size: 1.2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: #ffffff;
        }
        .project-desc {
            color: #cccccc;
        }
        .section-title {
            color: #66ccff;
            font-size: 1.8rem;
            margin-top: 2rem;
        }
        .skill-section, .experience-box {
            background: #141617;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.4);
            margin-top: 1rem;
            color: #e0e0e0;
        }
        a {
            color: #66ccff !important;
        }
        .skill-section {
        background-color: #141617;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.2);
        }
        .skill-section h6 {
            color: #66ccff;
            margin-bottom: 0.5rem;
        }
        .skill-section ul {
            padding-left: 1.2rem;
            color: #e0e0e0;
        }

    </style>
""", unsafe_allow_html=True)

contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL@example.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

col1, col2 = st.columns([1, 2])
with col1:
    st.image("profile-pic.png", width=200, use_container_width=False, output_format="PNG")

with col2:
    st.markdown("<div class='header-title'>Harshini Vutukuri</div>", unsafe_allow_html=True)
    st.markdown("<div class='intro'><b> human = True</b> Fueled by a deep-seated passion for Artificial Intelligence, I am an AI/ML developer dedicated to transforming innovative ideas into impactful solutions. <br>Let’s connect! <br><br><b>Code Train Fine-tune Repeat❤️</b> <p></div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='links'>
        📄 <a href='https://drive.google.com/file/d/139YJS2doN0JLXtxIP-rdkk6FuBavGtKG/view?usp=sharing' target='_blank'>Resume</a>
        🌎 <a href='https://www.linkedin.com/in/harshini1v/' target='_blank'>LinkedIn</a>
        👩🏻‍💻 <a href='https://github.com/Harshin1V' target='_blank'>GitHub</a>
        📩 <a href="mailto:harshinivutukuri5@gmail.com?subject=Hello%20Harshini!" target="_blank">Email me</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<div class='section-title'>Projects 🏅</div>", unsafe_allow_html=True)

projects = [
    {"title": "RAG Application built on AWS", "link": "https://github.com/Harshin1V/rag-app-on-aws",
     "desc": "Deployed a scalable Retrieval-Augmented Generation (RAG) application backend on AWS using Terraform Infrastructure as Code (IaC), integrating Google Gemini Pro and Embedding models for AI-powered document querying and generation. This backend leverages a serverless architecture (Lambda, API Gateway), PostgreSQL RDS with pgvector for efficient semantic search, and Cognito authentication. The project includes CI/CD with GitHub Actions for automated deployment and features a Streamlit UI for user interaction."},
    {"title": "Autonomous Agent System", "link": "https://github.com/Harshin1V/CodeAgents",
     "desc": "Explored the evolution of AI agents by leveraging Hugging Face's smolagents, demonstrating stages from basic conversational agents to advanced types with capabilities like secure code execution (sandboxing) and performing deep research tasks. The project detailed agent design principles, introduced evaluation metrics, and provided practical implementations and examples primarily within Jupyter Notebooks."},
    {"title": "Efficient Lottery Ticket Pruning with Optimization", "link": "https://github.com/Harshin1V/Lottery-Ticket-Hypothesis",
     "desc": "Implemented the Lottery Ticket Hypothesis (LTH) for neural network pruning using PyTorch on the MNIST dataset, analyzing the impact of iterative pruning compared to random reinitialization. Demonstrated that iterative pruning consistently outperforms random reinitialization across different pruning levels, incorporating robust training enhancements including Gradient Clipping, Dropout Regularization, and AdamW Optimizer."},
    {"title": "Meeting Minutes Generator using Whisper", "link": "https://github.com/Harshin1V/Meeting-Minutes",
     "desc": "Developed an AI-powered Meeting Minutes Generator using OpenAI's Whisper for audio transcription and Meta's LLaMA 3.1 for summarising transcripts into structured meeting minutes. The application features an interactive Streamlit UI for uploading audio files (MP3/WAV) and downloading generated minutes in markdown format. This project demonstrates end-to-end audio processing and text generation leveraging large language models"},
]

for proj in projects:
    st.markdown(f"""
        <div class="highlight-box">
            <div class="project-title">{proj['title']} <a href="{proj['link']}" target="_blank">[GitHub]</a></div>
            <div class="project-desc">{proj['desc']}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<div class='section-title'>Skills 👩‍💻</div>", unsafe_allow_html=True)

skill_sections = [
    ("🖥️ Programming & Development", [
        "Python, SQL", 
        "FastAPI, Django, Streamlit", 
        "RESTful API Development", 
        "Object-Oriented Programming (OOP)", 
        "Data Structures and Algorithms",
        "Jupyter Notebooks & Collab"
    ]),

    ("📊 Machine Learning", [
        "Supervised & Unsupervised Learning",
        "Regression, Classification, Clustering",
        "Feature Engineering "," Model Evaluation",
        "Scikit-Learn, XGBoost, LightGBM",
        "Ensemble Methods, Tuning Techniques"
    ]),

    ("🧠 Deep Learning & AI Techniques", [
        "CNNs, RNNs, LSTMs",
        "Transformers (BERT, GPT, LLaMA)",
        "Neural Network Pruning (LTH)",
        "Gradient Clipping, Dropout, AdamW",
        "Kaiming Initialization",
        "NLP & Speech Recognition (Whisper)",
        "Computer Vision"
    ]),

    ("🚀 Generative AI & LLMs", [
        "LLMs: LLaMA 3.1, Gemini Pro",
        "Retrieval-Augmented Generation (RAG)",
        "Fine-Tuning: PEFT, LoRA, QLoRA",
        "Prompt Engineering, Sandboxing",
        "LangChain, smolagents, Hugging Face",
        "GANs, Mixtral, Mistral",
        "Tool-using & Monitoring Agents"
    ]),

    ("📦 AI Model Deployment & MLOps", [
        "FastAPI, Streamlit UIs",
        "Docker, GitHub Actions",
        "Model Monitoring & Evaluation",
        "Unit & Integration Testing",
        "tox, Tqdm, pip",
        "Linux, Bash Scripting"
    ]),

    ("☁️ Cloud & DevOps (AWS)", [
        "Terraform (IaC), AWS Lambda, S3, RDS",
        "AWS Cognito, Secrets Manager"," API Gateway",
        "CloudWatch, SNS, VPC",
        "CI/CD Pipelines ",
        "GitHub Actions, Jenkins"
    ])
]


left_col, right_col = st.columns(2)

for i, (title, skills) in enumerate(skill_sections):
    section_html = f"""
        <div class='skill-section'>
            <h6>{title}</h6>
            <ul>{''.join([f'<li>{skill}</li>' for skill in skills])}</ul>
        </div>
    """
    if i % 2 == 0:
        with left_col:
            st.markdown(section_html, unsafe_allow_html=True)
    else:
        with right_col:
            st.markdown(section_html, unsafe_allow_html=True)


st.markdown("<div class='section-title'>Work Experience 💼</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='experience-box'>
    <h5>Software Developer<br><span style='font-size: 0.9rem;'>IBM, Bangalore | Jan 2024 – Present</span></h5>
    <ul>
        <li>Automated 65% of Z-system test cases using Robot Framework, reducing regression test cycles.</li>
        <li>Built and optimized CI/CD pipelines with Jenkins and Groovy, accelerating integration frequency.</li>
        <li>Ensured accessibility and security compliance across test workflows.</li>
        <li>Streamlined issue resolution, improving defect turnaround by 40%.</li>
    </ul>
    </div>
""", unsafe_allow_html=True)
