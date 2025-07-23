# import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns 

# sns.set_style("whitegrid")

# #load dataSets

# url = "https://gist.githubusercontent.com/Ironraptor3/34f3938c703111353ee5f28cc9b29d68/raw/5c57e51dbc550a141a44f93028104ffce6281624/vgsales.csv"

# try :
#     game = pd.read_csv(url)
# except:
#     game = pd.read_csv('vgsales.csv')
# # print(game.isnull().sum())  # Check missing values
# # game.dropna(inplace=True)  # Drop rows with missing data
# top_games = game.sort_values(by='Global_Sales', ascending=False).head(10)
# print(top_games[['Name', 'Global_Sales']])
# plt.figure(figsize=(10,6))
# sns.barplot(x='Global_Sales', y='Name', data=top_games, palette='viridis')
# plt.title('Top 10 Best Selling Games Globally')
# plt.xlabel('Global Sales (millions)')
# plt.show()

# print(game.head())
# print(game.info()) 

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

sns.set_style("whitegrid")
try:
   game = pd.read_csv("Games.csv")
except:
   print("Failed to load Excel file:")

downloaded_games = game.sort_values(by='Downloads (Pakistan)', ascending=False).head(10)
print(downloaded_games[['Game Name', 'Downloads (Pakistan)']])

plt.figure(figsize=(10, 6))
sns.barplot(
    x='Game Name',
    y='Downloads (Pakistan)',
    data=downloaded_games,
    palette='viridis'
)

plt.title('Top 10 Downloaded Games in Pakistan')
plt.xlabel('Game Name')
plt.ylabel('Downloads (Pakistan)')
plt.show()

