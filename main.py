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
import pandas as pd
# import crossover

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

	# Import Database and cleanup
	printstage('importing From:' + DB_DIR)
	FOOD_DF = pd.read_csv(DB_DIR)
	printstage('Preprocessing' + DB_DIR)
	CLEAN_FOOD_DF = DatabaseHelper.preprocess_DB(FOOD_DF)

	# Initialize Population
	printstage('Intializing Population')
	population_df = GAOperators.initPop(CLEAN_FOOD_DF, POPULATION_NUMBER) # Population of different meals and associated nutritional values

	printstage('Completing GA')
	for i in range(2):

		# Mutate
		printstage('Mutating chromosomes of generation ' + str(i))
		population_df = GAOperators.mutate(population_df, CLEAN_FOOD_DF)

		# Evaluate Fitness of each chromosome and attach fit function to df
		printstage('Evaluating fitness of generation ' + str(i))
		population_df = fitness.fitness_value(population_df, RECOMMENDED_DATA)

		# Select Parents
		population_df = GAOperators.Select_Parents(population_df, POPULATION_NUMBER)

		# Create new offspring, Crossover
		# child = crossover.crossover_child(parents, options, nvars, fitness, score, population_df)


if __name__ == '__main__':
	main()
