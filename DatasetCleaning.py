# %% [markdown]
# instalations

# %%
# %pip install pandas openpyxl

# %%
import pandas as pd

# %% [markdown]
# read file

# %%
df = pd.read_excel(r".\DataSet\Customer Call List.xlsx")
df 

# %% [markdown]
# remove duplicates and not letters from the dataframe

# %%
df["Last_Name"] = df["Last_Name"].str.strip("123./_")
df

# %%
df["Phone_Number"] = df["Phone_Number"].str.replace('[^a-zA-Z0-9]', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace('nan--', '', regex=True)
df["Phone_Number"] = df["Phone_Number"].str.replace('Na--', '', regex=True)
df

# %%
df[[ "Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(",", expand=True)
df

# %%
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y')
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N')
df['Paying Customer'] = df['Paying Customer'].str.replace('N/a', '')

df

# %%
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y')
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N')

df

# %% [markdown]
# fill novalue with blank

# %%
df = df.fillna('')
df

# %% [markdown]
# reutrn only people that we can contact

# %%
for x in df.index :
    if df.loc[x , "Do_Not_Contact"] == 'Y' :
        df.drop (x , inplace = True)

#df = df.drop(columns = "Address")
#df = df.drop(columns = "Not_Useful_Column")

for x in df.index :
    if df.loc[x , "Phone_Number"] == '' :
        df.drop (x , inplace = True)
df


# %%
df.reset_index(drop=True, inplace=True)

# %%
df

# %%
df.isnull()


