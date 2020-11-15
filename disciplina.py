# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-


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
		print("\n\n#################################### Lista de disciplinas ###################################")
		print('\n|---------------+----------------------+-----------------------------+-----------------------|')
		print('  ID Disciplina        Disciplina             Notas Concluídas         Notas a Distribuir')
		print('|---------------+----------------------+-----------------------------+-----------------------|')
		for disc in self.objects:
			print(' {:>5}       {:>22}               {:<3.1f} de {:>5.1f}          {:>12.1f}'.format(disc.id, disc.nome, Disciplina().calcNotasDistribuidas(provas, disc.id), disc.notaTotal, (disc.notaTotal - Disciplina().calcNotasDistribuidas(provas, disc.id, 'Todos')) ) )
			print('|---------------+----------------------+-----------------------------+-----------------------|')
	


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
				if(Disciplina().calcNotasDistribuidas(provas, p.id, 'Todos') > 0):
					array.append(p.id)
		return array