df = pd.read_csv('data/test_data.csv')
sns.scatterplot(data=df, x='x', y='y')
sns.despine()
plt.show()