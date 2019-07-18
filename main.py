#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                  #
#                                                               #
#################################################################

import GAOperators
import DatabaseHelper
import fitness
#import crossover

def printstage(value):
    print('+------------------------------------------------------------+')
    print(value)
    print('+------------------------------------------------------------+')
    print('')

def main():
	LOCAL_DIR = './'
	DB_DIR = LOCAL_DIR + 'FoodDB.csv'
	POPULATION_NUMBER = 10
	RECOMMENDED_DATA = [130,56,60] # [Carb, Protein, Fat] 19-30 year old man based off 1600 cal diet

	#Import Database and cleanup
	printstage('Importing Database')
	FOOD_DF = DatabaseHelper.import_DB(DB_DIR)

	#Initialize Population
	printstage('Intializing Population')
	population_df = GAOperators.initPop(FOOD_DF, POPULATION_NUMBER) # Population of different meals and associated nutritional values

	printstage('Completing GA')
	for i in range(2):
		population_df = GAOperators.mutate(population_df,FOOD_DF)

		#Mutate
		population_df = GAOperators.mutate(population_df, FOOD_DF)

		#Evaluate Fitness of each chromosome and attach fit function to df
		population_df = fitness.fitness_value(population_df, FOOD_DF, RECOMMENDED_DATA)

		#Select Parents
		population_df = GAOperators.Select_Parents(population_df, POPULATION_NUMBER)
		print(population_df)

		#Create new offspring, Crossover
		# child = crossover.crossover_child(parents, options, nvars, fitness, score, population_df)


if __name__ == '__main__':
	main()
