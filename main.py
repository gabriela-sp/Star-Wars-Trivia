import os
from time import sleep

perguntas = {
  'Questão 1) Em que ano foi lançado o primeiro filme de\nStar Wars no cinema?' : '1977',
  'Questão 2) Qual o nome do mestre Jedi que é verde e\npequeno?' : 'Yoda',
  'Questão 3) Qual o primeiro nome do protagonista da\ntrilogia original de Star Wars?' : 'Luke',
  'Questão 4) O nome do vilão que se veste de preto e tem\numa voz metálica é Darth...' : 'Vader',
  'Questão 5) Escreva a letra da opção que NÃO é o nome de\num título de filme da saga Star Wars:\n A) Uma nova Esperança \n B) O Retorno do Jedi \n C) Os Jedis Contra Atacam' : 'C'
}

jogar = str(
  input(
    "********************************************************\n\n       ✨🪐💫BEM VIND@ AO STAR WARS TRIVIA!💫🪐✨\n\n        Será que você é um Nerd Raiz ou Nutella?\n\n********************************************************\n\n                    🚨SOBRE O JOGO🚨\n\nO jogo possui 5 perguntas, responda-as corretamente e,\nse a sua pontuação for maior do que 3 pontos, você é um\nverdadeiro Nerd Raiz!\n\n********************************************************\n\n              Aperte ENTER para começar!🚀\n"
  ))
os.system("clear")

print(
  "\n             ✨QUE A FORÇA ESTEJA COM VOCÊ!✨\n\n********************************************************\n"
)

pontuacao = 0

def verifica_resposta(pergunta, resposta):
  if resposta == perguntas[pergunta]:
    return True
  else:
    return False

for pergunta in perguntas.keys():
  print(pergunta)
  resposta = str(input("Sua Resposta: ").title())
  if verifica_resposta(pergunta, resposta):
    pontuacao += 1
    print("\nResposta certa! 😁\nSua pontuação atual é: " + str(pontuacao) + "\n\n********************************************************\n")
  else:
    print("\nVocê errou! 😓\nA resposta correta era: " + perguntas[pergunta] + "\nSua pontuação atual é: " + str(pontuacao) + "\n\n********************************************************\n")

if pontuacao >= 3:
  sleep(3)
  os.system("clear")
  print("********************************************************\n\nPARABÉNS! VOCÊ É UM(A) VERDADEIR@ NERD RAIZ! 🤓\nSua pontuação final foi: " + str(pontuacao))
else:
  sleep(3)
  os.system("clear")
  print(f"********************************************************\n\nNÃO FOI DESSA VEZ! VOCÊ É UM(A) NERD NUTELLA.\nSua pontuação final foi: {pontuacao}\nFaltou/faltaram {3-pontuacao} ponto(s) para ganhar o jogo.")

print("\n********************************************************\n\n                 🌠OBRIGADA POR JOGAR🌠")
