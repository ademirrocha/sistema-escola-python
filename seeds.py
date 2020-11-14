# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from aluno import Aluno
from disciplina import Disciplina
from prova import Prova
from nota import Nota

class Seeds(object):
	def __init__(self):
		if(len(Aluno().objects) == 0):
			Aluno().save('João', 12)
			Aluno().save('Maria', 11)
			Aluno().save('Gabriela', 14)
		if(len(Disciplina().objects) == 0):
			Disciplina().save('Matemática')
			Disciplina().save('Português')
			Disciplina().save('História')
		if(len(Prova().objects) == 0):
			Prova().save(1, 10.0)
			Prova().save(2, 10.0)
			Prova().save(3, 15.0)
		if(len(Nota().objects) == 0):
			Nota().save(1, 1, 7.0)
			Nota().save(1, 2, 5.5)
			Nota().save(1, 3, 8.0)
			Prova().atualizaStatus(1)