# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from disciplina import Disciplina
from prova import Prova
from aluno import Aluno
from nota import Nota

class Form(object):

	def cadastroAluno(self):
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' CADASTRO DE ALUNOS '))
		self.nome = input('\n------------- Digite o nome: ')
		self.idade = Form().inputInt('------------- Digite a idade: ', '\nErro: A idade deve ser um número.')
		return self

	def cadastroDisciplina(self):
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' CADASTRO DE DISCIPLINAS '))
		self.nome = input('\n------------- Digite o nome da disciplina: ')
		return self

	def cadastroProva(self):
		Disciplina().all(Prova().objects)
		idsDisciplina = Disciplina().ids('Pontos Disponível', Prova().objects)
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' CADASTRO DE PROVAS '))
		self.disciplina = Form().inputInt('\n------------- Digite o ID da disciplina conforme a lista acima: ', '\nErro: O ID da disciplina deve ser um número presente na lista acima.', idsDisciplina, '\nErro: Digite o ID de uma disciplina com notas a distribuir cisponível')
 
		disciplina = Disciplina().getData(self.disciplina)
		pontuacaoRestante = disciplina.notaTotal - Disciplina().calcNotasDistribuidas(Prova().objects, self.disciplina, "todos")
		
		self.pontos = Form().inputFloat('------------- Digite a quantidade de pontos que vale a prova: ', '\nErro: Os pontos da prova deve ser um número (casas decimais deve separados por . e não por , ).', pontuacaoRestante, '\nErro: Valor máximo de pontos deve ser menor ou igual a {} pontos.\n'.format(pontuacaoRestante))
		return self

	def cadastroNota(self):
		alunos = Aluno()
		dataProva = Prova().getOnlyData(Form().pesquisaProva(' 	não realizada', "\nErro: Pesquise por uma prova da lista e que não foi realizada ainda."))
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' INFORMAÇÕES SOBRE A PROVA '))
		print('\n{:>30} {}'.format(' ', "Prova de {} valendo {} pontos:".format(dataProva[1].nome, dataProva[0].pontos)))
		for aluno in alunos.objects:
			nota = Form().inputFloat('\n\n{:>30} {}'.format(' ', 'Digite a nota de {}: '.format(aluno.nome)), '\nErro: A nota deve ser um número (casas decimais devem separadas por .)', dataProva[0].pontos, 'Erro: Digite um número maior ou igual a 0 e menor ou igual a {}.'.format(dataProva[0].pontos))
			Nota().save(dataProva[0].id, aluno.matricula, nota)

		#Atualiza o status da prova pra "Realizada"
		Prova().atualizaStatus(dataProva[0].id)


	def menu(self):
		print('\n\n\n##############################################################################################')
		print("{:>30} {}".format(' ', ' MENU PRINCIPAL '))
		print("\n{:>30} {}".format(' ', " 1   ->    Cadastros"))
		print("{:>30} {}".format(' ', " 2   ->    Listar"))
		print("{:>30} {}".format(' ', " 3   ->    Pesquisar"))
		print("{:>30} {}".format(' ', " 9   ->    Limpar Tela"))
		print("{:>30} {}".format(' ', " x   ->    Sair do Sistema"))
		opcao = input("\n\n{:>30} {}".format(' ', 'Digite o valor do menu: '))
		if(opcao == "1"):
			print('\n\n\n##############################################################################################')
			print("{:>30} {}".format(' ', ' SUBMENU -> CADASTROS '))
			print("\n{:>30} {}".format(' ', " 1   ->   Cadastrar Aluno"))
			print("{:>30} {}".format(' ', " 2   ->   Cadastrar Disciplina"))
			print("{:>30} {}".format(' ', " 3   ->   Cadastrar Prova"))
			print("{:>30} {}".format(' ', " 4   ->   Cadastrar Notas de uma prova"))
			print("{:>30} {}".format(' ', " 0   ->   Retornar ao menu anterior"))
			o = input("\n\n{:>30} {}".format(' ', 'Digite o valor do submenu: '))
			if(o == "1"):
				opcao = '1-1'
			elif (o == "2"):
				opcao = '1-2'
			elif (o == "3"):
				opcao = '1-3'
			elif (o == "4"):
				opcao = '1-4'
			elif(o == "0"):
				Form().menu()

		if(opcao == "2"):
			print('\n\n\n##############################################################################################')
			print("{:>30} {}".format(' ', ' SUBMENU -> LISTAR '))
			print("\n{:>30} {}".format(' ', " 1   ->   Lista de Alunos"))
			print("{:>30} {}".format(' ', " 2   ->   Lista de Disciplinas"))
			print("{:>30} {}".format(' ', " 3   ->   Lista de Provas"))
			print("{:>30} {}".format(' ', " 0   ->   Retornar ao menu anterior"))
			o = input('\n\n{:>30} {}'.format(' ', 'Digite o valor do submenu: '))
			if(o == "1"):
				opcao = '2-1'
			elif (o == "2"):
				opcao = '2-2'
			elif (o == "3"):
				opcao = '2-3'
			elif(o == "0"):
				Form().menu()
		if(opcao == "3"):
			print('\n\n\n##############################################################################################')
			print("{:>30} {}".format(' ', ' SUBMENU -> PESQUISAR '))
			
			print("\n{:>30} {}".format(' ', " 1   ->   Pesquisar Aluno"))
			print("{:>30} {}".format(' ', " 2   ->   Pesquisar Disciplina"))
			print("{:>30} {}".format(' ', " 3   ->   Pesquisar Prova"))
			print("{:>30} {}".format(' ', " 0   ->   Retornar ao menu anterior"))
			o = input('\n\n{:>30} {}'.format(' ', ' Digite o valor do submenu: '))
			if(o == "1"):
				opcao = '3-1'
			elif (o == "2"):
				opcao = '3-2'
			elif (o == "3"):
				opcao = '3-3'
			elif(o == "0"):
				Form().menu()

		return opcao

	def pesquisaProva(self, options = 'todos', otherError = None):
		Prova().all()
		idsProva = Prova().ids(options)
		
		return Form().inputInt('\n{:>20} {}'.format(' ', 'Digite o ID da prova conforme a lista acima: '), '\nErro: O ID da prova deve ser um numero presente na lista acima.', idsProva, otherError)


	def pesquisaAluno(self, options = 'todos', otherError = None):
		Aluno().all()
		matriculas = Aluno().matriculas()
		return Form().inputInt('\n{:>20} {}'.format(' ', 'Digite a matricula do aluno conforme a lista acima: '), '\nErro: A matricula deve ser um numero presente na lista acima.', matriculas, otherError)


	def inputFloat(self, caption, errCaption, lessOrEqual = None, otherError = None):
		x = None
   
		while True:
			try:
				x = float(input(caption))
				if(lessOrEqual == None):
					break
				elif(x <= lessOrEqual and x >= 0.0):
					break
				elif(lessOrEqual != None):
					if(otherError == None):
						otherError = errCaption
					print(otherError)
			except ValueError:
				print(errCaption)
		return x

	def inputInt(self, caption, errCaption, idsDisciplina = None, otherError = None):
		x = None
		while True:
			try:
				x = int(input(caption))
				if(idsDisciplina == None):
					break
				elif(x in idsDisciplina):
					break
				elif(idsDisciplina != None):
					if(otherError == None):
						otherError = errCaption
					print(otherError)
			except ValueError:
				print(errCaption)
		return x

