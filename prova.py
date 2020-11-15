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
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' LISTA DE PROVAS '))
		print('\n|---------------+--------------------------------+-----------------+-------------------------|')
		print(f"{'':5} {'ID':10} {'':8}  {'DISCIPLINA':28} {'PONTOS':22} {'STATUS':25}")
		print('|---------------+--------------------------------+-----------------+-------------------------|')
		for p in cls.objects:
			disciplina = list(filter(lambda x: x.id == p.disciplina, Disciplina().objects))
			print(f"{p.id:7} {'':17}  {disciplina[0].nome:11} {p.pontos:22.1f} {'':15} {p.status:25}")
			print('|---------------+--------------------------------+-----------------+-------------------------|')
	
	def get(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		disciplina = list(filter(lambda x: x.id == prova[0].disciplina, Disciplina().objects))
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' INFORMAÇÕES SOBRE A PROVA '))
		print('\n{:>20} {}'.format(' ', "Prova de {} valendo {} pontos.   ".format(disciplina[0].nome, prova[0].pontos)))
		print("\n{:>20} {}".format(' ', "ID da Prova {} - Status: {}.".format(prova[0].id, prova[0].status)))
		
		if(prova[0].status != 'não realizada'):
			Nota().getNotas(prova[0].id)

	#return array com objeto prova e objeto disciplina
	def getOnlyData(self, id_prova):
		prova = list(filter(lambda x: x.id == id_prova, self.__class__.objects))
		disciplina = list(filter(lambda x: x.id == prova[0].disciplina, Disciplina().objects))
		return [prova[0], disciplina[0]]

	#return objeto disciplina
	def getDisciplina(self):
		disciplina = list(filter(lambda x: x.id == self.disciplina, Disciplina().objects))
		return disciplina[0]
			

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


	def getProvaByAluno(self, matricula):
		idsProvas = Prova().ids('Realizada')
		provas = list(filter(lambda x: x.id in idsProvas, Prova().objects))

		if(len(provas) > 0):
			print('\n\n|-----------------------+-------------------+-------------------+-----------------------|')
			print('     Disciplina             Valor                Pontuação          Aproveitamento')
			print('|-----------------------+-------------------+-------------------+-----------------------|')
			for prova in provas:
				nota = Nota().getNotaAluno(prova.id, matricula)
				
				print('     {:>10}       {:>10,.1f} pontos   {:>10,.1f} pontos        {:>10}%'.format(prova.getDisciplina().nome, prova.pontos, nota, (nota / prova.pontos * 100)))
				print('|-----------------------+-------------------+-------------------+-----------------------|')


		else:
			print('\n\n------------------------ Nenhuma prova realizada ainda! -------------------------------')

		
