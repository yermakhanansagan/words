from population import Population
from dna import DNA
import math

target = "Ермахан Ансаган и Нургалиев Олжас." # менять генерируемое слово здесь
popmax = 500
mutationRate = 0.01

population = Population(target, mutationRate, popmax)

def displayInfo():
	answer = population.getBest()

	statsText = "Количество генерации   " + str(population.getGenerations()) + "\n"
	statsText += "Cредняя годность   " + str(population.getAverageFitness()) + "\n"
	statsText += "Общая численность потомков   " + str(popmax) + "\n"
	statsText += "Скорость мутации   " + str(mutationRate *100) + "%\n"
	print("Все слова: " + population.allPhrases())
	print(statsText)
	print("Лучший ответ: " + answer + "\n")

while True:
	
	population.naturalSelection()

	population.generate()

	population.calcFitness()

	population.evaluate()

	displayInfo()

	if population.isFinished():
		break


