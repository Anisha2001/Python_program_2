import pandas as pd
diamonds = pd.read_csv('https://storage.googleapis.com/kaggle-data-sets/1312/2368/compressed/diamonds.csv.zip?GoogleAccessId=web-data@kaggle-161607.iam.gserviceaccount.com&Expires=1590256324&Signature=lXFOP1UR1Nwj7KigJXIOXn1VYIfPZQHfX%2FCbi%2B%2F3MnGCL8AB5oakU%2BGq0aGvRWrX1wTRptYEx87AxsIU16dvb6CVRaEskY229hYPmfsgoGGV05VfiNp56JN1Wp2k%2FK%2B7eqdTkLvfyLYXbD%2BTX0zCj18zYjG7zg5GwMtY%2BqGpRjlMEQT66X4nvv%2FnQQLXFT%2FnoiF4WaMC2CS%2F9Zc6JB8LONKm3TZqWZkHnVtTdElZ4TgRuNzaaN%2F9sgxr%2BNrWrI%2ByyaCNl6HW0B7lM6uqHreHHaQYigCc%2F5UV2UdI5Nc7K4i%2BtiLUtbPdAoe2Jld69TWkcpjp0IK9LWZpQ7HvibBunQ%3D%3D&response-content-disposition=attachment%3B+filename%3Ddiamonds.csv.zip')
print("Original Dataframe:")
print(diamonds.shape)
print("\nSample 75% of diamonds DataFrame's rows without replacement:")
result = diamonds.sample(frac=0.75, random_state=99)
print(result)
print("\nRemaining 25% of the rows:")
print(diamonds.loc[~diamonds.index.isin(result.index), :])