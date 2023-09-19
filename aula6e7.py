# -*- coding: utf-8 -*-
"""aula6e7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t-moROe4cBxcRRCiHTzWa7PWHqFDJmfu
"""

# UNINASSAU
# DOCENTE: CLOVES ROCHA
# CC/SI/EC - 4MA E 4MB
# 11. Um pouco de Álgebra Linear

IMC = [181, # ALTURA
       100, # PESO
       40]  # IDADE
print(IMC)

NOTAS = [10, # N1
         9,  # N2
         8,  # N3
         4]  # N4
print(NOTAS)

def vet_add(vet1, vet2):
  #soma elementos correspondentes
return [vet1_i + vet2_i
      for vet1_i, vet2_i in zip(vet1, vet2)]

def vet_sub(vet1, vet2):
  #subtrair elementos correspondentes
return [vet1_i - vet2_i
        for vet1_i, vet2_i in zip(vet1, vet2)]

def vet_soma(vets):
# soma todos elementos correspondentes
result = vets[0] # começa com o primeiro vetor
for vet in vets[1:]: # depois passa por todos os outros
  result = vet_add(result, vet) # e os adiciona ao resultado
return result

metro = [100, 101, 102, 103, 104]
metro.append(105) # insere um elemento no final da fila
metro.append(106)
metro.append(107)
print(metro)

class Pessoa(object):
  def __init__(self):
    self.dados = []

  def inserir(self, elemento):
    self.dados.append(elemento)

  def retirar(self):
   return self.dados.pop(0)

  def vazia(self):
    return len(self.dados) == 0

# Revisar f ou format
idade = int(input('Digite sua idade: '))
print(f'Sua idade é {idade} anos.')