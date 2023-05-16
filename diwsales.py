import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline 
import seaborn as sns

df = pd.read_csv(r'C:\Users\HP\Desktop\p6\Diwali Sales Data.csv', encoding = 'unicode_escape')

df.shape
df.head(5)

df.info()

df.drop(['Status','unnamed1'], axis=1, inplace=True)

pd.isnull(df).sum()

df.dropna(inplace=True)

df['Amount'] = df['Amount'].astype('int64')
df['Amount'].dtypes

df.columns

df.describe()
df[['Age', 'Orders', 'Amount']].describe()

ax = sns.countplot(x = 'Gender', data = df)
for bars in ax.containers:
    ax.bar_label(bars)
    
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount')
sns.barplot(x='Gender', y='Amount', data=sales_gen)

ax = sns.countplot(data=df, x='Age Group', hue='Gender')
for bars in ax.containers:
    ax.bar_label(bars)
     
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x='Age Group', y='Amount', data=sales_age)

sns.set(rc={'figure.figsize': (20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
    
sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize': (20,5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize': (20,5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')
