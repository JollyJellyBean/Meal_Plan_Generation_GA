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
        print('Iteration',i)
        #Mutate (Sid)


        #Evaluate Fitness of each chromosome(Sid)


        #Select Parents (Jake)

        #Create new offspring, Crossover (Dave)



if __name__ == '__main__':
    main()
