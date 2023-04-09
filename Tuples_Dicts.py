# >>Tuples<<

'''Nesse caso, a variável cadastro recebeu como valor uma tupla de 3 elementos: um nome, um número float 
(correspondente à altura de Mariana, em metros) e um objeto do tipo datetime 
que corresponde à data de nascimento de Mariana.'''

# No exemplo a seguir é necessário importar a biblioteca datetime para reproduzi-lo:

import datetime

cadastro = ('Mariana', 1.65, datetime.datetime(1982, 5, 12))

cadastro = 'Mariana', 1.65, datetime.datetime(1982, 5, 12)

print(cadastro)

# ('Mariana', 1.65, datetime.datetime(1982, 5, 12, 0, 0))

'''Tuplas também podem ser acessadas pelo índice. Na nossa tupla de três elementos, fica assim:'''

cadastro[0]

# 'Mariana'

cadastro[1]

# 1.65

cadastro[2]

# datetime.datetime(1982, 5, 12, 0, 0)

'''Note que, nas tuplas, haverá uma preocupação maior com a ordem das coisas. 
Normalmente essa ordem é definida pelo(a) programador(a), de acordo com a circunstância e conveniência.'''

'''Uma observação importante sobre o uso de uma tupla é que, se ela tiver um único item, 
será necessário colocar uma vírgula depois dele, senão o Python entende que o objeto que está sendo atribuído no item é do tipo valor.'''

# Por exemplo:

minha_tupla = 2,

meu_numero_inteiro = 2

print(type(minha_tupla), type(meu_numero_inteiro))

# <class 'tuple'> <class 'int'>

'''Na saída desse trecho de código, você pode notar que o tipo da variável minha_tupla é «tuple», 
enquanto meu_numero_inteiro é um «int».'''

'''IMPORTANTE! No Brasil, costumamos usar vírgula como separador das casas decimais de um número real. 
Já, em Python, o separador decimal é o ponto «.» — a vírgula é usada para separar elementos em listas, 
tuplas, argumentos de funções etc.'''

# Além disso, o enclausurador parênteses «()» pode ser usado para quebrar linhas longas em Python. Por exemplo:

minha_tupla_longa = ('primeiro elemento da tupla', 
2.5, 300,
'quarto elemento da tupla',
None)

print(minha_tupla_longa)

# ('primeiro elemento da tupla', 2.5, 300, 'quarto elemento da tupla', None)

# >>Dicts<<

'''As principais operações em um dicionário são armazenar um valor com alguma chave e/ou extrair o valor fornecido pela chave. 
Por isso, é muito utilizado quando é necessário armazenar dados de forma organizada e que possuem identificação única 
(como acontece em bancos de dados).'''

# Veja um exemplo muito simples de uso de um dicionário: converter o nome de uma cidade do Brasil em seu prefixo de DDD.

cidade_para_codigo = {'FRANÇA': 16, 'SÃO SEBASTIÃO': 12, 'SÃO PAULO': 11}

print(cidade_para_codigo)

# {'FRANÇA': 16, 'SÃO SEBASTIÃO': 12, 'SÃO PAULO': 11}

cidade_para_codigo['FRANÇA']

# 16

'''Se você tentar resgatar o valor de uma chave que não foi cadastrada no dicionário, 
será retornado um erro. Para isso, o método de dicionários .get() pode funcionar como alternativa, 
retornando um valor padrão quando não houver chave cadastrada:'''

cidade_para_codigo['CAMPINAS']

# KeyError: 'CAMPINAS'

cidade_para_codigo.get('CAMPINAS', 'Código não cadastrado')

# 'Código não cadastrado'