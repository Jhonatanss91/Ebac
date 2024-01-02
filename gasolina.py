# código de geração do gráfico
import matplotlib.pyplot as plt
import pandas as pd

data_gas = pd.read_csv('/content/Ebac/gasolina.csv', sep=',')
plt.figure(figsize=(12, 6))
plt.plot(data_gas['dia'],data_gas['venda'])
plt.title('preço gasolina-2021')
plt.xlabel('dia(julho)')
plt.ylabel('Preço(R$)')
plt.show()
plt.savefig('gasolina.png', format='png')
