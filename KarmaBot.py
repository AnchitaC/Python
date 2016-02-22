

import praw
import pprint
user_agent =('PyRed 3.5.1')
r = praw.Reddit(user_agent = user_agent)

thing_limit = 10
user_name = input("Please enter username: ")
user = r.get_redditor(user_name)


while True:
	if x == 'Yes' or x == 'YES' or x == 'yes':
		user = r.get_redditor(user_name)
		gen = user.get_submitted(limit = thing_limit)
		karma = {}
		for thing in gen:
			subreddit = thing.subreddit.display_name
			karma[subreddit] = (karma.get(subreddit, 0) + thing.score)

		pprint.pprint(karma)
	elif:
		user_name = input("Please enter the correct username! ")
		x = input("Is this the correct username: ")
	else:
		a = input("Would you like to continue? ")
		if a == 'yes' or a == 'Yes':
			pass
		else:
			break
