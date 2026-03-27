import os
from env.environment import CodeReviewEnv
from env.models import Action

env = CodeReviewEnv()

obs = env.reset()

print("Code:\n", obs["code"])

# If API key exists → use OpenAI
if False:
    from openai import OpenAI

    client = OpenAI(
        base_url=os.getenv("API_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = f"""
    Review this code:
    {obs['code']}
    Find issues and explain them.
    """

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    action = Action(issue=output, explanation=output)

# ❗ No API → fallback (VERY IMPORTANT)
else:
    print("No API key found → using dummy action")

    action = Action(
    issues=["assignment instead of comparison"],
    explanation="Using = instead of == leads to incorrect condition evaluation",
    severity="medium",
    fix="Replace = with == in the condition"
)

obs, reward, done, _ = env.step(action)

print("Reward:", reward)
print("Done:", done)