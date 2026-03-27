def __init__(self):
    self.tasks = [
        {
            "difficulty": "easy",
            "code": "int a = 5;\nif(a = 10) printf('yes');",
            "issue": "assignment instead of comparison"
        },
        {
            "difficulty": "medium",
            "code": "password = input()\nif password == '1234': print('ok')",
            "issue": "hardcoded password"
        },
        {
            "difficulty": "hard",
            "code": "function login(u,p){ if(u==admin && p==123){ return true; }}",
            "issue": "hardcoded credentials"
        }
    ]