__author__ = 'adelli'


rockList = ['aybcddez','baccdyz', 'zeyebabg', 'mtprazb']

def getGems (rockList=[]):
    if rockList == []: return set(list(map(chr, range(97, 123))))
    else: return set(rockList[0]) & getGems(rockList[1:])

print('the number of gems is {}'.format(len(getGems(rockList))))

