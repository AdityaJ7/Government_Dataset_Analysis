import pandas as pd

df = pd.read_csv('dd.csv')
# Dropping the columns for countrycode , politicalcode, region name , leader name and the leadership summary as they dont add any useful information to our EDA
df.drop(["cowcode2", "politycode", "un_region_name",
         "ehead", "leaderspellreg"], axis=1, inplace=True)
# Providing better names of two columns
df.rename(columns={'ctryname': 'Country',
                   'un_continent_name': 'Continent'}, inplace=True)

# Function for data categorization of the start_year column which is used to form a new column called period


def period(year):
    """[Takes in the year value and categories it under one of the three values: Early, Middle or Late based on the criteria providde in the conditional statements]

    Args:
        year ([int]): [year when the government started]

    Returns:
        [string]: [Category in which the year provided in input got classified into]
    """
    if year > 1945 and year <= 1965:
        return 'Early'
    elif year > 1965 and year <= 1985:
        return 'Middle'
    else:
        return 'Late'


# Ensuring that the column contains numeric values
df['start_year'] = pd.to_numeric(df['start_year'])

# New categorial column on the basis of year of start of the government
df['Period'] = df['start_year'].apply(period)

# Saving the  adjusted dataframe into a new file
df.to_csv('adjusted_dd.csv')
