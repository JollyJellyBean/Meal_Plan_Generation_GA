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
    # Drop rows where protein, carbohydrates and fats are 0
    clean_df = dirty_df[(dirty_df['Protein_(g)'] != 0) |
                        (dirty_df['Carbohydrt_(g)'] != 0) |
                        (dirty_df[ 'Lipid_Tot_(g)'] != 0)]

    dropped_df = dirty_df[(dirty_df['Protein_(g)'] == 0) &
                          (dirty_df['Carbohydrt_(g)'] == 0) &
                          (dirty_df[ 'Lipid_Tot_(g)'] == 0)]

    print(str(len(dropped_df))+" foods dropped where protein, carbohydrates and fats are 0")
    print(dropped_df['Shrt_Desc'])

    return clean_df

