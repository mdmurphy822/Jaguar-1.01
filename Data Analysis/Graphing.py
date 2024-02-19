import matplotlib.pyplot as plt
import pandas as pd

# Example 1 takes a local csv file and displays the top 5 countries that login attempts originated from.
# This data is plotted against

df = pd.read_csv('Admin_Log.csv')

agg_data = df.groupby('Country').sum().reset_index()

top_5 = agg_data.nlargest(5, 'LoginAttempts')

plt.bar(top_5['Country'], top_5['LoginAttempts'])

plt.xlabel('Country')
plt.ylabel('LoginAttempts')
plt.title('Top 5 Countries with the Most Login Attempts')

plt.grid(True)
plt.show()
