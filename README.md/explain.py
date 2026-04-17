from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="google/flan-t5-small",
    max_new_tokens=150,
    do_sample=True,
    temperature=0.3
)

def explain(score, match):
    with open("prompts/explain_prompt.txt", "r") as f:
        prompt_template = f.read()

    prompt = prompt_template.format(
        score=score,
        match=match
    )

    result = generator(prompt)

    return result[0]["generated_text"].replace(prompt, "").strip()