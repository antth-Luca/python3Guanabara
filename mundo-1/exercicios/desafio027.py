nome = str(input('Digite seu nome completo: ')).strip()
nomeSeparado = nome.split()
print('Seu primeiro nome é {}'.format(nomeSeparado[0]))
print('Seu último nome é {}'.format(nomeSeparado[len(nomeSeparado)-1]))
