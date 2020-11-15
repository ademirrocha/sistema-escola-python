# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from nota import Nota

class Disciplina (object):
	seq = 0
	objects = []
	
	def save(self, nome, notaTotal = 100):
		self.__class__.seq += 1
		self.id = self.__class__.seq
		self.nome = nome
		self.notaTotal = notaTotal
		self.__class__.objects.append(self)

	@classmethod
	def all(self, provas):
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' LISTA DE DISCIPLINAS '))
		print('\n|--------+-----------------------------+-----------------------------+-----------------------|')
		print(f"{'':3} {'ID':3} {'':10} {'DISCIPLINA':25} {'NOTAS CONCLUIDAS':27} {'NOTAS A DISTRIBUIR':25}")
		print('|--------+-----------------------------+-----------------------------+-----------------------|')
		for disc in self.objects:
			notasConcluidas = Disciplina().calcNotasDistribuidas(provas, disc.id)
			notasRestante = disc.notaTotal - Disciplina().calcNotasDistribuidas(provas, disc.id, 'Todos')
			print(f" {disc.id:4}  {'':9}   {disc.nome:15} {notasConcluidas:20.1f} {notasRestante:30.1f}")
			print('|--------+-----------------------------+-----------------------------+-----------------------|')
	


	def calcNotasDistribuidas(self, provas, id_disciplina, options = 'Realizada'):
		if(options == 'Realizada'):
			provasRealizadas = list(filter(lambda x: x.disciplina == id_disciplina and x.status == 'Realizada', provas))
		elif(options == 'não realizada'):
			provasRealizadas = list(filter(lambda x: x.disciplina == id_disciplina and x.status == 'não realizada', provas))
		else:
			provasRealizadas = list(filter(lambda x: x.disciplina == id_disciplina, provas))
		pontos = 0
		for prova in provasRealizadas:
			pontos = pontos + prova.pontos
		return pontos


	@classmethod
	def getData(self, id_disciplina):
		prova = list(filter(lambda x: x.id == id_disciplina, self.objects))
		return prova[0]



	@classmethod
	def ids(cls, options = None, provas = None):
		array = []
		for p in cls.objects:
			if(options == None):
				array.append(p.id)
			elif(options == 'Pontos Disponível'):
				if(Disciplina().calcNotasDistribuidas(provas, p.id, 'Todos') < p.notaTotal):
					array.append(p.id)
		return array


	#Total de notas por disciplina
	def getNotaAluno(self, matricula, provas):
		provas = list(filter(lambda x: x.disciplina == self.id and x.status == 'Realizada', provas))
		nota = 0
		for prova in provas:
			notaProva = list(filter(lambda x: x.prova == prova.id and x.aluno == matricula, Nota().objects))
			if(len(notaProva) == 0):
				self.save(prova.id, matricula, 0.0)
				notaProva = list(filter(lambda x: x.prova == prova.id and x.aluno == matricula, Nota().objects))
			nota += notaProva[0].nota

		return nota

