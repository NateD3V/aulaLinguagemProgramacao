import numpy as np
import time

# start_time = time.time()
# lista = [0] * 2000000
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de lista de 1 bilhão de elementos levou: {elapsed_time}')
#
# start_time = time.time()
# ndarray = np.zeros(10000000)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'A criação de um ndarray de 1 bilhão de elementos levou: {elapsed_time}')

rng = np.random.default_rng()  # numpy tem sua métodos random inclusos
vetor = rng.random(4)
print(f'Array de 1 Dimensão (VETOR) randômico:\n{vetor}\n')
matriz = rng.random([4, 4])
print(f'Array de 2 Dimensões (MATRIZ) randômico:\n{matriz}\n')
tensor = rng.random([4, 4, 4])
print(f'Array de 3  Dimensões (TENSOR) randômico:\n{tensor}\n')


rng = np.random.default_rng()
matriz = rng.random([4, 4])
m_coluna = np.sort(matriz, axis=0)
m_linha = np.sort(matriz, axis=1)
m_col_lin = np.sort(m_linha, axis=0)
print(f'Ordenação dentro coluna:\n{m_coluna}')
print(f'Ordenação dentro linha :\n{m_linha}')
print(f'Ordenação dentro coluna e linha :\n{m_col_lin}')