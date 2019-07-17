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
#        RECOMMENDED_DATA - Dataframe of the recommended nutritional infromation
# OUTPUT: fitness - Fitness evaluation for the given population_df where higher fitness is desirable
# DESCRIPTION:  Evaluates fitness based on the differences from the individual meal and recommended daily nutritional intake of protein, carbohydrates, and fats
def fitness_value(population_df, MEAL_DATA, RECOMMENDED_DATA)
	
    for row in range(1:population_df.shape[0]):
	    fitness = 0;
		sum = zeros(1,11); # protein carb cost e
		meal = population_df.iloc[row,:]
        length = population_df.Series.nonzero();

        for i in range(1:length):
            for k in range(1:11):
                sum(k) = sum(k) + MEAL_DATA(p(i),k);
				
        for row in range(1:3)		# (protein, carbohydrates, fats)
            fitness = fitness + abs(RECOMMENDED_DATA(i)-sum(i+1))/RECOMMENDED_DATA(i);
			
        fitness = fitness + sum(10)*0.05 + sum(11)*0.05;
		
        fitness(j) = 1/fitness; # return inverse for optimization function to find max
	
	return fitness


