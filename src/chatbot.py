from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar o Chatbot
chatbot = ChatBot('MeuBot')

# Criar um novo treinador para o Chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Treinar o Chatbot com o corpus em inglês
trainer.train('chatterbot.corpus.english')

# Loop para a interação com o Usuário
while True:
    user_input = input("Você: ")

    # Saia do loop se o Usuário digitar 'sair'
    if user_input.lower() == 'sair':
        break

    # Obtenha a resposta do Chatbot
    response = chatbot.get_response(user_input)

    # Imprima a resposta do Chatbot
    print("Bot:", response)
