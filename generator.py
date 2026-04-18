def generate_resume(name, skills, education, experience, projects):

    # Clean skills properly
    skills_list = [s.strip().capitalize() for s in skills if s.strip() != ""]

    # Format skills
    formatted_skills = []
    for skill in skills_list:
        formatted_skills.append(skill)

    # Fix experience (avoid double "Developed")
    improved_experience = []
    for line in experience.split("\n"):
        line = line.strip()
        if line != "":
            if line.lower().startswith("developed"):
                improved_experience.append("• " + line)
            else:
                improved_experience.append("• Developed " + line + " with measurable impact")

    # Fix projects
    improved_projects = []
    for proj in projects.split(","):
        proj = proj.strip()
        if proj != "":
            improved_projects.append("• Built " + proj + " using modern technologies")

    return {
        "name": name.upper(),
        "skills": formatted_skills,
        "education": education,
        "experience": improved_experience,
        "projects": improved_projects
    }
