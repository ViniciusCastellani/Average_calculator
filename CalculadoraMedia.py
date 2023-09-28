import tkinter as tk
from tkinter import simpledialog 

"""
----------------------------------------------
simpledialog = Serve para abrir, criar uma janela secundaria, simplifica o processo de troca de informação 
               do usuário, input e output

tk.Tk() = cria a janela principal

.title = coloca o titulo da janela

tk.button(aonde o botao vai estar, text = "coloca texto dento do botao") = cria um botao

pack(padx = posicao x, pady = posicao y) = chamar o pacote de funções da biblioteca do tkinter, interface, 
                                           caracteristicas, funções do tkinter

simpledialog.askfloat("Titulo", "mensagem para o usuario") = abre uma janela secundária para o usuario
                                                             inserir um numero float

None = Vazio

{variavel:.2f} = formata em 2 casas decimais, deixa apenas 2 numeros após a virgula

.config = configura uma variável, por exemplo um label para reescrever algum texto, por exemplo,
          nessa variavel

mainloop() = deixa a janela aberta até o usuário fechar
----------------------------------------------
"""

#----------------------------------------------
#CRIACAO DE UMA ROTINA, FUNÇÃO

def calcular_media():
    numero1 = simpledialog.askfloat("Solicitar o numero", "Digite o primeiro numero:")
    numero2 = simpledialog.askfloat("Solicitar o numero", "Digite o segundo numero:")
    
    if numero1 is not None and numero2 is not None:
        media = (numero1 + numero2) / 2
        resultado_label.config(text = f"A media dos numeros é: {media:.2f}")
    else:
        resultado_label.config(text= "Erro ao solicitar os valores!")
#----------------------------------------------
#CRIA A JANELA

janela = tk.Tk() 
janela.title("Calculadora de media")
#----------------------------------------------
#CRIA O ROTULO PARA SOLICITAR OS VALORES

resultado_label = tk.Label(janela, text= "")
resultado_label.pack(pady =20)
#----------------------------------------------
#CRIAÇAO DE UM BOTAO

botao = tk.Button(janela, text = "calcular a media", command = calcular_media)
botao.pack()
#----------------------------------------------

janela.mainloop()

