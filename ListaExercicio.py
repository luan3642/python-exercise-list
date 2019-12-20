import math
import random
from builtins import print

# from pygame import mixer

linha = '-' * 50
titulo = '\033[1;34;40mLista de Exercicios\033[m'

print()
print(titulo.center(65))
print(linha)

print()

print('1) Calcule a média de um aluno que possui 4 notas')
print()
print('2) Escreva o sucessor e o antecessor de um número')
print('')
print('3) Converta de Fanhreit  para Celsius ')
print('')
print('4) Descubra o dobro, o triplo e a raiz quadrada de um número ')
print()
print('5) Imprima a tabuada de um número')
print()
print('6) Realize a divisão de dois números')
print()
print('7) Informe o Cateto Oposto, Cateto Adjacente e a Hipotenusa de um Triangulo Retangulo')
print()
print('8) Leia um angulo e informe seu seno, cosseno e tangente')
print()
print('9- Leia o número de 4 alunos e sortei 1 deles')
print()
print('10- Toque uma música utilizando Python ')
print()
print(
    '11- Faça com que o nome que o usuário digitar fique em LETRA MAIÚSCULA e conte quantas letras existem nessa frase')
print()
print('12- Descubra a Unidade, Dezena, Centena e Unidade de milhar')
print()
print('13- Separe o nome do sobrenome de um usuário')
print()
print('14- Digite 2 números e informe o maior número')
print()
print('15- Entre com um número e informe se é impar ou par  ')
print()
print('16- Entre com a receita e a despesa de uma empresa, para informar se ela teve lucro ou prejuízo')
print()
print(
    '17- Mande o usuário entrar com um número e descubra se esse número é maior 100, menor que 100 ou é um número negativo')
print()
print(
    '18- Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.')
print()
print('19- Faça um Programa que verifique se uma letra digitada é vogal ou consoante.')
print()
print(
    '20- Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.')
print()
print("21- Faça um Programa que leia três números e mostre o maior deles")
print()
print('\033[1;32;0m0) Para sair do programa \033[m')
print()
print(linha)

escolha = int(input('\033[1;32;36mEscolha um exercício: \033[m'))
print('-' * 50)

