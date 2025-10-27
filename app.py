import os, io
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
from PyPDF2 import PdfReader
from docx import Document

load_dotenv()

ENDPOINT   = os.getenv("AZURE_OPENAI_ENDPOINT", "")
API_KEY    = os.getenv("AZURE_OPENAI_API_KEY", "")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
API_VER    = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

client = AzureOpenAI(
    api_key=API_KEY,
    api_version=API_VER,
    azure_endpoint=ENDPOINT
)

st.set_page_config(page_title="Policy Q&A (Azure RAG-lite)", page_icon="🧠")
st.title("🧠 Policy Q&A — Azure OpenAI (RAG-lite)")
st.caption("Built by Lavanya Srivastava • GPT-4o-mini on Azure • File-grounded answers")

# --- Helpers --------------------------------------------------
def extract_text(file):
    name = file.name.lower()
    data = file.read()
    byts = io.BytesIO(data)
    if name.endswith(".pdf"):
        text = []
        reader = PdfReader(byts)
        for p in reader.pages:
            text.append(p.extract_text() or "")
        return "\n".join(text)
    elif name.endswith(".docx"):
        doc = Document(byts)
        return "\n".join(p.text for p in doc.paragraphs)
    else:
        # txt or anything else treated as text
        return data.decode("utf-8", errors="ignore")

# --- Sidebar: upload policy -----------------------------------
with st.sidebar:
    st.subheader("📄 Upload policy file")
    file = st.file_uploader("Upload .txt / .pdf / .docx", type=["txt","pdf","docx"])
    if file:
        policy_text = extract_text(file)
        st.success(f"Loaded: {file.name} ({len(policy_text)} chars)")
    else:
        policy_text = ""

# --- Chat UI --------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

def ask_llm(question, context):
    system = (
        "You are an intelligent company policy assistant. "
        "Answer ONLY using the facts from the provided policy context. "
        "If the answer is not in the policy, say: "
        "\"I don't see this in the policy document.\" Keep answers concise."
    )
    user = f"Policy context:\n\"\"\"\n{context}\n\"\"\"\n\nQuestion: {question}"
    resp = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role":"system","content":system},
            {"role":"user","content":user}
        ],
        temperature=0.2
    )
    return resp.choices[0].message.content

st.write("Ask a question about your policy document:")
q = st.text_input("Your question", placeholder="e.g., How many paid annual leave days do we get?")
go = st.button("Ask")

if go:
    if not policy_text:
        st.warning("Please upload a policy file in the sidebar first.")
    elif not q.strip():
        st.warning("Type a question.")
    else:
        answer = ask_llm(q.strip(), policy_text[:120000])  # protect token limits
        st.session_state.history.append((q.strip(), answer))

for i, (qq, aa) in enumerate(reversed(st.session_state.history), 1):
    st.markdown(f"**Q{i}. {qq}**")
    st.write(aa)
    st.divider()

st.caption("Tip: replace the policy file anytime; answers will adapt instantly.")
