data = input().split("\\")
last_index = data[-1]

file_and_ext = last_index.split(".")
print(f"File name: {file_and_ext[-2]}")
print(f"File extension: {file_and_ext[-1]}")
