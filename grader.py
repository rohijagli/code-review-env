def grade(task, action):
    score = 0

    correct_issues = task["issues"]
    total = len(correct_issues)
    found = 0

    # 🔍 Issue detection
    for issue in correct_issues:
        for ai_issue in action.issues:
            if issue.lower() in ai_issue.lower():
                found += 1
                break

    if total > 0:
        score += (found / total) * 0.5

    def grade(task, action):
        score = 0

    correct_issues = task["issues"]
    total = len(correct_issues)
    found = 0

    for issue in correct_issues:
        for ai_issue in action.issues:
            if issue.lower() in ai_issue.lower():
                found += 1
                break

    # Issue score
    if total > 0:
        score += (found / total) * 0.5

    # 🔥 BONUS
    if found == total:
        score += 0.2

    # Explanation
    if len(action.explanation) > 20:
        score += 0.2
    elif len(action.explanation) > 10:
        score += 0.1

    # Severity
    if action.severity == task["severity"]:
        score += 0.1

    # Fix
    if len(action.fix) > 10:
        score += 0.1

    return min(score, 1.0)
    # 🚨 Penalty for useless answers
if found == 0:
    score -= 0.2