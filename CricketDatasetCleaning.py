# %%
# %pip install pandas openpyxl

# %%
import pandas as pd

# %%
df = pd.read_csv(r".\DataSet\CricketDataset.csv")
df.head()

# %%
new_column_names = ['Player', 'Span', 'Matches', 'Inns', 'Not_Outs', 'Runs_Scored', 'Highest_Inns_Score', 'Ave', 'Balls_Faced', 'Batting_Strikes_Rate', '100', '50', '0', '4s', '6s']
df.columns = new_column_names
df.head()

#rename the columns


# %%
df=df.drop(0) # drop the first row

# %%
df

# %%
df.isnull().any() # Check for missing values

# %%
df[df['Balls_Faced'].isna() == True] # rows with NaN values

# %%
df = df.fillna(0) # fill NaN values with 0
df

# %%
df.duplicated() # Check for duplicates

# %%
df.drop_duplicates() # No duplicates found

# %%
df['Span'].str.split(pat = '-') # Splitting the Span column into two columns

# %%
df['Rookie_Year'] = df['Span'].str.split(pat = '-').str[0] # Extracting the first year from the Span column

# %%
df.head()

# %%
df['Final_Year'] = df['Span'].str.split(pat = '-').str[1] # adding a new column for final year

# %%
df

# %%
df.drop(columns = ['Span'], inplace = True) # deleting the column

# %%
df

# %%
df['Country'] = df['Player'].str.split( pat = '(').str[1].str.replace(')', '') 
df['Player'] = df['Player'].str.split( pat = '(').str[0] 
#splitting the player name and country name

# %%
df

# %%
df.dtypes # to check the data types of the columns 

# %%
df = df.replace('[^a-zA-Z0-9.]', '', regex = True) # Remove all special characters from the DataFrame
df

# %%
df = df.astype({'Rookie_Year': 'int', 'Final_Year': 'int' })
df['Ave'] = df['Ave'].astype('float')
df.dtypes

# %%
df = df.astype({'Matches': 'int' , 'Inns' : 'int' , 'Not_Outs' : 'int' , 'Runs_Scored' : 'int' , 'Highest_Inns_Score' : 'int' , 'Batting_Strikes_Rate' : 'float' , '100' : 'int' , '50' : 'int' , '0' : 'int' , '4s' : 'int' , '6s' : 'int' })
#change types of columns to int

# %%
df.dtypes

# %%
for x in df.index :
    if df.loc[x , "Balls_Faced"] == '' :
        df.loc[x , "Balls_Faced"] = 0

# %%
df = df.astype({'Balls_Faced' : 'int' , 'Batting_Strikes_Rate' : 'float'}) # Converting the data type of Balls_Faced to int
df.dtypes

# %%
pd.set_option('display.max_rows', None) # Display all rows
df

# %%
pd.set_option('display.max_rows', 10) # to reset the display to default 
df

# %%
df['Career_legth'] = df['Final_Year'] - df['Rookie_Year'] # Career length is calculated by subtracting the rookie year from the final year
df

# %%
df['Career_legth'].mean() # Average Career Length ther's also .max() and .min()

# %%
df[df['Career_legth'] > 10]['Batting_Strikes_Rate'].mean() # Average Batting Strike Rate of players who have played more than 10 years

# %%
df[df['Rookie_Year'] < 1960]['Player'].count() # Number of players who started playing before 1960

# %%
pd.set_option('display.max_rows', None)
df.groupby('Country')['Highest_Inns_Score'].max().to_frame('highestinnsscore').reset_index().sort_values('highestinnsscore' , ascending = False) # Highest Inns Score by Country

# %%
df.groupby('Country')[['100' , '50' , '0']].mean() #mean of 100, 50 and 0 by country


