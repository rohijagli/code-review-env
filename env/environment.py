import random
from env.models import Action
from env.grader import grade

class CodeReviewEnv:
    def __init__(self):
        self.tasks = [
    {
        "difficulty": "easy",
        "code": "int a = 5;\nif(a = 10) printf('yes');",
        "issues": ["assignment instead of comparison"],
        "severity": "medium"
    },
    {
        "difficulty": "medium",
        "code": "password = input()\nif password == '1234': print('ok')",
        "issues": ["hardcoded password", "security issue"],
        "severity": "high"
    },
    {
        "difficulty": "hard",
        "code": "function login(u,p){ if(u==admin && p==123){ return true; }}",
        "issues": ["hardcoded credentials", "no validation", "security flaw"],
        "severity": "high"
    }
]

    def reset(self):
        self.current_task = random.choice(self.tasks)
        return {
            "code": self.current_task["code"],
            "difficulty": self.current_task["difficulty"]
        }
        
    def state(self):
        return self.current_task

    def step(self, action: Action):
        score = grade(self.current_task, action)

        # penalty
        if score < 0.2:
            score -= 0.2

        done = True

        return (
            self.reset(),
            score,
            done,
            {}
        )