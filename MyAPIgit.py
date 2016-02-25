import requests

name = input("Please enter your summoner name: ")
region = input("Please enter the region in which you play: ").lower()
apikey = "apikey"
 
def SummonersData(name, region, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + name + "?api_key=" + apikey
	r = requests.get(url)
	return r.json()

def RankedData(region, ID, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + apikey
	r = requests.get(url)
	return r.json()

def main():
	rJSON = SummonersData(name, region, apikey)
	ID = rJSON[name.lower()]['id']
	ID = str(ID)
	rJSON1 = RankedData(region, ID, apikey)
	division = rJSON1[ID][0]['tier']
	print("Your summoner name is: " + name + " and your region is: " + region.upper() + ".")
	print("Your tier is: " + division[0] + division.lower()[1:] + " and you are in division " + rJSON1[ID][0]['entries'][0]['division'] + " with " + str(rJSON1[ID][0]['entries'][0]['leaguePoints']) + " points.")

if __name__ == "__main__":
	main()
