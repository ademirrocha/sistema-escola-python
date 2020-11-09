# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-

class Disciplina (object):
	seq = 0
	objects = []
	
	def save(self, nome):
		self.__class__.seq += 1
		self.id = self.__class__.seq
		self.nome = nome
		self.__class__.objects.append(self)

	@classmethod
	def all(cls):
		print("\n\nLista de disciplinas:")
		for p in cls.objects:
			print('ID: {} - Disciplina: {}'.format(p.id, p.nome))