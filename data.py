import time
i = {'timePlayed': 0, 'blocksConquered': 0, 'deaths': 0, 'ballsDestructed': 0,
		'lastUnlockedStages': 10, 'theme':0,
		#achievements
		'doubleKill': 0, 'worldEmperor': 0, 'yogaMaster': 0,
		#settings
		'musicVolume': 100, 'effectsVolume':100}


startTime = 0
def getActualTime():
	return int(time.mktime(time.localtime( )) - startTime)
