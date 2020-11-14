# --- coding: cp1252 ---
# --- coding: utf-8 ---
from disciplina import Disciplina
from nota import Nota

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
		print('\n\n\n############################# Lista de Provas #############################')
		print('\n|--------------+---------------------+-------------+----------------------|')
		print('  ID Prova          Disciplina            Pontos               Status   ')
		print('|--------------+---------------------+-------------+----------------------|')
		for p in cls.objects:
			disciplina = list(filter(lambda x: x.id == p.disciplina, Disciplina().objects))
			print(' {:>6}        {:>16}         {:>7,.1f}    {:>21}'.format(p.id, disciplina[0].nome, p.pontos, p.status))
			print('|--------------+---------------------+-------------+----------------------|')
	
	def get(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		disciplina = list(filter(lambda x: x.id == prova[0].disciplina, Disciplina().objects))
		print('\n\n\n####################### Informações sobre a prova #########################')
		print("\n            Prova de {} valendo {} pontos.   ".format(disciplina[0].nome, prova[0].pontos))
		print("\n            ID da Prova {} - Status: {}.".format(prova[0].id, prova[0].status))
		
		if(prova[0].status != 'não realizada'):
			Nota().getNotas(prova[0].id)

	#return array com objeto prova e objeto disciplina
	def getOnlyData(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		disciplina = list(filter(lambda x: x.id == prova[0].disciplina, Disciplina().objects))
		return [prova[0], disciplina[0]]
			

	@classmethod
	def ids(self, options = 'todos'):
		array = []
		if(options == 'não realizada'):
			provas = list(filter(lambda x: x.status == 'não realizada', Prova().objects))
		elif(options == 'Realizada'):
			provas = list(filter(lambda x: x.status == 'Realizada', Prova().objects))
		else:
			provas = Prova().objects

		for p in provas:
			array.append(p.id)
		return array

	def atualizaStatus(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		prova[0].status = "Realizada"