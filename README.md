# 🌐 Policy Q&A Bot — Azure OpenAI (RAG-lite)

### 🧠 Intelligent Policy Assistant powered by Azure OpenAI + Streamlit

**Developed by:** [Lavanya Srivastava](https://www.linkedin.com/in/lavanya-srivastava/)
**Live Demo:** [https://azurepolicybot.streamlit.app/](https://azurepolicybot.streamlit.app/)
**License:** MIT License

---

## 🚀 Overview

The **Policy Q&A Bot** is an enterprise-grade **Generative AI system** that transforms static HR and compliance documents into interactive, conversational knowledge assistants.

Built using **Azure OpenAI (GPT-4o-mini)** and a **RAG-lite (Retrieval-Augmented Generation)** architecture, it enables employees to ask natural-language questions about company policies and receive **accurate, document-grounded responses** — securely and transparently.

---

## ✨ Key Features

* 📄 **Document-Aware Answers:** Extracts and understands internal policy content automatically.
* 🔒 **Enterprise-Secure:** Hosted through Azure OpenAI ensuring complete confidentiality.
* ⚙️ **RAG-Lite Workflow:** Lightweight retrieval pipeline — no external vector DB required.
* 🪄 **Instant Adaptation:** Upload a new file anytime; responses refresh dynamically.
* 💬 **Streamlit Chat Interface:** Sleek, intuitive UX built for natural query flow.
* ☁️ **Multi-Cloud Compatible:** Works seamlessly on Azure App Service or Streamlit Cloud.

---

## 🏗️ Architecture

```
📁 PDF / DOCX / TXT
       ↓
🧩 Text Extractor (PyPDF2 / python-docx)
       ↓
💬 Context Prompt Builder
       ↓
🤖 Azure OpenAI (GPT-4o-mini)
       ↓
🪄 Policy-Grounded Response
       ↓
🌐 Streamlit Frontend
```

---

## ⚙️ Technology Stack

| Layer         | Technology                                            |
| ------------- | ----------------------------------------------------- |
| **Frontend**  | Streamlit                                             |
| **Backend**   | Azure OpenAI (GPT-4o-mini)                            |
| **Language**  | Python 3.10                                           |
| **Libraries** | openai, streamlit, python-dotenv, PyPDF2, python-docx |
| **Cloud**     | Azure AI Foundry + Streamlit Cloud                    |

---

## 💡 Why It Matters

Corporate policies are often dense, static, and hard to navigate.
**Policy Q&A Bot** brings agility, transparency, and intelligence to enterprise compliance systems — helping organizations achieve:

* 🕒 **Up to 90% faster access** to HR and policy information
* 📚 **Consistent interpretation** across teams and regions
* 🌍 **Scalable multilingual deployment** for global organizations
* ✅ **Traceable, compliant, and explainable** AI-driven answers

---

## 📚 Example HR Policy Documents for Testing

You can validate the app with publicly available HR policy documents — perfect for benchmarking accuracy and document grounding.

### 🔹 Recommended Documents

1. **[HR Guide: Policy & Procedure Template](https://communityfoundations.ca/wp-content/uploads/2021/08/HR-Guide_-Policy-and-Procedure-Template.pdf)**
   *Covers:* Leave policy, attendance, conduct standards
   **Sample Questions:**

   * What is the standard annual leave entitlement?
   * What are the professional conduct expectations?

2. **[Human Resources Policies & Procedures Manual (GESCI)](https://www.gesci.org/fileadmin/user_upload/HUMAN_RESOURCE_POLICIES_-_GESCI__June_2018.pdf)**
   *Covers:* Recruitment, employee categories, benefits, and termination
   **Sample Questions:**

   * What steps are included in the recruitment process?
   * How is probation confirmation handled for new hires?

3. **[IIMA HR Policy Manual 2023](https://www.iima.ac.in/sites/default/files/2023-01/HR%20Policy%20Manual%202023%20%288%29.pdf)**
   *Covers:* Leave, performance, benefits, and discipline
   **Sample Questions:**

   * What is the leave approval process at IIMA?
   * How are disciplinary actions handled?

---

## 💬 Sample Question Categories

### 🧾 Recruitment & Employment

* Who approves new hires?
* What onboarding documents are required?

### 🕒 Leave & Attendance

* How many paid leaves are available annually?
* Does the policy provide maternity or paternity leave?

### 💼 Conduct & Discipline

* What constitutes professional misconduct?
* How are disciplinary hearings conducted?

### 🏥 Medical & Benefits

* What healthcare benefits are provided?
* Are dependents covered under employee insurance?

### 🏠 Retirement & Housing

* What is the official retirement age?
* Can housing benefits continue after retirement?

---

## 🧩 Optional Demo Add-On

A **custom 2-page HR policy sample** (Leave, Conduct & Benefits) can be created for testing or classroom demonstrations — ensuring users experience grounded Q&A behavior immediately.

---

## 🏆 Professional Significance

This project demonstrates expertise in:

* 🧠 Retrieval-Augmented Generation (RAG) system design
* ☁️ Azure OpenAI Foundry orchestration
* 🎯 Prompt engineering and contextual grounding
* 💻 Streamlit deployment for applied GenAI

It reflects the ability to **architect, secure, and deploy** end-to-end Generative AI systems aligned with **enterprise-grade scalability and ethics**.

---

## 📄 License

**MIT License**

Copyright (c) 2025 **Lavanya Srivastava**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

---

## 🌍 Connect with the Creator

**Lavanya Srivastava**
AI Developer | Trainer | Azure OpenAI | RAG | Streamlit | GenAI Systems
🔗 [LinkedIn](https://www.linkedin.com/in/lavanya-srivastava/)
📧 [lavanaya.srivastava@gmail.com](mailto:lavanaya.srivastava@gmail.com)
🖥️ [Live Demo](https://azurepolicybot.streamlit.app/)


## Run locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # add your keys
streamlit run app.py
```
