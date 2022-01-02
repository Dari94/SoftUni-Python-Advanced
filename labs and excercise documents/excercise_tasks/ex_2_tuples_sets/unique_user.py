n = int(input())
user_names = set()
[user_names.add(input()) for _ in range(n)]
[print(username) for username in user_names]