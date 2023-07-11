import numpy as np

# Datos de ejemplo: tipos de violencia A y B (como listas o arrays NumPy)
violencia_fisica = [1, 2, 3, 4, 5]
violencia_psicologica = [5, 4, 3, 2, 1]

# Calcular la correlación entre los tipos de violencia A y B
correlacion = np.corrcoef(violencia_fisica, violencia_psicologica)[0, 1]

print("La correlación entre los tipos de violencia A y B es:", correlacion)
