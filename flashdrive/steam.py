import steamapi

steamapi.core.APIConnection(api_key = "key", validate_Key = True)

msg = input("Prompt: ")

user = steamapi.user.SteamUser(msg)
print(user.level)