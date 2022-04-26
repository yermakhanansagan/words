import string
import random
import math

def newChar():
	rus = "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
	return random.choice(rus+" .")

class DNA(object):
	
	def __init__(self, num):
		self.genes = []
		self.fitness = 0.0
		for i in range(num):
			self.genes.append(newChar())

	def getPhrase(self):
		return ''.join(self.genes)

	def calcFitness(self, target):
		score = 0.0
		for i in range(len(self.genes)):
			if self.genes[i] == target[i]:
				score+=1
		self.fitness = score / len(target)

	def crossover(self, partner):
		child = DNA(len(self.genes))

		midpoint = random.randint(1,len(self.genes)-1)

		child.genes = self.genes[0:midpoint] + partner.genes[midpoint:len(self.genes)]
		
		return child

	def mutate(self, mutationRate):
		for i in range(len(self.genes)):
			if random.random() < mutationRate:
				self.genes[i] = newChar()