#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                  #
#                                                               #
#################################################################

import GAOperators
import DatabaseHelper

def printstage(value):
    print('+------------------------------------------------------------+')
    print(value)
    print('+------------------------------------------------------------+')
    print('')



def main():
    LOCAL_DIR = './'
    DB_DIR = LOCAL_DIR + 'Database/FoodDB.csv'
    Population_Number = 10


    #Import Database
    printstage('Importing Database')
    Food_DF = DatabaseHelper.import_DB(DB_DIR) #(Sid Implement Cleanup)


    #Initialize Population
    printstage('Intializing Population')
    Population_DF = GAOperators.initPop(Food_DF,Population_Number)

    printstage('Completing GA')
    for i in range(2):

        #Mutate (Sid)
        Population_DF = GAOperators.mutate(Population_DF)

        #Evaluate Fitness of each chromosome(Sid)


        #Select Parents (Jake)
        Population_DF = GAOperators.Select_Parents(Population_DF,Population_Number)
        print(Population_DF)

        #Create new offspring, Crossover (Dave)



if __name__ == '__main__':
    main()
