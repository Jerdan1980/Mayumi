import random

msg = input("message: ")

if ("should" in msg and "?" in msg) or ("8ball" in msg):
  file = open('8ball.txt')
  answer = file.read().splitlines()[random.randint(len(file.readlines()))]
  print(answer)
elif "hello" in msg or "hullo" in msg:
  file = open('hello.txt')
  answer = file.read().splitlines()[random.randint(len(file.readlines()))]
  print(answer)
elif "bye" in msg or "cya" in msg:
  file = open('goodbye.txt')
  answer = file.read().splitlines()[random.randint(len(file.readlines()))]
  print(answer)
