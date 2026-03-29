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
            }
        ]
        self.current_task = None
        self.done = False

    def reset(self):
        self.current_task = random.choice(self.tasks)
        self.done = False

        return {
            "observation": self.current_task["code"],
            "reward": 0.0,
            "done": False,
            "info": {}
        }

    def step(self, action: Action):
        if self.done:
            return {}, 0.0, True, {}

        reward = grade(self.current_task, action)
        self.done = True

        return (
            {},
            reward,
            True,
            {}
        )

    def state(self):
        return {
            "current_task": self.current_task,
            "done": self.done
        }
