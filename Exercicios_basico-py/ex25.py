nome= str((input('Digite seu nome: '))).strip().lower()
print('Tem {}silva{} no nome?? {} '.format('\033[4;36m','\033[m','silva' in nome) )