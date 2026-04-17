from chains.extract import extract_data
from chains.match import match_skills
from chains.score import score_candidate
from chains.explain import explain

# Job Description
job_desc = """
Data Scientist role
Skills: Python, Machine Learning, SQL, NLP
Experience: 2+ years
"""

# Resume files
resume_files = ["strong.txt", "average.txt", "weak.txt"]

for file in resume_files:
    print("\n==============================")
    print(f"📄 Testing Resume: {file}")
    print("==============================")

    with open(f"resumes/{file}", "r") as f:
        resume = f.read()

    extracted = extract_data(resume)
    match = match_skills(extracted, job_desc)
    score = score_candidate(match)
    result = explain(score, match)

    print("\n--- EXTRACTED DATA ---")
    print(extracted)

    print("\n--- MATCH RESULT ---")
    print(match)

    print("\n--- SCORE ---")
    print(score)

    print("\n--- FINAL EXPLANATION ---")
    print(result)