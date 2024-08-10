import requests
import json
import os
import sys

tok = "YOUR_DISCORD_TOKEN"

def retrieve_messages(channelid):
    headers = {
        'authorization': tok
    }
    r = requests.get(f'https://discord.com/api/v10/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)
    return jsonn

def detecte_insulte(message):
    insultes = [
        "abruti", "aller chier dans sa caisse", "niquer sa mère", "enculer", "aller se faire endauffer", "foutre", 
        "aller se faire mettre", "aller se faire pendre", "allez vous faire foutre", "andouille", "anglo-fou", 
        "Annie Dingo", "appareilleuse", "Arabe", "assimilé", "assimilée", "astèque", "avorton", "bachi-bouzouk", 
        "baleine", "bande d’abrutis", "baraki", "bâtard", "baudet", "beauf", "bellicole", "bête", "bête à pleurer", 
        "bête comme ses pieds", "bête comme un âne", "bête comme un camion", "bête comme un chou", "bête comme un cochon", 
        "bête comme un cygne", "bête comme une oie", "biatch", "bibi", "bic", "bicot", "bicotte", "bique", "bitch", 
        "bite", "bitembois", "Bitembois", "bloke", "bogmoule", "bolos", "bordille", "boucaque", "boudin", "bouègre", 
        "bouffi", "bouffon", "bouffonne", "bougnoul", "bougnoule", "bougnoulisation", "bougnouliser", "bougre", 
        "bougre de", "boukak", "boulet", "bounioul", "bounioule", "bourdille", "bourrer", "bourricot", "bovo", 
        "branleur", "branleuse", "brêle", "bridé", "bridée", "brigand", "brise-burnes", "bulot", "cacou", "cafre", 
        "cageot", "caldoche", "casse-bonbon", "casse-couille", "casse-couilles", "catin", "cave", "chagasse", 
        "charlot de vogue", "charogne", "chauffard", "chauffeur", "chauffeuse", "chbeb", "chiabrena", 
        "chien de chrétien", "chiennasse", "chienne", "chienne de chrétienne", "chier", "chieur", "chieuse", 
        "chinetoc", "chinetoque", "Chinetoque", "chintok", "chleuh", "chnoque", "choucroutard", "citrouille", 
        "coche", "cochonne", "colon", "complotiste", "con", "con comme la lune", "con comme ses pieds", 
        "con comme un balai", "con comme un manche", "con comme une chaise", "con comme une valise", 
        "con comme une valise à poignée intérieure", "con comme une valise sans poignée", "conasse", 
        "conchier", "Conchita", "connard", "connarde", "connasse", "connaud", "conne", "conspirationniste", 
        "contracibête", "cornichon", "couille molle", "counifle", "courtaud", "courtaude", "CPF", "crétin", 
        "crevure", "cricri", "crotté", "crouïa", "crouillat", "crouille", "dago", "débile", "débougnouliser", 
        "dégouiner", "doryphore", "doxosophe", "doxosophie", "drouille", "du schnoc", "ducon", "duconnot", 
        "dugenoux", "dugland", "duschnock", "emmanché", "emmerder", "emmerdeur", "emmerdeuse", "empafé", 
        "empaffé", "empapaouté", "enculé", "enculé de ta race", "enculer", "enfant de fusil", "enfant de garce", 
        "enfant de putain", "enfant de pute", "enfant de salaud", "enflure", "enfoiré", "enfoirée", "envaselineur", 
        "envoyer faire foutre", "épais", "espèce de", "espingoin", "espingouin", "étron", "face de chien", 
        "face de craie", "face de pet", "face de rat", "fachiste", "FART", "FDP", "fell", "féminazie", 
        "fermer sa gueule", "feuj", "fils de bâtard", "fils de chien", "fils de chienne", "fils de garce", 
        "Ass", "Arse", "Bullshit", "Crap", "Damn", "Damn you", "Holy crap", "Piece of shit", "Shut up", 
        "Bastard", "Bloody Hell", "Bollocks", "Blimey", "Bugger", "Little bugger", "Knob", "Moron", 
        "Plonker", "Tosser", "Twat", "Twit", "Wanker", "Coward", "Chicken", "Darn", "Darn it", 
        "Dear me!", "Dear lord", "Dumb", "Effing…", "Fool", "For crying out loud", "Goddamn / Goddammit", 
        "Good heavens!", "Gosh", "Idiot", "Jeez", "Oh dear", "bz", "baize", "Old cow", "Scallywag", 
        "Shoot", "Silly", "Stupid", "Turd", "Villain", "Douche", "Douchebag", "Dumbass", "Jerk", 
        "Piss Off", "Screw you", "Tramp", "Twat", "Get lost!", "Go to hell!", "I don’t give a damn", 
        "I screwed up", "Shut the front door", "What the Fuck ?", "Fuck", "encule", "fils de pute"
    ]
    
    for insulte in insultes:
        if insulte.lower() in message.lower():
            return True
    return False

def detecte_mot_cle(messages, mots_cles):
    resultats = []
    for message in messages:
        if 'content' in message:
            insulte = detecte_insulte(message['content'])
            if insulte:
                for mot in mots_cles:
                    if mot.lower() in message['content'].lower():
                        resultat = {
                            "message": message['content'],
                            "insulte": insulte,
                            "envoye_par": f"{message['author']['username']}#{message['author']['discriminator']}"
                        }
                        resultats.append(resultat)
                        break
    return resultats

def main():
    filename = input("Entrez le nom du fichier contenant les IDs de canal (incluez l'extension .txt) : ")
    os.system('cls')
    with open(filename, 'r') as file:
        channel_ids = file.read().split(':')
        
    with open('result.txt', 'w') as output_file:
        for channelid in channel_ids:
            messages = retrieve_messages(channelid)
            mots_cles = [
                "Achoura", "Aïd-el-Kébir", "Aïd-el-Séghir", "Allah", "Arabes", 
                "Ayatollah", "Babisme", "Calife", "Charia", "Chiisme", 
                "Circoncision", "Coran", "Dhimmi", "Djihad", "Fatwa", 
                "Hadith", "Hadj", "Imam", "Islam", "Islamisme", 
                "Jérusalem", "Khomeyni", "Mahomet", "Médine", 
                "Mollah", "Mufti", "Musulman", "Piliers", "Prophète", 
                "Ramadan", "Soufisme", "Sourate", "Sunnisme", 
                "Taliban", "Tchador", "Wahhabisme", "Zakat",
                "Mosquée", "Minaret", "Salat", "Muezzin", "Halal", 
                "Haram", "Hijab", "Chahada", "Inshallah", "Subhanallah",
                "Jihadisme", "Salafisme", "Madrasa", "Burqa", "Fatiha",
                "Fatimide", "Fatiha", "Tawhid", "Khadija", "Sunna"
            ]

            resultats = detecte_mot_cle(messages, mots_cles)
            for resultat in resultats:
                output_file.write(f"Message : {resultat['message']}\n")
                output_file.write(f"Insulte : {resultat['insulte']}\n")
                output_file.write(f"Envoyé par : {resultat['envoye_par']}\n\n")

if __name__ == "__main__":
    main()
