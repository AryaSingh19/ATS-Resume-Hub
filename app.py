from flask import Flask, render_template, request
from matcher import match_keywords, enhance_experience, calculate_ats_score
from generator import generate_resume
import PyPDF2

app = Flask(__name__)


def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


@app.route("/")
def home():
    return render_template("builder.html")


@app.route("/generate", methods=["POST"])
def generate():

    # File upload
    file = request.files.get("resume_file")

    extracted_text = ""

    if file:
        extracted_text = extract_text_from_pdf(file)

    # Basic extraction (simple logic)
    name = request.form.get("name") or extracted_text[:30]
    description = request.form.get("description", "")
    skills = request.form.get("skills", "").split(",")
    education = request.form.get("education", "")
    experience = request.form.get("experience", "")
    projects = request.form.get("projects", "")
    job_description = request.form.get("job_description", "")
    template = request.form.get("template", "modern")
    color = request.form.get("color", "blue")

    # ATS logic
    updated_skills = match_keywords(skills, job_description)
    improved_experience = enhance_experience(experience)
    score, missing_keywords = calculate_ats_score(updated_skills, job_description)

    resume = generate_resume(
        name,
        updated_skills,
        education,
        "\n".join(improved_experience),
        projects
    )

    return render_template(
        "result.html",
        name=resume["name"],
        description=description,
        skills=resume["skills"],
        education=resume["education"],
        experience=resume["experience"],
        projects=resume["projects"],
        score=score,
        missing=missing_keywords,
        template=template,
        color=color
    )


if __name__ == "__main__":
    app.run(debug=True)