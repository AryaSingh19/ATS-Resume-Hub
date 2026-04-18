def match_keywords(skills, job_description):
    # Clean and split skills properly
    clean_skills = []
    for s in skills:
        for word in s.split():
            clean_skills.append(word.strip().lower())

    jd_words = job_description.lower().split()

    updated = list(set(clean_skills))

    for word in jd_words:
        if word not in updated and len(word) > 3:
            updated.append(word)

    return updated


def enhance_experience(experience):
    # Split by comma for better input handling
    lines = experience.split(",")

    improved = []
    for line in lines:
        line = line.strip()

        if line:
            improved.append(f"Developed {line} with measurable impact")

    return improved


def calculate_ats_score(skills, job_description):
    jd_words = job_description.lower().split()
    skills = [s.strip().lower() for s in skills]

    matched = 0

    for word in jd_words:
        if word in skills:
            matched += 1

    total = len(set(jd_words))

    if total == 0:
        return 0, []

    score = int((matched / total) * 100)

    missing = []
    for word in jd_words:
        if word not in skills and len(word) > 3:
            missing.append(word)

    return score, list(set(missing))