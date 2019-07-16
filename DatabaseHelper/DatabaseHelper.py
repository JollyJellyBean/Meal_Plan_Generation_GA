#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                    #
#                                                               #
#################################################################

import pandas as pd


# INPUT:  - Food_DF:
#         - Parents:
# OUTPUT:
# DESCRIPTION:
def import_DB(DB_DIR):
    print('importing From:', DB_DIR)
    Food_DF = pd.read_csv(DB_DIR)
    Food_DF.loc[-1] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # adding a row for NULL case
    Food_DF.index = Food_DF.index + 1  # shifting index

    Food_DF = clean_DB(Food_DF)

    return Food_DF

# INPUT:  - Food_DF:
#         - Parents:
# OUTPUT:
# DESCRIPTION:
def clean_DB (DB):
    new_DB = DB.copy(deep=True)

    new_DB.dropna()

    return new_DB

