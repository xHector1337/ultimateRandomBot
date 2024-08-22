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
