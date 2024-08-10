import requests

tok = "YOUR_DISCORD_TOKEN"

# Remplacez "YOUR_DISCORD_TOKEN" par votre propre jeton Discord
headers = {
    "Authorization": tok
}

def get_guilds():
    response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erreur lors de la récupération des serveurs :", response.status_code)
        return None

def get_channels(guild_id):
    response = requests.get(f"https://discord.com/api/v10/guilds/{guild_id}/channels", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur lors de la récupération des canaux du serveur {guild_id} :", response.status_code)
        return None

def write_to_file(guilds):
    with open("channel_ids.txt", "w") as file:
        for guild in guilds:
            file.write(f"{guild['id']}:")
            print(f"LOG [+] Server : {guild['id']}")
            channels = get_channels(guild['id'])
            if channels:
                for channel in channels:
                    file.write(f"{channel['id']}:")
            file.write("\n")

def main():
    guilds = get_guilds()
    if guilds:
        write_to_file(guilds)

if __name__ == "__main__":
    main()
