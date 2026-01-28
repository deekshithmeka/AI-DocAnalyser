import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_notes(text):
    prompt = f"""
You are a smart academic assistant.

From the following document, generate structured study notes in pure HTML using this exact structure:

<div class="note-section">
  <h4>📄 Summary</h4>
  <ul>
    <li>...</li>
  </ul>
</div>

<div class="note-section">
  <h4>🔑 Key Points</h4>
  <ul>
    <li>...</li>
  </ul>
</div>

<div class="note-section">
  <h4>🧠 Important Terms</h4>
  <ul>
    <li><b>Term</b> – meaning</li>
  </ul>
</div>

Rules:
- Use only valid HTML
- Use bullet lists
- Keep language simple
- Do not include anything outside these three sections

Document:
{text}
"""
    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return res.choices[0].message.content

def ask_question(context_chunks, question, style):
    context_text = "\n\n".join(context_chunks)

    prompt = f"""
You are a student assistant.
Use ONLY the following context to answer.

Context:
{context_text}

Instruction:
{style}

Question:
{question}
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content
