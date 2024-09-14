import pandas as pd
import numpy as np

def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # family size
    # add siblings, spouses, parents and children + self
    df["Family Size"] = df["SibSp"] + df["Parch"] + 1

    # title
    df["Title"] = df["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)
    # all the special titles can be considered rare, as they aren't as frequent as mr, ms, mrs etc.
    df["Title"].replace(["Don", "Rev", "Dr", "Major", "Lady", "Sir", "Col", "Capt", "Countess", "Jonkheer"], "Rare", inplace=True)
    df["Title"].replace(["Ms", "Mlle"], "Miss", inplace=True)
    df["Title"].replace(["Mrs", "Mme"], "Misses", inplace=True)
    df["Title"].replace(["Mr"], "Mister", inplace=True)
    df["Title"].fillna("Other", inplace=True)

    # age group
    df["Age Group"] = pd.cut(df["Age"], bins=[0, 12, 18, 65, np.inf], labels=["Child", "Teenager", "Adult", "Senior"])

    # fare per person
    df["FarePerPerson"] = df["Fare"] / df["Family Size"]

    return df