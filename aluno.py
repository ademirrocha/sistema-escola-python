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
	



	def get(self, matricula, provas, disciplinas):
		aluno = list(filter(lambda x: x.matricula == matricula, self.__class__.objects))
	
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ',' INFORMAÇÕES SOBRE O ALUNO '))
		
		print("\n 		Matrícula: {}  |  Nome: {}  | Idade: {} anos.   ".format(aluno[0].matricula, aluno[0].nome, aluno[0].idade))
		
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ',' PROVAS REALIZADAS '))
		
		provas.getProvaByAluno(matricula)

		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' SITUAÇÃO ESCOLAR DO ALUNO POR DISCIPLINA'))
		
		print('\n\n{:>43}'.format(' Critérios de avaliação:'))
		print('\n{:>15} {}'.format(' ', "* Abaixo de 40% Reprovado"))
		print('{:>15} {}'.format(' ', "* Maior que '40%' e menor que '60%' Em recuperação"))
		print('{:>15} {}'.format(' ', "* Igual ou superior a 60% Aprovado"))

		Aluno().situacaoAluno(aluno[0], provas.objects, disciplinas)


		
	@classmethod
	def matriculas(self):
		array = []
		alunos = Aluno().objects
		for aluno in alunos:
			array.append(aluno.matricula)
		return array




	def situacaoAluno(self, aluno, provas, disciplinas):

		print('\n|------------------------+----------------------+--------------------+-----------------------|')
		print(f"{'':5} {'DISCIPLINA':10} {'':10}  {'TOTAL DE PONTOS':20} {'PONTUACAO DO ALUNO':27} {'SITUACAO':10}")
		print('|------------------------+-------------------------------------------+-----------------------|')
			

		for disciplina in disciplinas:
			pontosDistribuidos = disciplina.calcNotasDistribuidas(provas, disciplina.id, options = 'Realizada')
			pontuacaoRestante = disciplina.notaTotal - disciplina.calcNotasDistribuidas(provas, disciplina.id, options = 'todos')
			notaAluno = disciplina.getNotaAluno(aluno.matricula, provas)
			if(pontuacaoRestante == 0):
				if((notaAluno / pontosDistribuidos * 100) < 40):
					situacao = 'Reprovado'
				elif( pontosDistribuidos > 0 and (notaAluno / pontosDistribuidos * 100) >= 40 and (notaAluno / pontosDistribuidos * 100) < 60):
					situacao = 'Em recuperação'
				else:
					situacao = 'Aprovado'
			elif(pontosDistribuidos < disciplina.notaTotal and pontosDistribuidos > 0):
				if((notaAluno / pontosDistribuidos * 100) < 40):
					situacao = 'Risco de reprovação'
				elif((notaAluno / pontosDistribuidos * 100) >= 40 and (notaAluno / pontosDistribuidos * 100) < 60):
					situacao = 'Risco de recuperação'
				else:
					situacao = 'Pré-aprovado'
			else:
				situacao = 'Aguardando notas'
			print(f"{'':4} {disciplina.nome:23} {disciplina.notaTotal:10.1f} {'':15} {notaAluno:.1f} de {pontosDistribuidos:1.1f} {'':6} {situacao:25}")
			print('|------------------------+-------------------------------------------+-----------------------|')
			


