import numpy as np
from scipy import stats

data = np.random.normal(loc=0, scale=1, size=100)

kstest_result = stats.kstest(data, 'norm')


print("Estadística de prueba: ", kstest_result.statistic)
print("Valor p: ", kstest_result.pvalue)


alpha = 0.05  

if kstest_result.pvalue < alpha:
    print("Se rechaza la hipótesis nula ya que el valor de p es menor que el umbral adquirido, por lo tanto la implementacion del programa no a tenido efecto en la reduccion del comportamiento violento.")
else:
    print("Se comprueba la hipotesiste, es decir, el programa de educacion a tenido efecto significativo en la reduccion del comportamiento violento.")

