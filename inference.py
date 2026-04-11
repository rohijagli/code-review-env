from env.environment import CodeReviewEnv
from env.models import Action

def main():
    env = CodeReviewEnv()

    obs = env.reset()

    print("[START] task=code_review_env", flush=True)

    action = Action(
        issues=["hardcoded password", "security issue", "assignment instead of comparison"],
        explanation="The code contains comparison and security issues.",
        severity="high",
        fix="Use == for comparison and avoid hardcoded passwords."
    )

    next_obs, reward, done, info = env.step(action)

    print(f"[STEP] step=1 reward={reward}", flush=True)
    print(f"[END] task=code_review_env score={reward} steps=1", flush=True)

if __name__ == "__main__":
    main()
