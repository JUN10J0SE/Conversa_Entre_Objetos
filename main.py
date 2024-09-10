#Crie um programa que cria dois objetos da mesma classe (Pessoa), e mostre uma conversa amigável entre os dois objetos.

#importacao de biblioteca
import random

#class Pessoa
class Pessoa:
    #os atributos sao sempre definidos dentro do metodo
    #metodo construtor
    def __init__(self, nome, humor):
        self.nome = nome
        self.humor = humor

    def cumprimentar(self):
        if self.humor:
            print(f'Olá o meu nome é {self.nome}: qual o seu? ')
        else:
            print(f'Me deixa!')

    def responder(self, nome, humor):
        if humor:
            print(f'Olá {nome}, meu nome é {self.nome} Prazer')
            self.humor = True
        else:
            print(f'Me deixa...')
            self.humor = False
        return self.humor

#Programa principal
if __name__ == '__main__':
    humores = (True, False)
    nome1 = input('Informe o seu nome: ')
    nome2 = input('Informe o seu nome: ')

    usuario1 = Pessoa(nome1, humores[random.randint(0,1)])
    usuario2 = Pessoa(nome2, humores[random.randint(0,1)])

    usuario1.cumprimentar()
    usuario1.humor = usuario2.responder(usuario1.nome, usuario2.humor)

    if usuario1.humor:
        print(f'{usuario1.nome} ficou feliz.')
    else:
        print(f'{usuario2} FiCou triste')