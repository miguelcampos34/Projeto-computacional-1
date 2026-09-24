class Companhia:
    def __init__(self, nome, quantidade_funcionarios, verba, salario, rota):
        self.nome = nome
        self.quantidade_funcionarios = quantidade_funcionarios
        self.verba = verba
        self.salario = salario
        self.rota = rota

class Pessoa:
    def __init__(self, nome, cpf, PCD):
        self.nome = nome
        self.cpf = cpf
        self.PCD = PCD


class Passageiro(Pessoa):
    def __init__(self, nome, cpf, telefone, idade, passagem):
        super().__init__(nome, cpf, PCD)
        self.telefone = telefone
        self.idade = idade
        self.passagem = passagem

    def nao_pagantes(self):
        if idade >= 65 or idade <= 5 or PCD:
            passagem = 0


class Funcionario(Pessoa, Companhia):
    def __init__(self, nome, cpf, cargo, salario):
        super().__init__(nome, cpf, salario)
        self.cargo = cargo
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

class Motorista(Funcionario, Companhia):
    def __init__(self, nome, cpf, telefone, CNH):
        super().__init__(nome, cpf, salario)
        self.telefone = telefone
        self.CNH = CNH

class Atendente(Funcionario, Companhia):
    def __init__(self, nome, cpf, telefone):
        super().init(nome, cpf, salario)
        self.telefone = telefone

        def telefonemas(self):
            print(self.telefone)


class Onibus(Companhia):
    def __init__(self, numero, capacidade, assentos_ocupados,preco):
        super().__init__(rota)
        self.numero = numero
        self.capacidade = capacidade


class Onibus_interestadual(Onibus, Companhia):
    def __init__(self, distancia, duracao, destino, origem, motorista, passageiros,preco, assentos_ocupados):
        super().__init__(rota)
        self.distancia = distancia
        self.duracao = duracao
        self.destino = destino
        self.origem = origem
        self.motorista = motorista
        self.passageiros = passageiros
        self.preco = preco
        self.assentos_ocupados = assentos_ocupados

class Onibus_rodoviario(Onibus, Companhia):
    def __init__(self, numero):
        super().__init__(rota, numero, capacidade, preco_fixo)
        self.preco_fixo = preco_fixo
