import requests
import random

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
def randomActivity():
    req = requests.get("https://bored-api.appbrewery.com/random")
    return req.json()["activity"]
def randomFoxImage():
    req = requests.get("https://randomfox.ca/floof/")
    return req.json()["image"]
def randomDogImage():
    req = requests.get("https://random.dog/woof.json")
    return req.json()["url"]
def randomDuckImage():
    req = requests.get("https://random-d.uk/api/random")
    return req.json()["url"]
def randomCatFact():
    req = requests.get("https://meowfacts.herokuapp.com/")
    return req.json()["data"][0]
def randomDogFact():
    req = requests.get("https://dog-api.kinduff.com/api/facts")
    return req.json()["facts"][0]
def randomCoffeeImage():
    req = requests.get("https://coffee.alexflipnote.dev/random.json")
    return req.json()["file"]
def randomQuote():
    req = requests.get("https://zenquotes.io/api/random")
    quote = f"{req.json()[0]['q']} {req.json()[0]['a']}"
    return quote
def randomNumber():
    return random.randint(0,9999999999999999999999999)
def randomCommitMessage():
    req = requests.get("https://whatthecommit.com/index.txt")
    return req.text
def randomPersonWhoDoesntExist():
    req = requests.get("https://thispersondoesnotexist.com/")
    return req.content
def randomPersonIdentity():
    req = requests.get("https://randomuser.me/api/")
    person_data = req.json()["results"][0]
    person = (
        f'{person_data["name"]["first"]} {person_data["name"]["last"]}\n'
        f'Location: {person_data["location"]["country"]}\n'
        f'Age: {person_data["dob"]["age"]}\n'
        f'Email: {person_data["email"]}\n'
        f'Username: {person_data["login"]["username"]}\n'
        f'Password: {person_data["login"]["password"]}'
    )
    return person
def randomYesOrNo():
    if random.randint(0,100) > 50:
        return "yes"
    else:
        return "no"
def randomHour():
    hour = random.randint(0,24)
    minute = random.randint(0,59)
    if hour > 9 and minute > 9:
        return f"{hour}:{minute}"
    elif hour < 10 and minute > 9:
        return f"0{hour}:{minute}"
    elif hour < 10 and minute < 10:
        return f"0{hour}:0{minute}"
    elif hour > 9 and minute < 10:
        return f"{hour}:0{minute}"
    else:
        return f"{hour}:{minute}"
def randomLetter():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if random.randint(0,100) > 50:
        return random.choice(letters).upper()
    else:
        return random.choice(letters)
def randomCountry():
    req = requests.get("https://restcountries.com/v3.1/all")
    countries = [""]
    for i in req.json():
        countries.append(i["name"]["common"])
    return random.choice(countries)
def randomRegion():
    regions = ["Africa","Europe","Asia","Antarctica","North America","South America","Australia"]
    return random.choice(regions)
def randomImage(width=200,height=300):
    req = requests.get(f"https://picsum.photos/{width}/{height}")
    return req.url
                        
