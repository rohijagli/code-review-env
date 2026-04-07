import os
from env.environment import CodeReviewEnv
from env.models import Action

env = CodeReviewEnv()

obs = env.reset()

print("Observation:\n", obs["observation"])

if False:
    from openai import OpenAI

    client = OpenAI(
        base_url=os.getenv("API_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )

    prompt = f"""
Review this code:
{obs['observation']}

Return:
1. issues
2. explanation
3. severity
4. fix
"""

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    action = Action(
        issues=[output],
        explanation=output,
        severity="medium",
        fix=output
    )
else:
    print("No API key found → using dummy action")
    action = Action(
        issues=["assignment instead of comparison", "hardcoded password", "security issue"],
        explanation="The code contains comparison and security issues.",
        severity="high",
        fix="Use == for comparison and avoid hardcoded passwords."
    )

next_obs, reward, done, info = env.step(action)

print("Reward:", reward)
print("Done:", done)
print("Next observation:", next_obs)
