import numpy as np
import itertools as it

max_doors = 3

def simulate_prizedoor(nsim):
	return np.random.randint(max_doors,size=nsim)

def simulate_guess(nsim):
	return np.zeros(nsim,dtype = np.int)

def diff_door(prizes,guesses):
	r = range(max_doors)
	response = []	
	for p,g in it.izip(prizes,guesses):
		diff = list(set(r)-set([p,g]))
		choice = np.random.choice(diff,1)[0]
		response.append(choice)
	return response

def win_percentage(guesses, prizedoors):
	return 100* (guesses == prizedoors).mean()

nsim  = 10000;

prizes = simulate_prizedoor(nsim)
guess =  simulate_guess(nsim)

print "Win percentage when keeping original door ", win_percentage(guess,prizes) 

goats =  diff_door(prizes,guess)
change = diff_door(guess,goats)

print "Win percentage when switching doors", win_percentage(change,prizes)
