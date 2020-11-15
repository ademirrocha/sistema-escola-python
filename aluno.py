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
		print("\n\n####################### Lista de alunos ######################")
		print('\n|--------------+---------------------------+-----------------|')
		print('  Matricula                Nome                  Idade   ')
		print('|--------------+---------------------------+-----------------|')
		
		for p in cls.objects:
			print('  {:>5}          {:>15}      {:13} anos'.format(p.matricula, p.nome, p.idade))
			print('|--------------+---------------------------+-----------------|')


	