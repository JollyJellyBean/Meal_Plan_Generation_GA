#################################################################
#                                                               
# Copyright 2019 All rights reserved.                           
# Author: David Cheng                                         
#                                  
#                                                               
#################################################################
import random

# INPUT: parents - Parents chosen by the selection function
#        options - Options created from OPTIMOPTIONS
#		 nvars - Number of variables 
#		 fitness - Fitness function 
#		 score - Vector of scores of the current population 
#		 population - Matrix of individuals in the current population
# OUTPUT:	crosschild - list with new offspring
# DESCRIPTION:  Combines the genetic information of two parents to generate new offspring.
def crossover(parents, options, nvars, fitness, score, population);
	nChild = length(parents)/2;
	crosschild = []
	index = 1;

		for i = 1:nChild
			parent1 = population[parents(index)];
			parent2 = population[parents(random.randint(len(parents)))];
			index = index + 2;
			 
			p1 = ceil((length(parent1) -1) * random.randint(0,1));
			p2 = p1 + 1;
			child = [parent1(1:p1), parent2(p2:8)];
			crosschild[i] = child;

	return crosschild


