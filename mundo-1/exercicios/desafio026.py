frase = str(input('Digite uma frase: ')).strip()
upFrase = frase.upper()
print('A letra "A" aparece {} vezes na sua frase'.format(upFrase.count('A')))
print('A primeira vez que a letra "A" aparece é na {}° posição'.format(upFrase.find('A')+1))
print('A última vez que a letra "A" aparece é na {}° posição'.format(upFrase.rfind('A')+1))
