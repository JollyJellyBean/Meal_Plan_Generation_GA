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
    LOCAL_DIR = '/Users/Jake_Mawdsley/PycharmProjects/Meal_Plan_Generation_GA/'
    DB_DIR = LOCAL_DIR + 'Database/FoodDB.csv'


    #Import Database
    printstage('Importing Database')
    Food_DF = DatabaseHelper.import_DB(DB_DIR) #(Sid Implement Cleanup)


    #Initialize Population
    printstage('Intializing Population')
    Parent_Population_DF = GAOperators.initPop(Food_DF,100)
    print(Parent_Population_DF)

    printstage('Completing GA')
    for i in range(100):
        x=1

        #Evaluate Fitness of each chromosome(Sid)


        #Mutate (Sid)


        #Select Parents (Jake)


        #Create new offspring, Crossover (Dave)



if __name__ == '__main__':
    main()
