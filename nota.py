# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from aluno import Aluno

class Nota(object):
	objects = []
	
	def save(self, prova, aluno, nota):
		self.prova = prova
		self.aluno = aluno
		self.nota = nota
		self.__class__.objects.append(self)

	def getNotas(self, id_prova):
		alunos = Aluno()
		print('\n\n\n################## Notas dos Alunos ####################')
		print('\n|-----------------------------+------------------------|')
		print('            Aluno                         Nota          ')
		print('|-----------------------------+------------------------|')
		for aluno in alunos.objects:
			nota = Nota().getNotaAluno(id_prova, aluno.matricula)
			print('   {:>13}                   {:>10,.1f}   '.format(aluno.nome, nota))
			print('|-----------------------------+------------------------|')

	def getNotaAluno(self, id_prova, matricula_aluno):
		nota = list(filter(lambda x: x.prova == id_prova and x.aluno == matricula_aluno, Nota().objects))
		if(len(nota) == 0):
			self.save(id_prova, matricula_aluno, 0)
			nota = list(filter(lambda x: x.prova == id_prova and x.aluno == matricula_aluno, Nota().objects))
		
		return nota[0].nota



