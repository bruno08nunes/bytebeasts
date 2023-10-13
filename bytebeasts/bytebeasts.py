import tkinter as tk
from tkinter import *
import random

vidaP1 = 6
vidaP2 = 6

def mudarTexto(tex):
  texto.config(text=tex)

def addEntry(entry):
  entry.grid(row = 1, column = 0, pady = (50, 0), padx = 5)
  btn = Button(janela, text="Enviar")
  btn.grid(row = 1, column = 1, pady = (50, 0), padx = 5)
  return btn

def addBtn2(btn1, btn2):
  btn1.grid(row = 1, column = 0, pady = (50, 0), padx = 5)
  btn2.grid(row = 1, column = 1, pady = (50, 0), padx = 5)

def addBtn3(btn1, btn2, btn3):
  btn1.grid(row = 1, column = 0, pady = (50, 0), padx = 5)
  btn2.grid(row = 1, column = 1, pady = (50, 0), padx = 5)
  btn3.grid(row = 2, column = 0, pady = 10, padx = 5, columnspan = 2)

def destroyButtons(botao1, botao2, botao3):
  botao1.destroy()
  if botao2 != False:
    botao2.destroy()
  if botao3 != False:
    botao3.destroy()

def reset(vit): #Serve para o modo campanha
  #Vida do jogador, vida do adversário, chance de ataque e derrota
  return 5, 5+vit, 6, 0

def responder(nome):
  botao1 = Button(janela, command = lambda: campanha(nome, 0, botao1, botao2, False), text="Continuar")
  botao2 = Button(janela, command=lambda: janela.quit(), text="Desistir")
  addBtn2(botao1, botao2)

def nomear():
  en_nome = Entry(janela)
  botao1.destroy()
  botao2.destroy()
  texto.config(text = "Qual é o seu nome?")
  btnEnviar = addEntry(en_nome)
  btnEnviar.config(command= lambda: preparado(en_nome, btnEnviar))

def preparado(en_nome, btnEnviar):
  nome = en_nome.get()
  texto.config(text = f"Bem vindo, {nome}! Você está preparado para o torneio?")
  btnEnviar.destroy()
  en_nome.destroy()
  responder(nome)

def campanha(nome, vit, botao1, botao2, botao3):
  destroyButtons(botao1, botao2, botao3)
  vitoria = vit
  vidaPokemon, vidaInimigo, chanceAtaque, derrota = reset(vitoria)
  combate(vidaPokemon, vidaInimigo, chanceAtaque, derrota, vitoria, True, nome, botao1, botao2, botao3, True)

def combate(vidaPokemon, vidaInimigo, chanceAtaque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3, primeiraRodada):
  nomeInimigo = ["Ziriguidum", "Clarrato", "Batemonpelé", "Marvalo", "Boitatão"]
  if primeiraRodada:
    texto.config(text=f"Você está de frente com o {nomeInimigo[vitoria]}, um perigoso oponente.")
  if seuTurno:
    if vidaPokemon <= 0:
      destroyButtons(botao1, botao2, botao3)
      derrota = 1
      responder(nome)
    else:
      destroyButtons(botao1, botao2, botao3)
      if not primeiraRodada:
        texto.config(text = "Sua rodada")
      acao(vidaPokemon, vidaInimigo, chanceAtaque, derrota, vitoria, False, nome, botao1, botao2, botao3)
  else:
    if vidaInimigo <= 0:
      texto.config(text = f"Você ganhou, {nome}! Vamos para o próximo combate")
      vitoria += 1
      vidaPokemon, vidaInimigo, chanceAtaque, derrota = reset(vitoria)
      if vitoria < 5:
        campanha(nome, vitoria, botao1, botao2, botao3)
      else:
        destroyButtons(botao1, botao2, botao3)
        venceuCampanha(nome)
    else:
      acaoOponente(vidaPokemon, vidaInimigo, chanceAtaque, derrota, vitoria, True, nome, botao1, botao2, botao3)

def acao(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3):
  botao1 = Button(janela, command=lambda: atacar(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3), text="Atacar")
  botao2 = Button(janela, command=lambda: descansar(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3), text="Descansar")
  botao3 = Button(janela, command=lambda: defender(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3), text="Defender")
  addBtn3(botao1, botao2, botao3)

def atacar(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3):
    if random.randint(1, 10) == 10: #Valor de crítico, que tem 1/10 de chance de causar o dobro de dano
        HPInimigo -= 2
        if HPInimigo < 0:
            texto.config(text="Você acertou. O Inimigo está com 0 de vida")
        else:
            texto.config(text=f"Você deu um ataque crítico. O inimigo está com {HPInimigo} de vida")
    else:
        HPInimigo -=1
        texto.config(text=f"Muito bem, você acertou. O inimigo está com {HPInimigo} de vida")
    destroyButtons(botao1, botao2, botao3)
    botao1 = Button(janela, command = lambda: combate(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3, False), text = "Continuar")
    botao2 = Button(janela, command = lambda: janela.quit(), text = "Sair")
    addBtn2(botao1, botao2)

