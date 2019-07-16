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


    #Import Database
    printstage('Importing Database')
    Food_DF = DatabaseHelper.import_DB(DB_DIR)


    #Initialize Population
    printstage('Intializing Population')
    Parent_Population_DF = GAOperators.initPop(Food_DF,100)
    print(Parent_Population_DF)

    printstage('Completing GA')
    for i in range(100):
        x=1

        #Evaluate Fitness of each chromosome


        #Mutate


        #Select Parents


        #Create new offspring



if __name__ == '__main__':
    main()
