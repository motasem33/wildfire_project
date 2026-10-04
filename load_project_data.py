import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

file_path = "Algerian_forest_fires_dataset.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

df = df[df['Classes'].astype(str).str.strip() != 'Classes']
df = df.dropna(subset=['Classes'])

df['Classes'] = df['Classes'].astype(str).str.strip()

print("=" * 60)
print("1. First 5 Rows :")
print(df.head())

print("\n" + "=" * 60)
print(f"2. Dataset Dimensions : {df.shape[0]} Rows, {df.shape[1]} Columns")

print("\n" + "=" * 60)
print("3. Missing Values :")
print(df.isnull().sum())

print("\n" + "=" * 60)
print("4. Target Distribution:")
print(df['Classes'].value_counts())