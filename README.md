# Relatório — Sistema de Gerenciamento de Transporte Rodoviário

## Descrição

O projeto consiste no desenvolvimento de um sistema em Python voltado para a representação e organização de uma companhia de transporte rodoviário. O sistema utiliza conceitos de Programação Orientada a Objetos (POO) para representar pessoas, funcionários, passageiros, motoristas, atendentes, ônibus e diferentes tipos de transporte.

A estrutura foi organizada por meio de classes e relacionamentos de herança. A classe Pessoa, por exemplo, representa informações comuns a diferentes indivíduos, como nome e CPF. A partir dela, é criada a classe Passageiro, enquanto Funcionario representa os funcionários da companhia e possui especializações como Motorista e Atendente.

Também foram criadas classes relacionadas aos ônibus, como Onibus, Onibus_interestadual e Onibus_rodoviario, permitindo representar características específicas de cada modalidade de transporte.

O objetivo é aplicar, em um exemplo prático, conceitos de orientação a objetos para modelar uma situação próxima à realidade de uma empresa de transporte.

## Justificativa

A escolha desse tema foi motivada pela possibilidade de aplicar conceitos de programação orientada a objetos em um problema do cotidiano. Uma companhia de transporte possui diferentes tipos de pessoas, funcionários, veículos, passageiros e serviços, tornando o cenário adequado para a utilização de classes, atributos, métodos e herança.

O desenvolvimento do projeto permite compreender como diferentes entidades podem ser representadas dentro de um sistema computacional e como características semelhantes podem ser reutilizadas por meio da herança.

Além disso, o projeto possibilita a prática da organização e estruturação de código, facilitando futuras alterações e ampliações do sistema.

## Funcionalidades

O código desenvolvido apresenta as seguintes funcionalidades e estruturas:

### 1 Cadastro de companhia

A classe Companhia permite representar informações relacionadas à empresa, como:

- Nome;
- Quantidade de funcionários;
- Verba;
- Salário;
- Rota.

### 2 Cadastro de pessoas

A classe Pessoa armazena informações básicas de uma pessoa:

- Nome;
- CPF;
- Condição de PCD.

Essa classe serve como base para outras classes do sistema.

### 3 Cadastro de passageiros

A classe Passageiro herda características de Pessoa e acrescenta:

- Telefone;
- Idade;
- Passagem.

Também existe o método `nao_pagantes()`, planejado para verificar condições que podem permitir gratuidade da passagem, como idade ou condição de PCD.

### 4 Cadastro de funcionários

A classe Funcionario representa funcionários da companhia, contendo informações como:

- Nome;
- CPF;
- Cargo;
- Salário.

Ela serve como classe-base para funcionários com funções específicas.

### 5 Cadastro de motoristas

A classe Motorista representa os motoristas da empresa, acrescentando informações como:

- Telefone;
- CNH.

### 6 Cadastro de atendentes

A classe Atendente representa os funcionários responsáveis pelo atendimento e possui um telefone para contato.

Foi criado também o método `telefonemas()`, que tem como objetivo exibir o número de telefone do atendente.

### 7 Cadastro de ônibus

A classe Onibus representa um veículo e possui informações como:

- Número;
- Capacidade;
- Quantidade de assentos ocupados;
- Preço.

### 8 Ônibus interestadual

A classe Onibus_interestadual adiciona características específicas desse tipo de transporte:

- Distância;
- Duração da viagem;
- Destino;
- Origem;
- Motorista;
- Passageiros;
- Preço;
- Assentos ocupados.

### 9 Ônibus rodoviário

A classe Onibus_rodoviario representa outro tipo de ônibus, possuindo informações relacionadas ao número do veículo e ao preço fixo.

## Temas abordados

Durante o desenvolvimento do projeto, foram abordados principalmente conceitos de Programação Orientada a Objetos, incluindo:

### Classes

As classes são utilizadas para representar entidades do sistema. Exemplos:

```python
class Pessoa:
class Passageiro(Pessoa):
class Funcionario(Pessoa, Companhia):
class Motorista(Funcionario, Companhia):
```

### Objetos

As classes permitem posteriormente criar objetos que representam pessoas, passageiros, funcionários, ônibus etc.

### Atributos

Os atributos representam as características dos objetos. Por exemplo:

```python
self.nome = nome
self.cpf = cpf
self.idade = idade
self.telefone = telefone
```

### Métodos

Os métodos representam comportamentos das classes, como:

```python
def nao_pagantes(self):
```

e

```python
def telefonemas(self):
```

### Herança

O projeto utiliza herança para aproveitar características de classes existentes. Por exemplo:

```python
class Passageiro(Pessoa):
```

Nesse caso, Passageiro herda características de Pessoa.

Também são utilizadas estruturas de herança múltipla, como:

```python
class Funcionario(Pessoa, Companhia):
```

### Construtor __init__

O método `__init__` é utilizado para inicializar os atributos dos objetos no momento de sua criação.

### Reutilização de código

A utilização de classes-base, como Pessoa, Funcionario e Onibus, permite organizar características comuns e reutilizá-las em classes especializadas.

## Tecnologias

O projeto utiliza recursos nativos da linguagem, principalmente:

- Classes;
- Objetos;
- Herança;
- Herança múltipla;
- Métodos;
- Atributos;
- Construtores;
- Estruturas condicionais.
- Lucidchart

## Bibliotecas

No projeto 1 não foi utilizado bibliotecas externas.

## Distribuição das Tarefas

Os três integrantes realizaram o trabalho em conjunto.