def descansar(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3):
    HPPlayer +=1
    texto.config(text = f"Você se curou, estando com {HPPlayer} de vida")
    destroyButtons(botao1, botao2, botao3)
    botao1 = Button(janela, command = lambda: combate(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3, False), text = "Continuar")
    botao2 = Button(janela, command = lambda: janela.quit(), text = "Sair")
    addBtn2(botao1, botao2)

def defender(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3):
    ataque -= 0.5
    texto.config(text = "Você diminui a chance de o ataque do adversário acertar")
    destroyButtons(botao1, botao2, botao3)
    botao1 = Button(janela, command = lambda: combate(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3, False), text = "Continuar")
    botao2 = Button(janela, command = lambda: janela.quit(), text = "Sair")
    addBtn2(botao1, botao2)

def acaoOponente(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3):
    if random.randint(1, 10) <= ataque:  #Valor de acerto, que tem chanceDeAcerto/10 de acertar
        if random.randint(1, 10) == 10: #Valor de crítico, que tem 1/10 de chance de causar o dobro de dano
            HPPlayer -= 2
            if HPPlayer > 0:
                if HPPlayer < 0:
                    texto.config(text = "Vez do adversário.\nEle acertou um ataque crítico, dando 2 de dano. Você está com 0 de vida")
                else:
                    texto.config(text = f"Vez do adversário.\nEle acertou um ataque crítico, dando 2 de dano. Você está com {HPPlayer} de vida")
            else:
                texto.config(text = "Vez do adversário.\nEle acertou o ataque, te deixando com 0 de vida. \nVocê perdeu. \nDeseja Continuar?")
        else:
            HPPlayer -= 1
            if HPPlayer > 0:
                texto.config(text = f"Vez do adversário.\nAtaque acertado, você tomou 1 de dano, estando com {HPPlayer} de vida")
            else:
                texto.config(text = "Vez do adversário.\nEle acertou o ataque, te deixando com 0 de vida. \nVocê perdeu. \nDeseja Continuar?")
    else:
        texto.config(text = "Vez do adversário.\nInimigo erra o ataque")
    botao1.config(command = lambda: combate(HPPlayer, HPInimigo, ataque, derrota, vitoria, seuTurno, nome, botao1, botao2, botao3, False))


def venceuCampanha(nome):
  texto.config(text="Parabéns, você venceu! Deseja recomeçar o jogo?")
  responder(nome)

def acaoPVP(atacante, atacado, HPAtacante, HPAtacado):
  act = input(f"Vez de {atacante}. Você vai atacar ou descansar? ").lower()
  if act == "atacar":
    if random.randint(1, 10) <= 7: #Valor de acerto, que tem 7/10 de chance de acertar
      if random.randint(1, 10) == 10: #Valor de crítico, que tem 1/10 de chance de causar o dobro de dano
        HPAtacado -= 2
        if HPAtacado < 0:
          print(f"Você acertou um crítico! {atacado} está com 0 de vida")
        else:
          print(f"Você acertou um crítico! {atacado} está com {HPAtacado} de vida")
      else:
        HPAtacado -= 1
        print(f"Você acertou. {atacado} está com {HPAtacado} de vida")
    else:
      print("Você errou o ataque")
  elif act == "descansar":
    HPAtacante += 1
    print(f"Você se curou, estando com {HPAtacante} de vida")
  else:
    print("Você perdeu a vez")
  return HPAtacante, HPAtacado

def nomearP1():
  en_nome = Entry(janela)
  botao1.destroy()
  botao2.destroy()
  texto.config(text = "Escreva o nome do Player 1")
  btnEnviar = addEntry(en_nome)
  btnEnviar.config(command= lambda: nomearP2(en_nome, btnEnviar))

def nomearP2(en_nome, btnEnviar):
  nomeP1 = en_nome.get()
  texto.config(text = "Escreva o nome do Player 2")
  en_nome.delete(0, END)
  btnEnviar.config(command = lambda: iniciarPVP(nomeP1, en_nome, btnEnviar))

def iniciarPVP(nomeP1, en_nome, btnEnviar):
  nomeP2 = en_nome.get()
  texto.config(text = f"Bem vindos, {nomeP1} e {nomeP2}. \nVocês dois batalharão um contra o outro. \nVocês poderão atacar ou se curar.")
  en_nome.destroy()
  btnEnviar.destroy()
  botao1 = Button(janela, command = lambda: PVP(nomeP1, nomeP2, botao1, botao2, True, True), text="Continuar")
  botao2 = Button(janela, command=lambda: janela.quit(), text="Sair do Jogo")
  addBtn2(botao1, botao2)

