
version = "1.4.0"


def intro():
	msg = "Assistente - version {} / by: AGNALDO KLEIN".format(version)
	print("-" * len(msg) +  "\n{}\n".format(msg)  +   "-" * len(msg))


lista_erros = [
		"Não entendi nada",
		"Desculpe, não entendi",
		"Repita novamente por favor"
]

conversas = {
	"Olá": "oi, tudo bem?, Quer saber quais as TÉCNICAS DE LEVANTAMENTO DE REQUISITOS cadastradas em nosso sistema?",
	"sim": "As técnicas disponíveis são, Entrevistas, Pesquisas e Questionários, Reuniões e Cenários, Grupo Focal, Brainstotrms e JAD/RAD, gostaria de saber qual a melhor técnica para sua empresa?",
	"gostaria": "Quantos funcionários trabalham em sua empresa?",

	"10": "Existem duas tecnicas que podem ser aplicadas em sua empresa. . Sua empresa possui um funcionário especilista em tecnologia?. se sim  diga '01' se não '02'",
	"01": "A melhor técnica para ser aplicada em sua empresa é a Grupo Focal. . Grupo Focal é considerado uma técnica de coleta de dados específicos das pesquisas com abordagem qualitativa, por proporcionar a interação grupal para a produção de dados que seriam menos acessíveis fora do contexto interacional. Com essa técnica é possível coletar dados, diretamente, dos depoimentos de um grupo, que faz o relato de suas experiências e percepções, em torno de um tema de interesse coletivo",
	"02": "A melhor técnica para ser aplicada em sua empresa é a Entrevista. . esta técnica consiste em reuniões com os stakeholders, formais ou informais, onde coloca-se questões formuladas pela equipe de engenharia de requisitos sobre o processo de trabalho atual do cliente e sobre o sistema que será desenvolvido. Devido a isso, a entrevista está presente na maioria dos processos de elaboração de requisitos, pois a partir dela que poderá surgir a necessidade da utilização de outras técnicas",

	"20": "Existem duas tecnicas que podem ser aplicadas . . Sua empresa possui algum stakeholders? . . se sim  diga '03' se não '04'.",
	"03": "A melhor técnica para ser aplicada em sua empresa é a Pesquisas e questionários . . Então, a técnica de questionários consiste na elaboração de um conjunto de perguntas que guiarão um stakeholder ou um grupo deles a respondê-las. Essa técnica não apresenta diretrizes bem definidas, mas existem recomendações diversas feitas por vários autores sobre como utilizar a técnica para fazer o levantamento de requisitos, devendo usar perguntas claras e objetivas, para potencializar o resultado",
	"04": "A melhor técnica para ser aplicada em sua empresa é a Reuniões e cenários . . A construção de cenários busca aproximar do mundo real o funcionamento do sistema a ser desenvolvido, ou seja, uma descrição dos fluxos de informações expondo de forma simplista o que os usuários esperam que ocorra em diversas situações é elaborada com o intuito de um melhor e total entendimento das necessidades e casos específicos que talvez não foram colocados em outras fases do processo de elicitação de requisitos do sistema",


	"30": "Existem duas tecnicas que podem ser aplicadas . . Sua empresa possui um alto nível de stakeholders? . . se sim  diga '05' se não '06'.",
	"05": "A melhor técnica para ser aplicada em sua empresa é a Brainstorms . .  princípio básico desta tecnica é reunir um conjunto de especialistas (sistemas e negócios) para que cada um possa inspirar ao outro o surgimento de ideias que possam vir a contribuir para resolver o problema em uma ou várias reuniões",
	"06": "A melhor técnica para ser aplicada em sua empresa é a  JAD/RAD. . O JAD facilita a criação de uma visão compartilhada do que o produto de software deve ser, então através da sua utilização os desenvolvedores ajudam os usuários a formular problemas e explorar soluções, desse modo, os usuários ganham um sentimento de envolvimento, posse e responsabilidade com o sucesso do produto",


	"100": ", para saber mais sobre a técnica diga '01'",
	"01000000" : "A técnica consiste em reuniões com os stakeholders, formais ou informais, onde coloca-se questões formuladas pela equipe de engenharia de requisitos sobre o processo de trabalho atual do cliente e sobre o sistema que será desenvolvido. Devido a isso, a entrevista está presente na maioria dos processos de elaboração de requisitos, pois a partir dela que poderá surgir a necessidade da utilização de outras técnicas",

	"200": "A melhor técnica para ser aplicada em sua empresa é a Pesquisas e Questionários, para saber mais sobre a técnica diga '02'",
	"02000000000" : "a técnica de questionários, consiste na elaboração de um conjunto de perguntas que guiarão um stakeholder ou um grupo deles à responde-las. Essa técnica não apresenta diretrizes bem definidas, mas existem recomendações diversas feitas por vários autores sobre como utilizar a técnica para fazer o levantamento de requisitos, devendo usar perguntas claras e objetivas, para potencializar o resultado",

	"300": "A melhor técnica para ser aplicada em sua empresa é a Reuniões e Cenários, para saber mais sobre a técnica diga '03'",
	"030000" : "A construção de cenários busca aproximar do mundo real o funcionamento do sistema a ser desenvolvido, ou seja, uma descrição dos fluxos de informações expondo de forma simplista o que os usuários esperam que ocorra em diversas situações é elaborada com o intuito de um melhor e total entendimento das necessidades e casos específicos que talvez não foram colocados em outras fases do processo de elicitação de requisitos do sistema",

	"400": "A melhor técnica para ser aplicada em sua empresa é a Grupo Focal, para saber mais sobre a técnica diga '04'",
	"0400000" : "O grupo focal é considerado uma técnica de coleta de dados específicos das pesquisas com abordagem qualitativa, por proporcionar a interação grupal para a produção de dados que seriam menos acessíveis fora do contexto interacional. Com essa técnica é possível coletar dados, diretamente, dos depoimentos de um grupo, que faz o relato de suas experiências e percepções, em torno de um tema de interesse coletivo",

	"500": "A melhor técnica para ser aplicada em sua empresa é a Brainstorms , para saber mais sobre a técnica diga '05'",
	"05000000000" : "Brainstorming, ou tempestade de ideias, é uma técnica para geração de ideias muito usada em dinâmicas de grupo com o objetivo de entender de forma mais ampla as necessidades dos usuários, estimulante que seus participantes desenvolvam ideias criativa",

	"600": "A melhor técnica para ser aplicada em sua empresa é a JAD/RAD, para saber mais sobre a técnica diga '06'",
	"0600000000" : "aqui vai ficar uma breve explicação sobre JAD/RAD",
}

