import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile) as f:
    cases = f.readlines()
cases = [x.strip('\n') for x in cases]

T = int(cases[0]) + 1
happySide = '+'
blankSide = '-'

def flip(pancake):
	if(pancake == happySide):
		return blankSide
	elif(pancake == blankSide):
		return happySide

with open(outputFile, 'w+') as out:
	for i in xrange(1, T):
		case 	 = cases[i].split(' ')
		pancakes = list(case[0])
		K 		 = int(case[1])
		nflips 	 = 0

		if(not(blankSide in pancakes)):
			out.write("Case #" + str(i) + ": " + str(nflips) + "\n")
		else:
			for j in xrange(0, len(pancakes)):
				if(pancakes[j] == blankSide):
					if(j + K > len(pancakes)):
						out.write("Case #" + str(i) + ": " + "IMPOSSIBLE\n")
						break
					else:
						for n in xrange(j, j + K):
							pancakes[n] = flip(pancakes[n])
						j += 1
						nflips += 1
						if(not(blankSide in pancakes)):
							out.write("Case #" + str(i) + ": " + str(nflips) + "\n")
							nflips = 0
							break



