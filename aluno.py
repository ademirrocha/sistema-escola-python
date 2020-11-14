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
		print("\n\nLista de alunos:")
		for p in cls.objects:
			print('Matricula: {} - Nome: {} - Idade: {}'.format(p.matricula, p.nome, p.idade))


	