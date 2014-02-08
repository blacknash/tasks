import numpy as np
import itertools as it

max_doors = 3

def simulate_prizedoor(nsim):
	return np.random.randint(max_doors,size=nsim)

def simulate_guess(nsim):
	return np.zeros(nsim,dtype = np.int)

def goat_door(prizes,guesses):
	result = np.random.randint(0, 3, prizes.size)
    	while True:
        	bad = (result == prizes) | (result == guesses)
        	if not bad.any():
            		return result
        	result[bad] = np.random.randint(0, 3, bad.sum())

#def switch_guess(prizes,guesses):
#	r = range(max_doors)
#	response = []	
#	for p,g in it.izip(prizes,guesses):
#		diff = list(set(r)-set([p,g]))
#		choice = np.random.choice(diff,1)[0]
#		response.append(choice)
#	return response

def switch_guess(guesses, goatdoors):
    result = np.zeros(guesses.size)
    switch = {(0, 1): 2, (0, 2): 1, (1, 0): 2, (1, 2): 1, (2, 0): 1, (2, 1): 0}
    for i in [0, 1, 2]:
        for j in [0, 1, 2]:
            mask = (guesses == i) & (goatdoors == j)
            if not mask.any():
                continue
            result = np.where(mask, np.ones_like(result) * switch[(i, j)], result)
    return result

def win_percentage(guesses, prizedoors):
	return 100* (guesses == prizedoors).mean()

nsim  = 10000;

prizes = simulate_prizedoor(nsim)
guess =  simulate_guess(nsim)

print "Win percentage when keeping original door ", win_percentage(guess,prizes) 

goats =  goat_door(prizes,guess)
change = switch_guess(guess,goats)

print "Win percentage when switching doors", win_percentage(change,prizes)
