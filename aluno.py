# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from pessoa import Pessoa


class Aluno (object):
	seq = 0
	objects = []
	
	def save(self, nome, idade):
		Pessoa.__init__(self, nome, idade)
		self.__class__.seq += 1
		self.matricula = self.__class__.seq
		self.__class__.objects.append(self)

	@classmethod
	def all(cls):
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' LISTA DE ALUNOS '))
		print('\n|------------------------+-------------------------------------------+-----------------------|')
		print(f"{'':5} {'MATRICULA':10} {'':23}  {'NOME':35} {'IDADE':45}")
		print('|------------------------+-------------------------------------------+-----------------------|')
		for p in cls.objects:
			print(f"{p.matricula:10} {'':30}  {p.nome:30} {p.idade:8} anos")
			print('|------------------------+-------------------------------------------+-----------------------|')
	



	def get(self, matricula, provas):
		aluno = list(filter(lambda x: x.matricula == matricula, self.__class__.objects))
	
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ',' INFORMAÇÕES SOBRE O ALUNO '))
		
		print("\n 		Matrícula: {}  |  Nome: {}  | Idade: {} anos.   ".format(aluno[0].matricula, aluno[0].nome, aluno[0].idade))
		
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ',' PROVAS REALIZADAS '))
		
		provas.getProvaByAluno(matricula)

		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' SITUAÇÃO ESCOLAR DO ALUNO '))
		
		print('\n\n{:>43}'.format(' Critérios de avaliação:'))
		print('\n{:>15} {}'.format(' ', "* Abaixo de 40% Reprovado"))
		print('{:>15} {}'.format(' ', "* Maior que '40%' e menor que '60%' Em recuperação"))
		print('{:>15} {}'.format(' ', "* Acima de 60% Aprovado"))
		
	@classmethod
	def matriculas(self):
		array = []
		alunos = Aluno().objects
		for aluno in alunos:
			array.append(aluno.matricula)
		return array




	def situacaoAluno(self, matricula):
		disciplina = Disciplina().getData(prova.disciplina)
		pontuacaoRestante = disciplina.notaTotal - Disciplina().calcNotasDistribuidas(Prova().objects, prova.disciplina, options = 'todos')
		if(pontuacaoRestante == 0):
			if((prova.pontos * nota / 100 * 10) < 4):
				situacao = 'Reprovado'
			elif((prova.pontos * nota / 100 * 10) >= 4 and (prova.pontos * nota / 100 * 10) < 4):
				situacao = 'Em recuperação'
			else:
				situacao = 'Aprovado'
		else:
			if((prova.pontos * nota / 100 * 10) < 4):
				situacao = 'Risco de reprovação'
			elif((prova.pontos * nota / 100 * 10) >= 4 and (prova.pontos * nota / 100 * 10) < 6):
				situacao = 'Risco de recuperação'
			else:
				situacao = 'Pré-aprovado'
		return situacao

