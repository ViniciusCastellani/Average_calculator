import tkinter as tk 

#-------------------
#Criação das funções

def mostrar_mensagem():
    mensagem_label.config(text = "Voce clicou o botao") #retorna a mensagem quando o botão for clicado, substitui o texto da mensagem_label

#------------------------
#cria a janela principal

janela = tk.Tk() #cria a janela, abre a janela e fecha muito rapido se não usar mainloop
janela.title("Titulo") #coloca o titulo da janela, define o titulo da janela

#------------------------
#criação de informação, mensagem para o usuário

mensagem_label = tk.Label(janela, text = "Aperte o botao") #label = mensagem para o usuário, texto para ser exibido
mensagem_label.pack(padx = 20, pady = 20) #mostra na tela a mensagem 

#----------------------
#criação de widgets

botao = tk.Button(janela, text = "Clique-me", command= mostrar_mensagem) #cria o botao, quando clicar vai executar a função
#se usar () no command depois do nome da função o comando é automaticamente executado mesmo não apertando o botão
botao.pack()


janela.mainloop()



