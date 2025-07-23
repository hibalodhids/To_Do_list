import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Pakistan_Covid19_Data.csv")
print(df)

df['Confirmed Cases'] = df['Confirmed Cases'].str.replace(',', '').astype(int)
df['Recoveries'] = df['Recoveries'].str.replace(',','').astype(int)
df['Deaths'] = df['Deaths'].str.replace(',','').astype(int)

print("Total Confirmed Cases:", df['Confirmed Cases'].sum())
print("Total Recoveries:", df['Recoveries'].sum())
print("Total Deaths:", df['Deaths'].sum())

cases = np.mean(df['Confirmed Cases'])
print("Average Confirmed Cases:", cases)

recoveries = np.mean(df['Recoveries'])
print(" Average Recoveries cases:",cases)

deaths = np.mean(df['Deaths'])
print("Average Deaths:",cases)

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Recoveries', y='Province', palette='viridis')
plt.title('PAKISTAN COVID-19: Recoveries by Province')
plt.xlabel('Recoveries')
plt.ylabel('Province')
plt.tight_layout()
plt.show()


















# import numpy as np
# import pandas as pd
# import seaborn as sns

# # Load the CSV file
# df = pd.read_csv("C:\\Users\\A.S\\Desktop\\covid 19.csv")

# # Optional: Clean column names (remove extra spaces)
# df.columns = df.columns.str.strip()

# # Print the DataFrame
# print(df)

# # Correct way to calculate sums
# print("Total Confirmed Cases:", df['Confirmed'].sum())
# print("Total Recoveries:", df['Recoveries'].sum())
# print("Total Deaths:", df['Deaths'].sum())
