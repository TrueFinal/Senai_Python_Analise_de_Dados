import pandas as pd

data = {'Nome': ['João', 'Ana', 'Carlos', 'Maria', 'Pedro'],
        'Idade': [23, 78, 22, 19, 45],
        'Cidade': ['Belo Horizonte', 'Fortaleza', 'Brasília',
                   'São Paulo', 'Rio de Janeiro']}
df = pd.DataFrame(data)

df_filtrado = df[df['Idade'] > 25]