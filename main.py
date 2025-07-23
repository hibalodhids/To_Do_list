import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 
# data = {
#     'Name': ['Hiba', 'Ali', 'Sara', 'Omar'],
#     'Age': [23, 29, 31, 25],
#     'Score': [88, 92, 79, 85]
# }
data = pd.DataFrame({
    'value': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6],
    'group': ['A', 'A', 'B', 'B', 'A', 'A', 'B', 'B', 'A', 'A', 'B']
})
df = pd.DataFrame(data)
# sns.histplot(x="Name",y="Score",data=df)
sns.histplot(data=df, x='value', hue='group', multiple='stack')

plt.title('Scores by Name')
plt.show()

# tips = sns.load_dataset("")