while escolha != 0:
    if escolha == 1:
        print()
        n1 = int(input('Digite a sua primeira nota: '))
        n2 = int(input('Digite a sua segunda nota: '))
        n3 = int(input('Digite a sua terceira nota: '))
        n4 = int(input('Digite a sua quarta nota: '))

        media = (n1 + n2 + n3 + n4) / 4

        print("A média do aluno é: ", media)
        print()

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 2:
        numero = int(input("Digite um número: "))

        antecessor = numero - 1
        sucessor = numero + 1

        print("Antecessor desse número: ", antecessor)
        print("Sucessor desse número: ", sucessor)

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 3:

        temperatura = int(input('Informe a temperatura em fahrenheit a ser convertida em graus celsius '))

        conversao = (5 * (temperatura - 32) / 9)

        print('{}ºF, convertidos em graus celsius equivalem  {:.2f}ºC'.format(temperatura, conversao))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 4:

        dobro = int(input('Digite um número para saber seu dobro: '))

        saberDobro = dobro * 2

        triplo = int(input('Digite um número para saber seu triplo: '))

        saberTriplo = triplo * 3

        raiz = int(input('Digite um número para saber a sua raiz: '))

        saberRaiz = math.sqrt(raiz)

        print()
        print("O dobro de \033[1;32;0;m{}\033[m, é \033[1;32;0;m{} \033[m".format(dobro, saberDobro))
        print()
        print('O triplo de \033[1;33;0;m{}\033[m, é \033[1;33;0;m {}\033[m '.format(triplo, saberTriplo))
        print()
        print('A raiz de \033[1;34;0;m{}\033[m, é \033[1;34;0;m{:.0f} \033[m'.format(raiz, saberRaiz))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 5:
        numTab = int(input('Informe um número para imprimir a sua tabuada: '))
        print()

        for i in range(0, 11):
            s = numTab * i
            print('{} * {} = {}'.format(numTab, i, s))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 6:
        nm1 = int(input('Entre com o primeiro número: '))

        nm2 = int(input('Entre com outro número: '))

        divisao = nm1 / nm2

        print('A divisão dos números é {:.1f}'.format(divisao))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 7:

        co = float(input("Digite o valor do cateto oposto "))
        ca = float(input("Digite o valor do cateto adjacente "))

        hi = math.hypot(co, ca)

        print("O comprimento da hipotenusa é {} ".format(hi))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 8:
        angulo = int(input("Digite um angulo "))

        seno = math.sin(math.radians(angulo))
        coseno = math.cos(math.radians(angulo))
        tangente = math.tan(math.radians(angulo))

        print("O angulo de seno é {:.2f}°".format(seno))
        print("O angulo coseno é {:.2f}°".format(coseno))
        print("O angulo da tangente é {:.2f}º".format(tangente))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 9:

        numberOne = int(input('Informe um número, ESTUDANTE 1: '))

        numberTwo = int(input('Informe um número, ESTUDANTE 2: '))

        numberThree = int(input('Informe um número, ESTUDANTE 3: '))

        numberFor = int(input('Informe um número, ESTUDANTE 4: '))

        sorteia = numberOne, numberTwo, numberThree, numberFor

        a = random.choice(sorteia)

        print()
        print('O número sorteado é ', a)

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()


    elif escolha == 10:
        mixer.init()
        mixer.music.load('FUNKTRISTE.mp3')
        mixer.music.play()

        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 11:
        nomeDigitado = input('Digite um nome: ')
        print()
        print(nomeDigitado.upper())
        print()
        print('Esse nome tem: {} letras'.format(len(nomeDigitado)))
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()


    elif escolha == 12:
        nmDig = int(input('Digite um valor entre 0 e 9999: '))

        convert = str(nmDig)
        print()

        print('Unidade: {}'.format(convert[3]))
        print('Dezena: {}'.format(convert[2]))
        print('Centena: {}'.format(convert[1]))
        print('Unidade de milhar {}'.format(convert[0]))

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()


    elif escolha == 13:

        name = input('Entre com o seu nome e sobrenome: ').strip().split()

        print('Seu nome é: ', name[0])
        print('Seu sobrenome é: ', name[1])

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 14:

        number1 = int(input('Digite o 1 número:'))

        number2 = int(input('Digite o 2 número: '))

        if number1 > number2:
            print('O maior número é: ', number1)
        elif number1 == number2:
            print('Números iguais')
        else:
            print('O maior número é: ', number2)

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 15:

        asd = int(input('Digite o número: '))

        if asd % 2 == 0:
            print()
            print('Par')
            print()
        else:
            print()
            print('Impar')
            print()

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 16:
        receita = int(input('Entre com a receita da empresa: '))

        despesa = int(input('Entre com a despesa da empresa: '))

        if receita > despesa:
            print()
            print('Você obteve lucro')
            print()
        else:
            print()
            print('Você obteve prejuizo')
            print()

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 17:

        j = int(input('Entre com número '))

        if j > 100:
            print('Maior de 100 ')
        elif j < 0:
            print('Número negativo ')
        else:
            print('Menor que 100')

        print('-' * 59)
        escolha = int(input('\033[1;31;0m Escolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 18:

        letraDigitada = input('Digite seu sexo, usando as letras M ou F: ').upper()

        if letraDigitada in 'M':
            print()
            print('Sexo Masculino')
        elif letraDigitada in 'F':
            print()
            print('Sexo Feminino')
        else:
            print()
            print('Sexo inválido')

        print('-' * 59)
        escolha = int(input('\033[1;31;0mEscolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 19:

        vogais = ['A', 'E', 'I', 'O', 'U']
        consoantes = ['B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']

        descobreLetra = input('Digite uma letra para descobrir se é vogal ou consoante: ').upper()

        if descobreLetra in vogais:
            print('VOGAL')
        elif descobreLetra in consoantes:
            print('CONSOANTE')

        print('-' * 59)
        escolha = int(input('\033[1;31;0mEscolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

    elif escolha == 20:

        nomeProdutoPrimeiro = input('Informe o primeiro produto que deseja comprar: ')

        valor1 = float(input('Informe o preço deste de produto: '))

        print()
        nomeProdutoSegundo = input('Informe o segundo produto que deseja comprar: ')

        valor2 = float(input('Informe o preço desse segundo produto: '))

        print()
        nomeProdutoTerceiro = input('Informe o terceiro produto que deseja comprar: ')

        valor3 = float(input('Informe o preço desse terceiro produto: '))

        print()

        if valor1 < valor2:
            print(valor1)
        elif valor1 < valor3:
            print(valor1)

        elif valor2 > valor1:
            print(valor2)
        elif valor2 < valor3:
            print(valor2)

        elif valor3 < valor1:
            print(valor3)
        elif valor3 < valor2:
            print(valor3)

    elif escolha == 21:
        numero1 = int(input("Digite o 1 número: "))
        numero2 = int(input("Digite o 2 número: "))
        numero3 = int(input("Digite o 3 número: "))

        if numero1 > numero2 >= numero3:
            numero3 = numero2
            numero3 = numero1
            print("O maior número é: {}".format(numero3))
        elif numero1 > numero2 <= numero3:
            numero3 = numero1
            numero3 = numero2
            print("O maior número é: {}".format(numero3))
        elif numero2 > numero3 >= numero1:
            numero1 = numero3
            numero1 = numero2
            print("O maior número é: {}".format(numero1))
        elif numero2 > numero3 <= numero1:
            numero1 = numero3
            numero1 = numero2
            print("O maior número é: {}".format(numero1))
        elif numero3 > numero1 >= numero2:
            numero2 = numero1
            numero2 = numero3
            print("O maior número é: {}".format(numero2))
        elif numero3 > numero1 <= numero2:
            numero2 = numero1
            numero2 = numero3
            print("O maior número é: {}".format(numero2))

        print('-' * 59)
        escolha = int(input('\033[1;31;0mEscolha outro exercício, ou aperte 0 para sair do programa: \033[m'))
        print('-' * 59)
        print()

print()
print('\033[1;31;40;mVocê saiu do programa \033[m')
