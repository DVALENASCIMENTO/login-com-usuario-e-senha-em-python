# Ler um número que é um código de usuário. Caso este código seja diferente, deve ser apresentada a mensagem ‘Usuário inválido!’.
# Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser
# mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.
# Autor: Diego Vale do Nascimento - 02/10/2022
print('"FAÇA O LOGIN COM USUÁRIO E SENHA"')
print('=' * 51)
import random
codigo = random.randint(1, 4)
n = int(input("insira o Código de Usuário: "))
print('~'*51)
while n != 1234:
    print('CÓDIGO INVÁLIDO!')
    codigo = random.randint(1, 4)
    print('~' * 51)
    n = int(input("insira novamente o Código de Usuário: "))
    print('=' * 51)
    print('=' * 51)
    senha = random.randint(1, 4)
    s = int(input("insira a Senha: "))
    print('~' * 51)
    while s != 9999:
        print('SENHA INCORRETA!')
        codigo = random.randint(1, 4)
        print('~' * 51)
        s = int(input("insira novamente a Senha: "))
        print('=' * 51)
        print('"ACESSO PERMITIDO"!')
