import requests
import Champions
import pprint
import Summs
import Items


name = input("Please enter your summoner name: ")
region = input("Please enter the region in which you play: ").lower()
apikey = "Insert your API Key"
 
def SummonersData(name, region, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + name + "?api_key=" + apikey
	r = requests.get(url)
	return r.json()

def RankedData(region, ID, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + apikey
	r = requests.get(url)
	return r.json()

def RankedSolo(region, ID, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.2/matchlist/by-summoner/" + ID + "?rankedQueues=RANKED_SOLO_5x5&seasons=SEASON2015&api_key=" + apikey
	r = requests.get(url)
	return r.json()

def RecentGames(region, ID, apikey):
	url = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.3/game/by-summoner/" + ID +  "/recent?api_key=" + apikey
	r = requests.get(url)
	return r.json()

def main():
	rJSON = SummonersData(name, region, apikey)
	ID = str(rJSON[name.lower()]['id'])

	rJSON1 = RankedData(region, ID, apikey)
	rJSON2 = RankedSolo(region, ID, apikey)
	rJSON3 = RecentGames(region, ID, apikey)

	division = rJSON1[ID][0]['tier']
	champs = Champions.champs.get('data')
	minions = rJSON3['games'][0]['stats']['minionsKilled']	
	level = rJSON3['games'][0]['stats']['level']
	win = rJSON3['games'][0]['stats']['win']
	assists = rJSON3['games'][0]['stats']['assists']
	deaths = rJSON3['games'][0]['stats']['numDeaths']
	kills = rJSON3['games'][0]['stats']['championsKilled']
	ip = rJSON3['games'][0]['ipEarned']
	spells = Summs.spells.get('data')	
	print("Your are in "  +   division[0] + division.lower()[1:] + " " +  rJSON1[ID][0]['entries'][0]['division'] + " with " + str(rJSON1[ID][0]['entries'][0]['leaguePoints']) + " points.")
	
	x  = input("How many matches do you want to see history for: ")
	for i in range(0,int(x)):
		print("Match " + str(i + 1) + " stats:")
		for champion in champs:
			if champs.get(champion).get('id') == rJSON3['games'][i]['championId']:
				print("\n" + "Champion played: "  + champion)
			else:
				pass
		
		for summs in spells:
			if spells.get(summs).get('id') == rJSON3['games'][i]['spell1']:
				print("Summoner spell #1: " + spells.get(summs).get('name'))
			else:

				pass
		for summs in spells:
			if spells.get(summs).get('id') == rJSON3['games'][i]['spell2']:
				print("Summoner spell #2: " + spells.get(summs).get('name'))		
	
		print("Level " + str(rJSON3['games'][i]['stats']['level']) + "\n" + str(rJSON3['games'][i]['stats']['minionsKilled']) + " minions " + "\n" +  "KDA: " + str(rJSON3['games'][i]['stats']['championsKilled']) + "/" + str(rJSON3['games'][i]['stats']['numDeaths']) + "/" + str(rJSON3['games'][i]['stats']['assists']) + ".")
		print(str(rJSON3['games'][i]['stats']['goldEarned']) + " gold earned.")
		if win:
			print("Game Won" + "\n" +  str(rJSON3['games'][i]['ipEarned']) + " IP." +"\n ")
		else:
			print("Game Lost" + "\n"  + str(rJSON3['games'][i]['ipEarned']) + " IP." + "\n")
		


if __name__ == "__main__":
	main()
