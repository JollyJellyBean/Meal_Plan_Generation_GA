#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                    #
#                                                               #
#################################################################


# INPUT: - dirty_df:
#        - Parents:
# OUTPUT: -clean_df
# DESCRIPTION:
def preprocess_DB (dirty_df):
    clean_df = dirty_df.copy(deep=True)

    return clean_df

def print_fooditems(food_df, pop_df, index):
    for i in range(16):
        if (int(pop_df.loc[index,'Food'+str(i)]) > 0):
            print('Food'+str(i),': ')
            print(food_df.loc[pop_df.loc[index,'Food'+str(i)],'Weight (g)'],' grams of ',food_df.loc[pop_df.loc[index,'Food'+str(i)],'Food Name'])
            print('')
        else:
            return






