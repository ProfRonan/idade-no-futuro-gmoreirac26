ano_atual = int(input('digite sua o ano atual: '))
idade_atual = int(input('digite sua idade atual: '))
outro_ano = int(input('digite um ano próximo, para saber a sua idade nesse ano: '))
nome = (input('por ultimo, digite seu nome: '))
idade_outro_ano = idade_atual + (outro_ano - ano_atual)

print(f'{nome},no ano de {outro_ano} você terá {idade_outro_ano} anos')