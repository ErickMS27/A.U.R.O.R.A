import nltk
from nltk.chat.util import Chat, reflections

answers = [
    [
        
        r"(.*)",
        ["Desculpe, eu não entendi.", "Poderia reformular a pergunta?", 
         "Eu não tenho certeza do que você está falando.", "Não consegui compreender, poderia repetir a pergunta?"]
    ]
]

chatbot = Chat(answers, reflections)

def start_chat():
    print("\nOlá! Me chamo Aurora! Sou uma I.A gerada para te ajudar!")
    print("Como posso ajudar você hoje?")
    while True:
        input_data = input("\nVocê: ")  
        answer = chatbot.respond(input_data)  
        print("A.U.R.O.R.A: " + answer) 
        if input_data.lower() == "adeus":
            print("Até mais!") 
            break
        elif input_data.lower() == "reiniciar":
            print("Reiniciando o chat...")
            start_chat()
            break

if __name__ == "__main__":
    nltk.download("punkt", quiet=True)
    start_chat()
