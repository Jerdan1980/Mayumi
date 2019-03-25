from OsuApi import OsuApi, ReqConnector
import requests
import re #regular expressions used for searching strings...
  #https://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python

api = OsuApi("myKey", connector = ReqConnector())

msg = input("prompt: ")

if "peppy" in msg:
  player = api.get_user("peppy")[0]
  print(player.user_id)
if "ppy.sh" in msg:
  print("this is a beatmap link")
if ("get" in msg) and ("user" in msg):
  indexes = [m.start() for m in re.finditer('`', msg)]
  username = msg[indexes[0]:indexes[1]])
  if "full" in msg:
    results = uFull(username)
  print(results)