import pandas as pd 
import matplotlib.pyplot as plt

data = {'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
        'Data de Fabricação': ['2024-01-01', '2024-02-01', '2024-03-01', '2024-04-01', '2024-05-01']}
df = pd.DataFrame(data)

df['Data de Fabricação'] = pd.to_datetime(df['Data de Fabricação'])

df = df.sort_values('Data de Fabricação')

plt.plot_date(df['Data de Fabricação'], df['Produto'], linestyle='solid')
plt.gcf().autofmt_xdate

plt.title('Datas de Fabricação por Produto')
plt.xlabel('Data de Fabricação')
plt.ylabel('Produto')

plt.tight_layout()
plt.show()