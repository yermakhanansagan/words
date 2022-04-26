import math
import random
from dna import DNA

class Population(object):
	
	def __init__(self, p, m, num):

		self.population = []
		self.matingPool = []
		self.generations = 0
		self.finished = False
		self.target = p
		self.mutationRate = m
		self.perfectScore = 1

		self.best = ""

		for x in range(num):
			self.population.append(DNA(len(self.target)))

		self.calcFitness()
		
	def calcFitness(self):
		for i in range(len(self.population)):
			self.population[i].calcFitness(self.target)

	def naturalSelection(self):

		self.matingPool = [] # clear the list

		self.maxFitness = 0.0
		for i in range(len(self.population)):
			if self.population[i].fitness > self.maxFitness:
				self.maxFitness = self.population[i].fitness

		for x in range(len(self.population)):
			fitness = self.population[x].fitness/self.maxFitness
			n = math.floor(fitness * 100)
			for i in range(n):
				self.matingPool.append(self.population[x])

	def generate(self):
		for i in range(len(self.population)):
			partnerA = random.choice(self.matingPool)
			partnerB = random.choice(self.matingPool)
			child = partnerA.crossover(partnerB)
			child.mutate(self.mutationRate)
			self.population[i] = child
		self.generations+=1;

	def getBest(self):
		return self.best

	def evaluate(self):
		worldrecord = 0.0
		index = 0
		for x in range(len(self.population)):
			if self.population[x].fitness > worldrecord:
				index = x
				worldrecord = self.population[x].fitness

		self.best = self.population[index].getPhrase()
		if worldrecord == self.perfectScore:
			self.finished = True

	def isFinished(self):
		return self.finished

	def getGenerations(self):
		return self.generations

	def getAverageFitness(self):
		total = 0
		for i in range(len(self.population)):
			total = total + self.population[i].fitness

		return total / len(self.population)

	def allPhrases(self):
		everything = ""
		displayLimit = min(len(self.population),50)

		for i in range(displayLimit):
			everything = everything + self.population[i].getPhrase() + "\n"

		return everything