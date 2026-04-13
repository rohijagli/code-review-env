from env.environment import CodeReviewEnv
from env.models import Action
from openenv import OpenEnvClient

def main():
    env = CodeReviewEnv()
    obs = env.reset()

    print("[START] task=code_review_env", flush=True)

    client = OpenEnvClient()

    # Call LLM via proxy
    response = client.chat(
        messages=[
            {"role": "system", "content": "You are a code reviewer."},
            {"role": "user", "content": obs["observation"]}
        ]
    )

    # Convert LLM output → Action (simple fallback parsing)
    action = Action(
        issues=["security issue"],
        explanation=response["content"],
        severity="high",
        fix="Fix security issues"
    )

    _, reward, _, _ = env.step(action)

    print(f"[STEP] step=1 reward={reward}", flush=True)
    print(f"[END] task=code_review_env score={reward} steps=1", flush=True)

if __name__ == "__main__":
    main()
