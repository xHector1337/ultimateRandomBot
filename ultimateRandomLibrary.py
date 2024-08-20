import requests
valid_languagesWORDS = ["zh", "en", "fr", "es", "it", "de"]
def randomWord(count=1,lang="en"):
    if lang not in valid_languagesWORDS:
        print("Available languages are zh,en,fr,es,it and de.")
        return
    req = ""
    if count == 1:
        req = requests.get(f"https://random-word-api.herokuapp.com/word?lang={lang}")
    elif count > 1:
        req = requests.get(f"https://random-word-api.herokuapp.com/word?lang={lang}&number={count}")
    else:
        print("randomWord function error occured.")    
    return req.text.replace('"',"").replace("[","").replace("]","").replace(","," ")
def randomWordAll(lang="en"):
    if lang not in valid_languagesWORDS:
        print("Avaliable languages are:\n",valid_languagesWORDS)
        return
    print("This might take some time...")
    req = requests.get(f"https://random-word-api.herokuapp.com/all?lang={lang}")
    return req.text.replace('"',"").replace("[","").replace("]","").replace(","," ")
valid_languagesJokes = ["en","cs","de","es","fr","pt"]
def randomJoke(lang="en"):
    if lang not in valid_languagesJokes:
        print("Available languages are:\n",valid_languagesJokes)
        return
    req = requests.get(f"https://v2.jokeapi.dev/joke/Any?lang={lang}&format=txt")
    return req.text
valid_languagesFacts = ["en","de"]
def randomFunFact(lang="en"):
    if lang not in valid_languagesFacts:
        print("Available languages are:\n",valid_languagesFacts)
        return
    req = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/random?language={lang}")
    return req.json()["text"]
def randomTechyQuote():
    req = requests.get(f"https://techy-api.vercel.app/api/text")
    return req.text
def randomChuckNorrisJoke():
    req = requests.get("https://api.chucknorris.io/jokes/random")
    return req.json()["value"]
def randomExcuse():
    req = requests.get(f"https://excuser-three.vercel.app/v1/excuse")
    return req.json()[0]["excuse"]
def randomYoMammaJoke():
    req = requests.get("https://www.yomama-jokes.com/api/v1/jokes/random/")
    return req.json()["joke"]
def randomDadJoke():
    req = requests.get("https://icanhazdadjoke.com/",headers={"Accept": "text/plain"})
    return req.text
