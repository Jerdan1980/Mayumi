from OsuApi import OsuApi, ReqConnector
import requests

api = OsuApi("myKey", connector = ReqConnector()) #will this even work this way?

def uBasic(username):
  player = api.get_user(username)
  results = "Username: " + player.username + " (Rank" + player.pp_rank + ")\n" +
            "Score: " + player.ranked_score + " / " + player.total_score + "\n" +
            "PP: " + player.pp_raw + " Accuracy: " + player.accuracy
  return results

def uFull(username):
  player = api.get_user(username)
  results = user_basic(username)
  results += uBest(username)
  return results

def uBest(username):
  score = api.get_user_best(username)[0]
  results = "Score: " + score.score + " Rank " + score.rank + " (" + score.pp + " pp)\n" +
            "Mods: " + api.enabled_mods

def uRecent(username):
  score = api.get_user_recent(username)[0]
  results = "Score: " + score.score + " Rank " + score.rank + " (" + score.pp + " pp)\n" +
            "Mods: " + api.enabled_mods

def mod_compiler(mods):
  #TODO lol