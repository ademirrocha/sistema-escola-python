# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from disciplina import Disciplina
from prova import Prova

class Form(object):

	def cadastroAluno(self):
		self.nome = input('Digite o nome: ')
		self.idade = Form().inputInt('\nDigite a idade: ', '\nErro: A idade deve ser um número.')
		return self

	def cadastroDisciplina(self):
		print('\n\nCadastro de Disciplina:')
		self.nome = input('\nDigite o nome da disciplina: ')
		return self

	def cadastroProva(self):
		Disciplina().all()
		idsDisciplina = Disciplina().ids()
		print('\n\nCadastro de Prova:')
		self.disciplina = Form().inputInt('\nDigite o ID da disciplina conforme a lista acima: ', '\nErro: O ID da disciplina deve ser um número presente na lista acima.', idsDisciplina)
		self.pontos = Form().inputFloat('\nDigite a quantidade de pontos que vale a prova: ', '\nErro: Os pontos da prova deve ser um número (casas decimais deve separados por . e não por , ).')
		return self

	def menu(self):
		print("\n\nMenu")
		print("1 -> Cadastros")
		print("2 -> Listar")
		print("3 -> Pesquisar")
		print("9 -> Limpar Tela")
		print("x -> Sair do Sistema")
		opcao = input('\n\nDigite o valor do menu: ')
		if(opcao == "1"):
			print("\nSubmenu - Cadastro")
			print("1 -> Cadastrar Aluno")
			print("2 -> Cadastrar Disciplina")
			print("3 -> Cadastrar Prova")
			print("0 -> Retornar ao menu anterior")
			o = input('\n\nDigite o valor do submenu: ')
			if(o == "1"):
				opcao = '1-1'
			elif (o == "2"):
				opcao = '1-2'
			elif (o == "3"):
				opcao = '1-3'
			elif(o == "0"):
				Form().menu()

		if(opcao == "2"):
			print("\nSubmenu - Listar")
			print("1 -> Lista de Alunos")
			print("2 -> Lista de Disciplinas")
			print("3 -> Lista de Provas")
			print("0 -> Retornar ao menu anterior")
			o = input('\n\nDigite o valor do submenu: ')
			if(o == "1"):
				opcao = '2-1'
			elif (o == "2"):
				opcao = '2-2'
			elif (o == "3"):
				opcao = '2-3'
			elif(o == "0"):
				Form().menu()
		if(opcao == "3"):
			print("\nSubmenu - Pesquisar")
			print("1 -> Pesquisar Aluno")
			print("2 -> Pesquisar Disciplina")
			print("3 -> Pesquisar Prova")
			print("0 -> Retornar ao menu anterior")
			o = input('\n\nDigite o valor do submenu: ')
			if(o == "1"):
				opcao = '3-1'
			elif (o == "2"):
				opcao = '3-2'
			elif (o == "3"):
				opcao = '3-3'
			elif(o == "0"):
				Form().menu()

		return opcao

	def pesquisaProva(self):
		Prova().all()
		idsProva = Prova().ids()
		return Form().inputInt('\nDigite o ID da prova conforme a lista acima: ', '\nErro: O ID da prova deve ser um numero presente na lista acima.', idsProva)


	def inputFloat(self, caption, errCaption):
		x = None
   
		while True:
			try:
				x = float(input(caption))
				break
			except ValueError:
				print(errCaption)
		return x

	def inputInt(self, caption, errCaption, idsDisciplina = None):
		x = None
		while True:
			try:
				x = int(input(caption))
				if(idsDisciplina == None):
					break
				elif(x in idsDisciplina):
					break
				elif(idsDisciplina != None):
					print(errCaption)
			except ValueError:
				print(errCaption)
		return x