comandos = {
	"desligar": "desligando",
	"reiniciar": "reiniciando"
}


def verifica_nome(user_name):
	if user_name.startswith("Meu nome é"):
		user_name = user_name.replace("Meu nome é", "")
	if user_name.startswith("Eu me chamo"):
		user_name = user_name.replace("Eu me chamo", "")
	if user_name.startswith("Eu sou o"):
		user_name = user_name.replace("Eu sou o", "")
	if user_name.startswith("Eu sou a"):
		user_name = user_name.replace("Eu sou a", "")

	return user_name 


def  verifica_nome_exist(nome):
	dados = open("dados/nomes.txt", "r")
	nome_list = dados.readlines()

	if not nome_list:
		vazio = open("dados/nomes.txt", "r")
		conteudo = vazio.readlines()
		conteudo.append("{}".format(nome))
		vazio = open("dados/nomes.txt", "w")
		vazio.writelines(conteudo)
		vazio.close()

		return "Olá {}, prazer em te conhecer!".format(nome)

	for linha in nome_list:
		if linha == nome:
			return "Olá {}, acho que já nos conhecemos".format(nome)

	vazio = open("dados/nomes.txt", "r")
	conteudo = vazio.readlines()
	conteudo.append("\n{}".format(nome))
	vazio = open("dados/nomes.txt", "w")
	vazio.writelines(conteudo)
	vazio.close()

	return "Oi {} é a primeira vez que nos falamos".format(nome)


def name_list():
	try:
		nomes = open("dados/nomes.txt", "r")
		nomes.close()

	except FileNotFoundError:
		nomes = open("dados/nomes.txt", "w")
		nomes.close()
