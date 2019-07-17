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
import crossover

def printstage(value):
    print('+------------------------------------------------------------+')
    print(value)
    print('+------------------------------------------------------------+')
    print('')

def main():
	LOCAL_DIR = './'
	DB_DIR = LOCAL_DIR + 'Database/FoodDB.csv'
	Population_Number = 10
	RECOMMENDED_DATA = [130,56,60] # [Carb, Protein, Fat] 19-30 year old man based off 1600 cal diet 

	#Import Database
	printstage('Importing Database')
	Food_DF = DatabaseHelper.import_DB(DB_DIR) #(Sid Implement Cleanup)

	#Initialize Population
	printstage('Intializing Population')
	Population_DF = GAOperators.initPop(Food_DF,Population_Number)

	printstage('Completing GA')
    for i in range(2):
		Population_DF = GAOperators.mutate(population_Df)

		#Evaluate Fitness of each chromosome
		fit_vals = fitness.fitness.value(population_df, Food_DF, RECOMMENDED_DATA)

		#Select Parents (Jake)
		Population_DF = GAOperators.Select_Parents(Population_DF, Population_Number)

        #Mutate (Sid)
        Population_DF = GAOperators.mutate(Population_DF,Food_DF)

        #Evaluate Fitness of each chromosome(Sid)


        #Select Parents (Jake)
        Population_DF = GAOperators.Select_Parents(Population_DF,Population_Number)
        print(Population_DF)

		print(Population_DF)

		#Create new offspring, Crossover 
		child = crossover.crossover_child(parents, options, nvars, fitness, score, Population_DF)


if __name__ == '__main__':
	main()
