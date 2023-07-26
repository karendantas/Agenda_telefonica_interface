from tkinter import *
from tkinter import messagebox

def abrirtela ():
    jcadastro = Tk()
    def adicionar_contato ():
        if len(contatos)<3:
            with open('Agenda telefonica.txt','a') as arquivopy:
                arquivopy.write(lnome.get() + "\n" + ltel.get() + "\n")
        else:
            messagebox.showwarning(title=None, message="A agenda está no limite de 100 contatos!")
        pegar_linhas()

    jcadastro.title("Criar contato")
    jcadastro.geometry("500x250")
    jcadastro.configure(background="#FDF5E6")

    Label(jcadastro, text="Nome:", background="#FDF5E6", anchor="w").place(x=10, y=10, width=100, height=20)
    lnome=Entry(jcadastro)
    lnome.place(x=10, y=30, width=300, height=30)

    Label(jcadastro, text="Telefone:", background="#FDF5E6", anchor="w").place(x=10, y=60, width=100, height=20)
    ltel=Entry(jcadastro)
    ltel.place(x=10, y=80, width=300, height=30)

    Button(jcadastro, text = "confirmar", background="#FFCBDB", command=adicionar_contato).place(x=10, y=150, width=200, height=30)
    Button(jcadastro, text = "Voltar",background="#FFCBDB", command= jcadastro.destroy).place(x=250, y=150, width=200, height=30)

    

              
           
#função que le as linhas de um arquivo
def ler_agenda():
    with open ("Agenda telefonica.txt", 'r') as arquivopy:
        linhas=arquivopy.readlines() #variavel linhas recebe funcao que le as linhas do arquivo
        for lines in linhas:
         print(lines)



#função que pega as linhas do arquivo o transforma em um dicionario
def pegar_linhas():
    listanome=[]
    listtel=[]
    with open ("Agenda telefonica.txt", "r") as arquipy:
        linhas = arquipy.readlines()
        
        #aqui estou pegando cada linha do arquivo, e se a linha é par, o elemento que esta nela
        #cai na lista dos nome, se for impar cai na lista dos numeros.
        for i in range (len(linhas)):
            if(i%2==0):
                listanome.append(linhas[i].strip())
                #a funcao strip retira espaços em branco e enter "\n"
                #append é a maneira de adiconar itens dentro de listas no python
            elif(i%2!=0):
                listtel.append(linhas[i].strip())
               
        #agora junto as duas listas em um dicionario
    unirlistas = zip(listanome, listtel)
    global contatos #transformando em uma variavel global para poder usar em outras funções
    contatos= dict(unirlistas) 
       
    print(contatos)#esse print é so pra eu ver se deu certo dps apago(lembrete para karen do futuro)


def tela_procuranome():
    pnome= Tk()
    #função que procura pelo nome
    def procurar_nome():
        
        if pronome.get() in contatos.keys():
            nomedigitado=Label(pnome, text="O contato de: '{}', está na agenda! ".format(pronome.get()), anchor="w")
            nomedigitado.place(x=10, y=100, width=300, height=20)
        else:
            print ("Contato não encontrado")

    pnome.title("Criar contato")
    pnome.geometry("500x300")

    Label(pnome, text="Nome", anchor="w").place(x=10, y=10, width=100, height=20)
    pronome=Entry(pnome)
    pronome.place(x=10, y=30, width=200, height=20)
    Button(pnome, text = "Procurar",background="#FDF5E6", command=procurar_nome).place(x=100, y=250, width=200, height=20)
        
  


#função que procura pelo numero
def procurar_numero():
    procuranumero = str(input("Digite seu número:"))
    if procuranumero in contatos.values():
        print ("O número '{}', foi encontrado na agenda!" .format(procuranumero))
    else:
        print("Número não foi encontrado.")


#funcao para alterar um contato()
def alterar_contato():
    procurar_cont = str(input("Digite seu nome: "))
    if procurar_cont in contatos:
        del contatos[procurar_cont]
        #del é uma keyword que deleta o elemento nas chaves

        novo_nome=str(input("Digite o novo nome: "))
        novo_tel = input("Digite o novo número")
        contatos[novo_nome]=novo_tel

        with open ("Agenda telefonica.txt", 'a') as arquivopy:
            arquivopy.truncate(0) #apago a agenda para inserir o novo dicionario com o contato alterado
            for nome, telefone in contatos.items():
                arquivopy.write(str(nome)+"\n"+str(telefone)+"\n")

        print("O contato foi alterado!")
    else:
        print("Desculpe, contato não encontrado!")



