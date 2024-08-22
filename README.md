Ultimate Random Bot is a randomizer discord bot that has its own library. It uses a couple of APIs to fetch random data such as random cat and dog images, fun facts etc.

# Discord Bot

## Installation of Discord Bot

After cloning or downloading the repository, install all dependencies by typing either `pip install -r requirements.txt` or `python -m pip install -r requirements.txt` on the command line.
Then edit `settings.json` with a text editor to add your Discord bot token. Finally, run your bot by either typing `python ultimateRandomBot.py` or executing `ultimateRandomBot.py` with Python.
Congratulations, now your bot is active and ready to go.

## Command List of Discord Bot

Default prefix is **?**.

+ ?help --> Sends full list of commands as a message.

+ ?randomword <(optional) number> <(optional) language> --> Uses `https://random-word-api.herokuapp.com/` API to get random words in the language you pass as argument.
  If you use it without any parameters, it returns a word in English.

+ ?randomjoke <(optional) language> --> Uses `https://v2.jokeapi.dev/joke/` API to get a random joke in the language you pass as argument.
  If you use it without any parameters, it returns a joke in English.

+ ?randomfact <(optional) language> --> Uses `"https://uselessfacts.jsph.pl/api/v2/facts/random` API to get a random fun fact in the language you pass as argument.
  If you use it without any parameters, it returns a fun fact in English.

+ ?randomtechyquote --> Uses `https://techy-api.vercel.app/api/text` API to get a random techy quote.

+ ?randomchucknorrisjoke --> Uses `https://api.chucknorris.io/jokes/random` API to get a random Chuck Norris joke.

+ ?randomexcuse --> Uses `https://excuser-three.vercel.app/v1/excuse` API to get a random excuse.

+ ?randomyomammajoke --> Uses `https://www.yomama-jokes.com/api/v1/jokes/random/` API to get a random Yo Mamma joke.

+ ?randomdadjoke --> Uses `https://icanhazdadjoke.com/` API to get a random dad joke.

+ ?randomactivity --> Uses `https://bored-api.appbrewery.com/random` API to get a random activity idea.

+ ?randomfoximg --> Uses `https://randomfox.ca/floof/` API to get a random fox image.

+ ?randomdogimg --> Uses `https://random.dog/woof.json` API to get a random dog image.

+ ?randomcatimg --> Uses `https://api.thecatapi.com/v1/images/search` API to get a random cat image.

+ ?randomduckimg --> Uses `https://random-d.uk/api/random` API to get a random duck image.

+ ?randomraccoonimg --> Uses `https://api.racc.lol/v1/raccoon` API to get a random raccoon image.

+ ?randomcatfact --> Uses `https://meowfacts.herokuapp.com/` API to get a random cat fact.

+ ?randomdogfact --> Uses `https://dog-api.kinduff.com/api/facts` API to get a random dog fact.               

+ ?randomcoffeeimg --> Uses `https://coffee.alexflipnote.dev/random.json` API to get a random coffee image.

+ ?randomquote --> Uses `https://zenquotes.io/api/random` API to get a random quote.

+ ?randomnumber --> Returns a random number.

+ ?randomcommitmessage --> Uses `https://whatthecommit.com/index.txt` API to get a random Git commit message.

+ ?randompersonwhodoesntexist --> Uses `https://thispersondoesnotexist.com/` API to get a photo of a random person who doesn't exist.

+ ?randomidentity --> Uses `https://randomuser.me/api/` API to get a random identity.

+ ?yesorno --> Returns yes or no randomly.

+ ?randomhour --> Returns randomly generated time in hour. (11:44 as example)

+ ?randomletter --> Returns a random letter from English alphabet.

+ ?randomcountry --> Uses `https://restcountries.com/v3.1/all` API to return a random country.

+ ?randomregion --> Returns a random region from the seven regions.

+ ?randomimg <(optional) width> <(optional) height> --> Uses `https://picsum.photos/` API to get a random image. If don't pass any arguments, it gets a random image of 200x300.               

