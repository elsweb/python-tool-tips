from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot("chatbot", read_only=False, 
    logic_adapters= [{
            "import_path":"chatterbot.logic.BestMatch",
            "default_response":"Sorry I dont' have an answer",
            "maximum_similarity_threshold": 0.9
            }])
trainer = ListTrainer(bot)
trainer_cp = ChatterBotCorpusTrainer(bot)
trainer_cp.train(
    "chatterbot.corpus.Portuguese.conversations"
)

# trainer.train(['Olá','precisa? 1',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 2',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 3',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 4',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 5',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 6',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 7',' Qual seu nome?' ,'sou uma ia'])
# trainer.train(['Olá','precisa? 8',' Qual seu nome?' ,'sou uma ia'])

exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {bot.get_response(query)}")