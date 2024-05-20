import requests
from tkinter import *
from tkinter import messagebox
import random

root = Tk()

class MainWindow():
    def __init__(self):
        self.root = root
        self.frame()
        root.mainloop()

    def frame(self):
        self.root.title("Ficha Cadastral")
        self.root.configure(background='#CCFFCC')
        self.root.geometry("500x400")
        self.root.resizable(True, False)

        # label informações básicas
        self.lbl_nome = Label(self.root, text='Nome: ', font=('verdana',10),bg='#CCFFCC',anchor='e')
        self.lbl_nome.place(relx=.05,rely=.05,relwidth=.20)
        self.lbl_sobrenome = Label(self.root, text='Sobrenome: ', font=('verdana',10),bg='#CCFFCC',anchor='e')
        self.lbl_sobrenome.place(relx=.05,rely=.1,relwidth=.20)
        self.lbl_cpf = Label(self.root, text='CPF: ', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_cpf.place(relx=.05,rely=.15,relwidth=.20)
        self.lbl_rg = Label(self.root, text='RG: ', font=('verdana',10),bg='#CCFFCC')
        self.lbl_rg.place(relx=.46,rely=.15)
        self.lbl_data_nascimento = Label(self.root, text='Data de nasc.: ', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_data_nascimento.place(relx=.01,rely=.20,relwidth=.24)
        self.lbl_telefone = Label(self.root, text='Tel.:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_telefone.place(relx=.45,rely=.20)
        self.lbl_sexo = Label(self.root, text='Sexo: ', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_sexo.place(relx=.05,rely=.25,relwidth=.20)
        self.lbl_naturalidade = Label(self.root, text='Naturalidade: ', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_naturalidade.place(relx=.05,rely=.30,relwidth=.20)
        self.lbl_estado_civil = Label(self.root, text='Estado civil: ', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_estado_civil.place(relx=.05,rely=.35,relwidth=.20)
        self.lbl_cnh = Label(self.root, text='CNH:', font=('verdana',10))
        self.lbl_cnh.place(relx=.45,rely=.35)
        self.nivel_escolaridade = Label(self.root, text='Nivel escolaridade:', font=('verdana',10))
        self.nivel_escolaridade.place(relx=.05,rely=.40)

        # entry informações básicas
        self.entry_nome = Entry(self.root, font=('verdana',10))
        self.entry_nome.place(relx=.25,rely=.05, relwidth=.5)
        self.entry_sobrenome = Entry(self.root, font=('verdana',10))
        self.entry_sobrenome.place(relx=.25,rely=.1, relwidth=.5)
        self.entry_cpf = Entry(self.root, font=('verdana',10))
        self.entry_cpf.place(relx=.25,rely=.15, relwidth=.20)
        self.entry_rg = Entry(self.root, font=('verdana',10))
        self.entry_rg.place(relx=.55,rely=.15, relwidth=.20)
        self.entry_data_nasc = Entry(self.root, font=('verdana',10,'italic'))
        self.entry_data_nasc.place(relx=.25,rely=.20, relwidth=.20)
        self.entry_data_nasc.insert(0, "ddmmaaaa")

        self.entry_ddd = Entry(self.root, font=('verdana',10,'italic'))
        self.entry_ddd.place(relx=.55,rely=.20, relwidth=.07)
        self.entry_ddd.insert(0, "ddd")
        self.entry_ddd = Entry(self.root, font=('verdana',10))
        self.entry_ddd.place(relx=.61,rely=.20, relwidth=.20)

        # Radio Button
        global sexo
        sexo = IntVar(value=1)
        self.radio_masc = Radiobutton(self.root,text='Masc.', value=1, variable=sexo,bg='#CCFFCC')
        self.radio_masc.place(relx=.25,rely=.25,relwidth=.10)
        self.radio_fem = Radiobutton(self.root,text='Fem.', value=2, variable=sexo,bg='#CCFFCC')
        self.radio_fem.place(relx=.35,rely=.25,relwidth=.10)

        # label trabalho
        self.lbl_trabalho = Label(self.root, text='Trabalha?', font=('verdana',10))
        self.lbl_trabalho.place(relx=.05,rely=.47)
        self.lbl_empresa = Label(self.root, text='Empresa:', font=('verdana',10))
        self.lbl_empresa.place(relx=.40,rely=.47)
        self.lbl_funcao = Label(self.root, text='Função:', font=('verdana',10))
        self.lbl_funcao.place(relx=.40,rely=.52)
        self.faixa_salarial = Label(self.root, text='Faixa salarial:', font=('verdana',10))
        self.faixa_salarial.place(relx=.40,rely=.57)
        # botões trabalho
        self.btn_trabalha_sim = Button(self.root, text='Sim', font=('verdana',10),state='disabled')
        self.btn_trabalha_sim.place(relx=.20,rely=.48)
        self.btn_trabalha_nao = Button(self.root, text='Não', font=('verdana',10))
        self.btn_trabalha_nao.place(relx=.30,rely=.48)

        # label endereço
        self.lbl_endereco = Label(self.root, text='Endereço:', font=('verdana',10))
        self.lbl_endereco.place(relx=.05,rely=.64)
        self.lbl_rua = Label(self.root, text='Rua:', font=('verdana',10))
        self.lbl_rua.place(relx=.05,rely=.71)
        self.lbl_numero = Label(self.root, text='Numero:', font=('verdana',10))
        self.lbl_numero.place(relx=.60,rely=.71)
        self.lbl_cep = Label(self.root, text='CEP:', font=('verdana',10))
        self.lbl_cep.place(relx=.05,rely=.76)
        self.lbl_cidade = Label(self.root, text='Cidade:', font=('verdana',10))
        self.lbl_cidade.place(relx=.45,rely=.76)
        self.lbl_bairro = Label(self.root, text='Bairro:', font=('verdana',10))
        self.lbl_bairro.place(relx=.05,rely=.81)
        self.lbl_uf = Label(self.root, text='UF:', font=('verdana',10))
        self.lbl_uf.place(relx=.45,rely=.81)

        # entradas endereço
        self.entrada_cep = Entry(self.root, font=('verdana',10,'italic'))
        self.entrada_cep.insert(0, "CEP")
        self.entrada_cep.place(relx=.20,rely=.64,relwidth=.15)

        # Botões endereço
        self.btn_buscar_cep = Button(self.root, text='Buscar CEP', font=('verdana',10))
        self.btn_buscar_cep.place(relx=.36,rely=.63)
        self.btn_buscar_logradouro = Button(self.root, text='Buscar Endereço', font=('verdana',10), state='disabled')
        self.btn_buscar_logradouro.place(relx=.54,rely=.63)
        self.btn_end_manual = Button(self.root, text='Inserir dados', font=('verdana',10))
        self.btn_end_manual.place(relx=.79,rely=.63)

        # botões Main
        self.btn_salvar = Button(self.root, text='SALVAR', font=('verdana',10))
        self.btn_salvar.place(relx=.2, rely=.87)
        self.btn_limpar = Button(self.root, text='LIMPAR', font=('verdana',10))
        self.btn_limpar.place(relx=.35, rely=.87)
        self.btn_ver_lista = Button(self.root, text='LIMPAR', font=('verdana',10))
        self.btn_ver_lista.place(relx=.55, rely=.87)
MainWindow()