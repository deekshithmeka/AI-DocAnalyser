from flask import Flask, request, render_template, send_file
from services.pdf_services import extract_text
from services.ai_services import generate_notes, ask_question
from services.vector_service import add_documents, query_documents
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import io

app = Flask(__name__)

all_docs_text = ""
notes = ""
chat_history = []

@app.route("/", methods=["GET", "POST"])
def home():
    global all_docs_text, notes, chat_history
    answer = ""

    if request.method == "POST":

        # Multi PDF upload
        if "pdfs" in request.files:
            files = request.files.getlist("pdfs")
            all_docs_text = ""
            chat_history.clear()

            for file in files:
                all_docs_text += "\n\n--- New Document ---\n\n"
                all_docs_text += extract_text(file)

            add_documents(all_docs_text)
            notes = generate_notes(all_docs_text)

        # Question asked
        if "question" in request.form:
            question = request.form["question"]
            mode = request.form["mode"]

            if mode == "simple":
                style = "Explain in very simple words for a beginner."
            elif mode == "exam":
                style = "Give an exam-oriented answer in clear points."
            else:
                style = "Give a detailed technical explanation."

            relevant_chunks = query_documents(question)
            answer = ask_question(relevant_chunks, question, style)

            chat_history.append({
                "question": question,
                "answer": answer,
                "mode": mode
            })

    return render_template(
        "index.html",
        answer=answer,
        notes=notes,
        history=chat_history
    )


# 🔽 THIS MUST BE OUTSIDE home()
@app.route("/download-notes")
def download_notes():
    global notes

    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    for line in notes.split("\n"):
        safe = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        story.append(Paragraph(safe, styles["Normal"]))

    doc = SimpleDocTemplate(buffer)
    doc.build(story)

    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="Auto_Notes.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    app.run(debug=True)