def deletar_contato ():
    deljanela = Tk()
    deljanela.geometry("400x200")
    deljanela.configure(background="#FDF5E6")
    #funcao para deletar um contato(essa não difere tanto da de alterar, os passos seguem praticamente os mesmos)
    def excluir_contato():
        
        if resposta.get() in contatos:
            del contatos[resposta.get()]
    
            with open ("Agenda telefonica.txt", 'a') as arquivopy:
                arquivopy.truncate(0)
                for nome, telefone in contatos.items():
                    arquivopy.write(str(nome)+"\n"+str(telefone)+"\n")

            print("O contato foi apagado da agenda!")
        else:
            print("Desculpe, contato não encontrado!")

    pergunta = Label(deljanela, text="Qual contato deseja apagar?", background="#FDF5E6", anchor="w")
    pergunta.place(x=10, y = 20, width=200, height=30)
    resposta = Entry(deljanela)
    resposta.place(x=10, y= 40, width=200, height = 30)
    Button(deljanela, text="Confirmar", background="#FFCBDB", command= excluir_contato).place(x=160, y=150, width=200, height=30)


#janela de opção de apagar a agenda
def janela_apagar():
    res= messagebox.askyesno(title="Alerta", message="Deseja certeza que deseja apagar a agenda")
    
    if (res==True):
        with open ("Agenda telefonica.txt", "r+") as arquivopy:
            arquivopy.truncate(0) #a função truncate "redimensiona" o arquivo, no caso para tamanho 0, que 
            #apaga os elementos existentes
            messagebox.showinfo(title=None, message = "Agenda apagada!")
      


#janela com menu e criação da agenda.txt    
def janela_agenda():
    agendajanela=Tk()
    #funcao que mostra o tamanho da agenda (pelo tamanho do dicionario)   
    def tamanho_agenda ():
        quantidade = len(contatos)
        quant= Label(agendajanela, text="O número de contatos que a agenda possui no momento é de {}:" .format(quantidade))
        quant.place(x=100, y=400, width=400, height=30)
      
    agendajanela.title("minha janelinha")
    agendajanela.geometry("500x500")
    agendajanela.configure(background="#FDF5E6")

    agenda = Listbox(agendajanela, borderwidth=1, relief="solid")
   
    with open ("Agenda telefonica.txt", 'r') as arquivopy:
        linhas=arquivopy.readlines() #variavel linhas recebe funcao que le as linhas do arquivo
        for line in linhas:
            agenda.insert(END, line)
    agenda.place(x=100, y=0, width=300, height=300)
    Button(agendajanela, text="Tamanho",background="#FFCBDB", command= tamanho_agenda).place(x=160, y=350, width=200, height=30)


#janela principal
janela = Tk()
with open('Agenda telefonica.txt','r') as arquivopy:
    pegar_linhas()
    janela.title("minha janelinha")
    janela.geometry("400x500")
    janela.configure(background="#FDF5E6")

    menu = Label(janela, text="Agenda Telefonica", background="#FDF5E6")
    menu.place(x=130, y=10, width=150, height= 40)
    texto = Label(janela, text="Selecione sua opção!", background="#FDF5E6")
    texto.place(x=130, y=50, width=150, height= 40)
    Button(janela, text="Novo contato", background="#FFCBDB", command=abrirtela).place(x=110, y=100, width=200, height=30)
    Button(janela, text="Ver agenda",background="#FFCBDB", command=janela_agenda).place(x=110, y=140, width=200, height=30)
    Button(janela, text="Procurar contato pelo nome",background="#FFCBDB", command=tela_procuranome).place(x=110, y=180, width=200, height=30)
    Button(janela, text="Procurar contato pelo número",background="#FFCBDB", command=tela_procuranome).place(x=110, y=220, width=200, height=30)
    Button(janela, text="Alterar contato",background="#FFCBDB", command=tela_procuranome).place(x=110, y=260, width=200, height=30)
    Button(janela, text="Deletar contato",background="#FFCBDB", command=deletar_contato).place(x=110, y=300, width=200, height=30)
    Button(janela, text="Apagar agenda",background="#FFCBDB", command=janela_apagar).place(x=110, y=340, width=200, height=30)
    Button(janela, text="Sair",background="#FFCBDB", command=janela.destroy).place(x=110, y=380, width=200, height=30)
    
janela.mainloop()




