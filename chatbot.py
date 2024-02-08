# Projeto 3 - Construindo um ChatBot personalizado com GPT-4 e Linguagem Python
# Os parâmetros são customizáveis e seguem o padrão conforme documentação: https://platform.openai.com/docs/api-reference/introduction

# Import
import openai

# Chave
openai.api_key = "sk-3nv4v394nv34nvn34onfv3p4n34oieorvn4"

# Função para gerar texto a partir do modelo de linguagem
def gera_texto(texto):
	
	# Obtém a resposta do modelo de linguagem
	response = openai.Completion.create(

		# Modelo utilizado
		# Outros modelos estão disponíveis em: https://platform.openai.com/account/rate-limits
		engine = "text-davinci-003",

		# Texto inicial da conversa com o chatbot
		prompt = texto,

		# Comprimento da resposta gerada pelo modelo
		max_tokens = 150,

		# Número de conclusões para cada prompt
		n = 5,

		# O texto retornado não obterá a sequencia de parada
		stop = None,

		# Medida de aleatoriedade de texto gerada pelo modelo. Seu valor está entre 0 e 1
		# Valores próximos a 1 significam saídas mais aleatórias. Enquanto valores próximos a 0 indicam saídas previsíveis.
		temperature = 0.8,
	)

	return response.choices[0].text.strip()

# Função principal do programa em Python
def main():

	print("\nBem-vindo ao GPT-4 ChatBot do Projeto 3 da DSA")
	print("(Digite 'sair' a qualquer momento para encerrar o chat)")

	# Loop
	while true:

		# Coleta a pergunta digitada pelo usuário
		user_message = input("\nVocê: ")

		# Se a mensagem for 'sair' finaliza o programa
		if user_message.lower() == "sair":
			break

		# Coloca a mensagem digitada pelo usuário na variável Python chamada gpt4_prompt
		gpt4_prompt = f"\nUsuário: {user_message}\nChatbot:"

		# Obtém a resposta do modelo executando a função gera_texto()
		chatbot_response = gera_texto(gpt4_prompt)

		# Imprime a resposta do chatbot
		print(f"\nChatbot: {chatbot_response}")

# Execução do programa (bloco main) em Python
if __name__ == "__main__":
	main()



