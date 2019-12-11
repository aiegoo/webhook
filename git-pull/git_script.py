import schedule, time, os, git

# This is the name of the file that has search criterion  
repoList = "repo_list.txt"

# Read the repo_list file and return list of repositories in an iterable format
def getRepoPaths():
	rows = []
	# reading file 
	with open(repoList, "r") as ins:
		for line in ins:
			print(line)
			rows.append(line.strip())
	return rows

def performTask():
	r = getRepoPaths()
	for repo in r:
		gr = git.Repo(repo)
		o = gr.remotes.origin
		res = o.pull()
		for i in res:
			if(str(i.ref)=='origin/master'):
				print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) + '\n' + str(i.ref) + '\n' + gr.commit(i.commit).message + '\n\n')

# Setting up the run schedule
schedule.every(5).minutes.do(performTask) # Every 5 minutes

# Test schedule
# schedule.every().day.at("16:16").do(performTask) # Test

while True:
	schedule.run_pending()
	time.sleep(1)