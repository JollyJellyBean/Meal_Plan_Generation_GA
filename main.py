#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                  #
#                                                               #
#################################################################

import pandas as pd
import GAOperators

def printstage(value):
    print('+------------------------------------------------------------+')
    print(value)
    print('+------------------------------------------------------------+')


def main():
    LOCAL_DIR = './'
    DB_DIR = LOCAL_DIR + 'Database/FoodDB.csv'


    #Import Database
    printstage('Importing Database')
    print('importing From:', DB_DIR)
    Food_DF = pd.read_csv(DB_DIR)
    Food_DF.loc[-1] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # adding a row for NULL case
    Food_DF.index = Food_DF.index + 1  # shifting index

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
