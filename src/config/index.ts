import type { SiteConfig, SiteContent } from "../types";

export const SITE_CONFIG: SiteConfig = {
  title: "Harshini Vutukuri — AI ML Developer",
  author: "Harshini",
  description:
    "AI ML Developer",
  lang: "en",
  siteLogo: "/Mee.png",
  navLinks: [
    { text: "Experience", href: "#experience" },
    { text: "Projects", href: "#projects" },
    { text: "About", href: "#about" },
  ],
  socialLinks: [
    { text: "Resume", href: "https://drive.google.com/file/d/1uxaxbrfIeMTlNp8_JobUwU3PPNEC3fAG/view" },
    { text: "LinkedIn", href: "https://www.linkedin.com/in/harshini1v/" },
    { text: "Github", href: "https://github.com/Harshin1V" },
  ],
  socialImage: "/vercel.png",
  canonicalURL: "https://harshin1v.vercel.app/",
};

export const SITE_CONTENT: SiteContent = {
  hero: {
    name: "Harshini Vutukuri",
    specialty: "AI ML Developer",
    summary:
      "Fueled by a deep-seated passion for Artificial Intelligence, I am an AI/ML developer dedicated to transforming innovative ideas into impactful solutions.",
      email: "harshinivutukuri5@gmail.com",
  },
  experience: [
    {
      company: "IBM",
      position: "Backend Developer(ML)",
      startDate: "Jan 2024",
      endDate: "Present",
      summary: [
        "Contributed to developing a multi-agent GenAI platform using LangGraph, watsonx.ai, and FastAPI to automate CRM workflows like ticketing and opportunity creation. Implemented RAG, SQL, and Reflection agents, improving context-aware insights from transcripts by 45%.",
        "Containerized backend services using Docker, Podman, and Terraform; built streaming APIs with FastAPI and PostgreSQL to enable seamless integration with Jira, Salesforce, and watsonx Orchestrate.",
        "Automated legacy Z-system test cases using Robot Framework and optimized CI/CD pipelines with Jenkins and Groovy, reducing regression time and defect turnaround by 40% while ensuring accessibility and security compliance.",
        ],
        
    },
    
  ],
  projects: [
    {
      name: "RAG Application built on AWS",
      summary: "Deployed a scalable RAG backend on AWS with serverless architecture, semantic search via pgvector, Gemini Pro integration, and CI/CD using GitHub Actions.",
      linkSource: "https://github.com/Harshin1V/rag-app-on-aws",
      image: "/rag.png",
    },
    {
      name: "Autonomous Agent System",
      summary: "Explored AI agent evolution using Hugging Face’s smolagents, showcasing secure code execution, deep research tasks, and practical agent design with evaluations",
      linkSource: "https://github.com/Harshin1V/CodeAgents",
      image: "/agentic.png",
    },
    {
      name: "Efficient Lottery Ticket Pruning with Optimization",
      summary: "Applied Lottery Ticket Hypothesis on MNIST using PyTorch, showing iterative pruning boosts performance over random reinitialization.",
      linkSource: "https://github.com/Harshin1V/Lottery-Ticket-Hypothesis",
      image: "/lth.png",
    },
  ],
  about: {
    description: `
      Hi, I’m Harshini Vutukuri, an AI/ML Developer passionate about building and deploying end-to-end Generative AI and machine learning solutions. With a solid foundation in both traditional ML and cutting-edge LLMs, I thrive at the intersection of creativity and intelligent systems—turning innovative ideas into impactful, data-driven applications. I love working on real-world problems where AI meets user-centric design and scalable backend engineering.`,
    image: "/Mee.jpeg",
  },
};

// #5755ff
