def add_points(user, results, points):
    if user not in results:
        results[user] = points
    else:
        if results[user] > points:
            return results
        else:
            results[user] = points
    return results


def add_submissions(lang, submissions):
    if lang not in submissions:
        submissions[lang] = 0
    submissions[lang] += 1
    return submissions


def is_banned(user, results):
    if user in results:
        results.pop(user)
    return results


results = {}
submissions = {}

command = input()
counter = 0

while not command == "exam finished":
    command = command.split('-')
    if command[1] == "banned":
        user = command[0]
        results = is_banned(user, results)
    else:
        name, language, points = command[0], command[1], int(command[2])
        results = add_points(name, results, points)
        submissions = add_submissions(language, submissions)

    command = input()

results = dict(sorted(results.items(), key=lambda x: (-x[1], x[0])))
submissions = dict(sorted(submissions.items(), key=lambda x: (-x[1], x[0])))

print("Results:")
for key, value in results.items():
    print(f"{key} | {value}")

print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")