def PVP(nomeP1, nomeP2, botao1, botao2, primeiraRodada, turnoP1):
  global vidaP1
  global vidaP2
  botao1.config(text="Atacar")
  botao2.config(text="Descançar")
  if primeiraRodada:
    vidaP1 = 6
    vidaP2 = 6
  if vidaP1 <= 0:
    venceu(nomeP1, nomeP2, botao1, botao2, nomeP2)
  elif vidaP2 <= 0:
    venceu(nomeP1, nomeP2, botao1, botao2, nomeP1)
  else:
    if turnoP1:
      texto.config(text = f"Vez de {nomeP1}")
      botao1.config(command=lambda: atacarPVP(nomeP1, nomeP2, vidaP1, vidaP2, turnoP1, botao1, botao2))
      botao2.config(command=lambda: descansarPVP(nomeP1, nomeP2, vidaP1, vidaP2, turnoP1, botao1, botao2))
    else:
      texto.config(text = f"Vez de {nomeP2}")
      botao1.config(command=lambda: atacarPVP(nomeP2, nomeP1, vidaP2, vidaP1, turnoP1, botao1, botao2))
      botao2.config(command=lambda: descansarPVP(nomeP2, nomeP1, vidaP2, vidaP1, turnoP1, botao1, botao2))

def atacarPVP(atacante, atacado, HPAtacante, HPAtacado, turnoP1, botao1, botao2):
  global vidaP1
  global vidaP2
  if random.randint(1, 10) <= 7:
    if random.randint(1, 10) == 10:
      HPAtacado -= 2
      if HPAtacado < 0:
        texto.config(text = f"Acerto crítico! {atacado} está com 0 de vida")
      else:
        texto.config(text = f"Acerto crítico! {atacado} está com {HPAtacado} de vida")
    else:
      HPAtacado -= 1
      texto.config(text = f"Você acertou! {atacado} está com {HPAtacado} de vida")
  else:
    texto.config(text = "Você errou o ataque")
  if turnoP1:
    vidaP1 = HPAtacante
    vidaP2 = HPAtacado
    botao1.config(command=lambda: PVP(atacante, atacado, botao1, botao2, False, False), text = "Continuar")
    botao2.config(command=lambda: janela.quit(), text = "Desistir")
  else:
    vidaP1 = HPAtacado
    vidaP2 = HPAtacante
    botao1.config(command=lambda: PVP(atacado, atacante, botao1, botao2, False, True), text = "Continuar")
    botao2.config(command=lambda: janela.quit(), text = "Desistir")

def descansarPVP(atacante, atacado, HPAtacante, HPAtacado, turnoP1, botao1, botao2):
  global vidaP1
  global vidaP2
  HPAtacante += 1
  texto.config(text = f"{atacante} se curou, estando com {HPAtacante} de vida")
  if turnoP1:
    vidaP1 = HPAtacante
    vidaP2 = HPAtacado
    botao1.config(command=lambda: PVP(atacante, atacado, botao1, botao2, False, False), text = "Continuar")
    botao2.config(command=lambda: janela.quit(), text = "Desistir")
  else:
    vidaP1 = HPAtacado
    vidaP2 = HPAtacante
    botao1.config(command=lambda: PVP(atacado, atacante, botao1, botao2, False, True), text = "Continuar")
    botao2.config(command=lambda: janela.quit(), text = "Desistir")

def venceu(nomeP1, nomeP2, botao1, botao2, vencedor):
  texto.config(text = f"{vencedor} venceu!\nDesejam continuar jogando?")
  botao1.config(text = "Continuar", command = lambda: PVP(nomeP1, nomeP2, botao1, botao2, True, True))
  botao2.config(text = "Sair do Jogo", command = lambda: janela.quit())

janela = tk.Tk()
janela.title("ByteBeasts")
janela.geometry("300x400")
janela.resizable(width=False, height=False)
janela.config(padx=30, pady=30)
texto = tk.Label(janela, text="ByteBeasts", font=("Verdana", "15"), justify = CENTER, wraplength = 250)
botao1 = Button(janela, command=nomear, text="Modo Campanha")
botao2 = Button(janela, command=nomearP1, text="Modo PVP")
creditos = tk.Label(janela, text="© Bruno Nunes", font=("Verdana", "15", "italic"))

texto.grid(row = 0, column = 0, pady = 2, columnspan = 2)
addBtn2(botao1, botao2)
creditos.grid(row = 3, column = 0, pady = (50, 5), columnspan = 2)
janela.mainloop()