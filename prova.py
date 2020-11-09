# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from disciplina import Disciplina
class Prova (object):
	seq = 0
	objects = []
	
	def save(self, disciplina, pontos, status = 'não realizada'):
		self.__class__.seq += 1
		self.id = self.__class__.seq
		self.disciplina = disciplina
		self.pontos = pontos
		self.status = status 
		self.__class__.objects.append(self)

	@classmethod
	def all(cls):
		print("\n\nLista de Provas:")
		for p in cls.objects:
			disciplina = list(filter(lambda x: x.id == p.disciplina, Disciplina().objects))
			print('ID Prova: {} - Disciplina: {} - Pontos: {} - Status: {}'.format(p.id, disciplina[0].nome, p.pontos, p.status))

	
	def get(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		disciplina = list(filter(lambda x: x.id == prova[0].disciplina, Disciplina().objects))
		print("\n\nProva de {} valendo {} pontos.".format(disciplina[0].nome, prova[0].pontos))
		print("\nID da Prova {} - Status: {}.".format(prova[0].id, prova[0].status))

		#for p in cls.objects:
			#print('Matricula: {} - Nome: {} - Idade: {}'.format(p.matricula, p.nome, p.idade))