+ ?randomcolour <(optional type> --> Uses `https://x-colors.yurace.pro/api/random` API to get a random image. If you don't pass any type as argument, it returns the colour in hex.

# Ultimate Random Library

## Installation

After cloning or downloading the repository, you can start using the library by downloading dependencies.
If you are not going to use the Discord bot you don't need to download `discord.py` dependency. Only `requests` is enough.

## List of Functions

+ randomWord(count=1,lang="en") --> If language is available in languages list. It returns random words in the language you passed as much as the count argument.
  Available languages are "zh", "en", "fr", "es", "it", "de". It uses `https://random-word-api.herokuapp.com/word` API.

+ randomWordAll(lang="en") --> If language is available in the languages list, returns all of the words in `https://random-word-api.herokuapp.com/word` API database.
 Available languages are "zh", "en", "fr", "es", "it", "de".

+ randomJoke(lang="en) --> If language is available in languages list, returns a joke from `https://v2.jokeapi.dev/joke/Any` API. Available languages are "en","cs","de","es","fr","pt".

+ randomFunFact(lang="en") --> If language is available in languages list, returns a random fun fact from `https://uselessfacts.jsph.pl/api/v2/facts/random` API. Available languages are "en","de".

+ randomTechyQuote() --> Returns a random techy quote from `https://techy-api.vercel.app/api/text` API.

+ randomChuckNorrisJoke() --> Returns a random Chuck Norris Joke from `https://api.chucknorris.io/jokes/random` API.

+ randomExcuse() --> Returns a random excuse from `https://excuser-three.vercel.app/v1/excuse` API.

+ randomYoMammaJoke() --> Returns a random Yo Mamma joke from `https://www.yomama-jokes.com/api/v1/jokes/random/` API.

+ randomDadJoke() --> Returns a random dad joke from `https://icanhazdadjoke.com/` API.

+ randomActivity() --> Returns a random activity from `https://bored-api.appbrewery.com/random` API.

+ randomFoxImage() --> Returns a random fox image url from `https://randomfox.ca/floof/` API.

+ randomDogImage() --> Returns a random dog image url from `https://random.dog/woof.json` API.

+ randomCatImage() --> Returns a random cat image url from `https://api.thecatapi.com/v1/images/search` API.

+ randomDuckImage() --> Returns a random duck image url from `https://random-d.uk/api/random` API.

+ randomRaccoonImage() --> Returns a random raccoon image url from `https://api.racc.lol/v1/raccoon` API.
               
+ randomCatFact() --> Returns a random fact about cats from `https://meowfacts.herokuapp.com/` API.

+ randomDogFact() --> Returns a random fact about dogs from `https://dog-api.kinduff.com/api/facts` API.

+ randomCoffeeImage() --> Returns a random coffee image url from `ttps://coffee.alexflipnote.dev/random.json` API.

+ randomQuote() --> Returns a random quote from `https://zenquotes.io/api/random` API.

+ randomNumber() --> Returns a number between 0 and 9999999999999999999999999.

+ randomCommitMessage() --> Returns a random Git commit message from `https://whatthecommit.com/index.txt` API.

+ randomPersonWhoDoesntExist --> Returns a random person's image who doesn't exist in bytes from `https://thispersondoesnotexist.com/` API.

+ randomPersonIdentity --> Returns a random person identity from `https://randomuser.me/api/` API. It includes a random name and surname, random location, age, email, username and password. Of course all of these are randomly generated.

+ randomYesOrNo() --> Returns yes or no.

+ randomHour() --> It returns a randomly generated time in hour. (Example: 05:44)

+ randomLetter() --> Returns a random letter from English alphabet.

+ randomCountry() --> Returns a random country from `https://restcountries.com/v3.1/all` API.

+ randomRegion() --> Returns a random region from the seveb regions.

+ randomImage(width=200,height=300) --> Returns a random image url according to weidth and height you pass as arguments. It uses `https://picsum.photos/` API.

+ randomColour(type="hex") --> Returns a random colour in the type you pass as argument. It uses `https://x-colors.yurace.pro/api/random` API.
  Available types are "hex","rgb","hsl".

# Last Words

All API credits go to their dear owners. I do not own any of them. If you find any bugs or mistakes in my project, please feel free to contact me.
Happy coding!
