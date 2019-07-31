#################################################################
#                                                               
# Copyright 2019 All rights reserved.                           
# Author: David Cheng                                         
#                                  
#                                                               
#################################################################
import pandas 
import numpy


	
# INPUT: population_df - Population dataframe of meals to be evaluated for fitness
#        MEAL_DATA - dataframe of the meals with nutritional information
#        RECOMMENDED_DATA - Array of the recommended nutritional information [Carb, Protein, Fat]
# OUTPUT: fitness - Fitness evaluation for the given population_df where higher fitness is desirable
# DESCRIPTION:  Evaluates fitness based on the differences from the individual meal and recommended daily nutritional intake of protein, carbohydrates, and fats
def fitness_value(population_df, RECOMMENDED_DATA):

    for row in range(population_df.shape[0]):

        meal_df = population_df.iloc[:,[16,17,18]]

        carb_fitness = abs(meal_df.loc[:, 'Carbohydrates'] - RECOMMENDED_DATA[0])/RECOMMENDED_DATA[0] # Carbohydrate percent Difference from recommended
        protein_fitness =  abs(meal_df.loc[:,'Protein'] - RECOMMENDED_DATA[1])/RECOMMENDED_DATA[1] # Protein percent Difference from recommended
        fat_fitness = abs(meal_df.loc[:,'Fat'] - RECOMMENDED_DATA[2])/RECOMMENDED_DATA[2] # Fat percent Difference from recommended

        fitness_df = pandas.DataFrame(carb_fitness).join(protein_fitness).join(fat_fitness)

        fitness_df['Sum'] = fitness_df.iloc[:,0]+fitness_df.iloc[:,1]+fitness_df.iloc[:,2]

        fitness_df['Inverse'] = 1/fitness_df.loc[:,'Sum'] # return inverse for optimization function to find max

        population_df['Fitness'] = fitness_df["Inverse"]

    return population_df


