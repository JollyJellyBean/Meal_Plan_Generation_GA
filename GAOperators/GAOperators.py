#################################################################
#                                                               #
# Copyright 2019 All rights reserved.                           #
# Author: Jakob Mawdsley                                         #
#                                    #
#                                                               #
#################################################################

import pandas as pd
import random

# INPUT:  - Food_DF:
#         - Parents:
# OUTPUT:
# DESCRIPTION:
def initPop(Food_DF, Parents):


    Population_DF = pd.DataFrame(columns=['Food0','Food1','Food2','Food3','Food4','Food5','Food6','Food7','Food8','Food9','Food10','Food11','Food12','Food13','Food14','Food15'])

    #For total number of parents
    for i in range(Parents):

        # init meal plan list
        Meal_List = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']


        #For random number of food items between 8 and 16
        for j in range(random.randint(8,16)):
            #Find Random Food
            randfood = random.randint(0,len(Food_DF.index))
            Meal_List[j] = randfood

        Population_DF.loc[i] = Meal_List
        Meal_List.clear()

    Population_DF = update_Foodplan(Food_DF,Population_DF)

    return Population_DF



# INPUT:  - population_df: population dataframe
# OUTPUT:- new_population_df: population dataframe
# DESCRIPTION:  when called function may or may not cause mutation
def mutate (Population_df,food_df):

    new_population_df = Population_df.copy(deep=True)
    food_df_size = len(food_df)

    i = 0
    for row_index  in new_population_df.iterrows():

        var = random.randrange(1, 100, 1)
        if var == 1:
            column_index = random.randrange(0, 15, 1)
            new_food = random.randrange(0,food_df_size, 1)

            new_population_df.iat[i,column_index] = new_food
            #new_population_df.ix[row_index,column_index] = new_food
        i = i+1


    return new_population_df



def crossover(df):

    population_df = df.copy(deep=True)
    #population_df = split_tail(population_df,0,1)
    iterator =int(population_df.shape[0]/2)

    for i in range(iterator):
        j = i*2
        population_df = split_tail(population_df,j,j+1)
    return population_df
# INPUT:  - population_df: population dataframe
#         - Parent0
#         - Parent1
# OUTPUT:-
# DESCRIPTION:

def split_tail (Population_df,Parent0,Parent1):
    new_population_df = Population_df.copy(deep=True)
    P0 = new_population_df.iloc[Parent0].values
    P1 = new_population_df.iloc[Parent1].values
    new_population_df.loc[Parent0,8:16] = P1[8:16]
    new_population_df.loc[Parent1,8:16] = P0[8:16]
    return new_population_df


# INPUT:  - Food_DF: Food database dataframe
#         - Population_DF: population dataframe
# OUTPUT: Outputs dataframe of population
# DESCRIPTION: updates population nutrient information and fitness
def update_Foodplan(Food_DF,population_DF):
    new_population_df = population_DF.copy(deep=True)

    new_population_df['Calories'] = 0
    new_population_df['Protein'] = 0
    new_population_df['Carbohydrates'] = 0
    new_population_df['Fat'] = 0
    new_population_df['Cholesterol'] = 0
    new_population_df['Calcium'] = 0
    new_population_df['Iron'] = 0
    new_population_df['Sodium'] = 0
    new_population_df['Cost'] = 0
    new_population_df['# of Foods'] = 0
    new_population_df['Fitness'] = 0

    for index, row in new_population_df.iterrows():
        Calories = 0
        Protein = 0
        Carbohydrates = 0
        Fat = 0
        Cholesterol = 0
        Calcium = 0
        Iron = 0
        Sodium = 0
        Food_num = 0

        for i in range(16):
            Food_type = new_population_df.at[index,'Food'+ str(i)]

            if(int(Food_type)<1):
                Sodium +=0
            else:
                Calories += (Food_DF.at[int(Food_type),'Energ_Kcal'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Protein += (Food_DF.at[int(Food_type),'Protein_(g)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Carbohydrates += (Food_DF.at[int(Food_type),'Carbohydrt_(g)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Fat += (Food_DF.at[int(Food_type),'Lipid_Tot_(g)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Cholesterol += (Food_DF.at[int(Food_type),'Cholestrl_(mg)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Calcium += (Food_DF.at[int(Food_type),'Calcium_(mg)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Iron += (Food_DF.at[int(Food_type),'Iron_(mg)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Sodium += (Food_DF.at[int(Food_type),'Sodium_(mg)'])*(Food_DF.at[int(Food_type),'GmWt_2'])/100
                Food_num +=1

        new_population_df.ix[index,'Calories'] = Calories
        new_population_df.ix[index,'Protein'] = Protein
        new_population_df.ix[index,'Carbohydrates'] = Carbohydrates
        new_population_df.ix[index,'Fat'] = Fat
        new_population_df.ix[index,'Cholesterol'] = Cholesterol
        new_population_df.ix[index,'Calcium'] = Calcium
        new_population_df.ix[index,'Iron'] = Iron
        new_population_df.ix[index,'Sodium'] = Sodium
        new_population_df.ix[index,'# of Foods'] = Food_num

    return new_population_df


# INPUT:  - Food_DF: Food database dataframe
#         - Population_DF: population dataframe
# OUTPUT: Outputs dataframe of population
# DESCRIPTION: updates population nutrient information and fitness
def Select_Parents(Population_df,Population_Number):
    parent_DF = Population_df.copy(deep=True)
    parent_DF.drop(parent_DF.index, inplace=True)

    pop_div_two = int(Population_Number/2)

    for i in range(pop_div_two):
        Parent1_index = select_parents_tournament(Population_df)
        Parent2_index = select_parents_tournament(Population_df)

        Parent1 = Population_df.iloc[[Parent1_index]]
        Parent2 = Population_df.iloc[[Parent2_index]]
        Parents = pd.concat([Parent1, Parent2])

        parent_DF = pd.concat([parent_DF, Parents])
        parent_DF = parent_DF.reset_index(drop=True)

    return parent_DF


# INPUT:  - df: population dataframe
# OUTPUT:  - index: Outputs index of a parent(int)
# DESCRIPTION: Uses proportional Roulette wheel to determine parent
def select_parents_roulette(df):
    # define roulette wheel position(pick)
    max = df['Fitness'].sum()
    pick = random.uniform(0, max)
    current = 0

    # determine what index the position(pick) corresponds to
    for index, row in df.iterrows():
        current += df.ix[index, 'Fitness']
        if current >= pick:
            return index


# INPUT:  - df: population dataframe
# OUTPUT: - index: Outputs index of a parent(int)
# DESCRIPTION: Uses tournament to determine parent
def select_parents_tournament(df):
    tournament_df = df.copy(deep=True)
    tournament_df = tournament_df.sample(n=2)
    index = int(tournament_df['Fitness'].idxmax())

    return index