import requests

def imbored():
	data = requests.get('https://www.boredapi.com/api/activity/').json()
	if data["price"] < 0.5:
		price = 'and is not too expensive'
	else:
		price = 'and is a bit expensive'
	return "I'm bored too, let's do this: " + data["activity"] + ". It's " + data["type"] + " and you could involve " + str(data["participants"]) + " people " + price
