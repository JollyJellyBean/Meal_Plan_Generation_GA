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
	POPULATION_NUMBER = 100
	RECOMMENDED_DATA = [384,154,102] # [Carb, Protein, Fat] 19-30 year old man based off bulking diet

	# Import Database and cleanup
	printstage('importing From:' + DB_DIR)
	CLEAN_FOOD_DF = pd.read_csv(DB_DIR)
	printstage('Preprocessing' + DB_DIR)

	# Initialize Population
	printstage('Intializing Population')
	population_df = GAOperators.initPop(CLEAN_FOOD_DF, POPULATION_NUMBER) # Population of different meals and associated nutritional values
	population_df = fitness.fitness_value(population_df, RECOMMENDED_DATA)
	testing_results_tot = pd.DataFrame({"Max":[],"Total Fitness":[]})

	population_df.to_csv(LOCAL_DIR + 'InitPop.csv')


	testing_results_tot = pd.DataFrame({"Food0":[],"Food1":[],"Food2":[],"Food3":[],"Food4":[],"Food5":[],"Food6":[],"Food7":[],"Food8":[],"Food9":[],"Food10":[],"Food11":[],"Food12":[],"Food13":[],"Food14":[],"Food15":[],"Total Fitness":[]})


	# Generational GA Algorithm
	printstage('Completing GA')
	for i in range(20):

		# Mutate
		population_df = GAOperators.mutate(population_df, CLEAN_FOOD_DF,i)

		# Update Total Carbs, Protein and Fats
		population_df = GAOperators.update_Foodplan(CLEAN_FOOD_DF,population_df)

		# Evaluate Fitness of each chromosome and attach fit function to df
		population_df = fitness.fitness_value(population_df, RECOMMENDED_DATA)

		# Select Parents
		population_df = GAOperators.Select_Parents(population_df, POPULATION_NUMBER)

		# Create new offspring, Crossover
		population_df = GAOperators.crossover(population_df)

		# testing_results = pd.DataFrame({"Food0":population_df['Food0'].nunique(),"Food1":population_df['Food1'].nunique(),"Food2":population_df['Food2'].nunique(),"Food3":population_df['Food3'].nunique(),"Food4":population_df['Food4'].nunique(),"Food5":population_df['Food5'].nunique(),"Food6":population_df['Food6'].nunique(),"Food7":population_df['Food7'].nunique(),"Food8":population_df['Food8'].nunique(),"Food9":population_df['Food9'].nunique(),"Food10":population_df['Food10'].nunique(),"Food11":population_df['Food11'].nunique(),"Food12":population_df['Food12'].nunique(),"Food13":population_df['Food13'].nunique(),"Food14":population_df['Food14'].nunique(),"Food15":population_df['Food15'].nunique(),"Total Fitness":[population_df['Fitness'].sum()]})
		# testing_results_tot = testing_results_tot.append(testing_results)
		print('Max of Generation'+str(i),': ',population_df['Fitness'].max())


	#testing_results_tot.to_csv(LOCAL_DIR + 'testresults.csv')
	printstage('Finished GA ')

	#DatabaseHelper.print_fooditems(CLEAN_FOOD_DF,population_df,population_df['Fitness'].idxmax())
	print('Total Carbs: ',population_df.loc[population_df['Fitness'].idxmax(),'Carbohydrates'])
	print('Total Protein: ',population_df.loc[population_df['Fitness'].idxmax(),'Protein'])
	print('Total Fats: ',population_df.loc[population_df['Fitness'].idxmax(),'Fat'])


if __name__ == '__main__':
	main()
