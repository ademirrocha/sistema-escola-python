# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from aluno import Aluno
from form import Form
from seeds import Seeds
from disciplina import Disciplina
from prova import Prova

import os

class Menu(object):
	def __init__(self):
		print("\n\n 	Olá, bem vindo ao sistema da escola!")

	def menu(self):
		opcao = Form().menu()
		if(opcao == "1-1"):
			p = Form().cadastroAluno()
			Aluno().save(p.nome, p.idade)
		if(opcao == "1-2"):
			d = Form().cadastroDisciplina()
			Disciplina().save(d.nome)
		if(opcao == "1-3"):
			d = Form().cadastroProva()
			Prova().save(d.disciplina, d.pontos)
		if(opcao == "1-4"):
			d = Form().cadastroNota()
		if(opcao == "2-1"):
			Aluno().all()
		if(opcao == "2-2"):
			Disciplina().all()
		if(opcao == "2-3"):
			Prova().all()
		if(opcao == "3-3"):
			Prova().get(Form().pesquisaProva())
		if(opcao == "9"):
			clear = lambda: os.system('clear')
			clear()
		if(opcao != "x"):
			app.menu()

Seeds();
app = Menu()
app.menu()

print("Obrigado por usar nosso sistema. Volte sempre!")