import requests
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

root = Tk()

class Funcs():
    def clicar_nao_trabalho(self):
        self.entry_empresa.configure(state='disabled')
        self.entry_funcao.configure(state='disabled')
        self.entry_salarial.configure(state='disabled')
        self.btn_trabalha_sim.configure(state='normal')
        self.btn_trabalha_nao.configure(state='disabled')
    def clicar_trabalha(self):
        self.entry_empresa.configure(state='normal')
        self.entry_funcao.configure(state='normal')
        self.entry_salarial.configure(state='normal')
        self.btn_trabalha_sim.configure(state='disabled')
        self.btn_trabalha_nao.configure(state='normal')

    def validar_nome(self):
        try:
            nome = self.entry_nome.get()
            if len(nome)>30:
                messagebox.showerror("Error",'Campo "nome" superior a 30 caracteres. Favor verificar!')
            elif len(nome) == 0:
                messagebox.showerror("Error", 'Campo "nome" está vazio. Favor verificar!')
            elif nome.isnumeric():
                messagebox.showerror("Error", 'Campo "nome" foi inserido somente números. Favor verificar!')
            else:
                return nome
        except:
            messagebox.showerror("Error",'Campo nome com dado inválido. Favor verificar!')
    def validar_sobrenome(self):
        try:
            sobrenome = self.entry_sobrenome.get()
            if len(sobrenome)>30:
                messagebox.showerror("Error",'Campo "sobrenome" superior a 30 caracteres. Favor verificar!')
            elif len(sobrenome) == 0:
                messagebox.showerror("Error", 'Campo "sobrenome" está vazio. Favor verificar!')
            elif sobrenome.isnumeric():
                messagebox.showerror("Error", 'Campo "sobrenome" foi inserido somente números. Favor verificar!')
            else:
                return sobrenome
        except:
            messagebox.showerror("Error",'Campo sobrenome com dado inválido. Favor verificar!')

    def validar_cpf(self):
        try:
            texto_cpf = self.entry_cpf.get()
            if len(texto_cpf) == 0:
                messagebox.showerror("Error", 'Campo "CPF" está vazio. Favor verificar!')
            else:
                texto_cpf = texto_cpf.replace('/', '')
                texto_cpf = texto_cpf.replace('.', '')
                texto_cpf = texto_cpf.replace('-', '')
                texto_cpf = texto_cpf.replace(',', '')
                if len(texto_cpf) < 11 or len(texto_cpf) > 11:
                    messagebox.showerror("Error", 'Campo "CPF" com dados inválidos. Favor verificar!')
                else:
                    int(texto_cpf)
                    return texto_cpf
        except:
            messagebox.showerror("Error", 'Campo "CPF" com dados inválidos. Favor verificar!')

    def limpar_texto_entry(self):
        try:
            texto_cep = self.entrada_cep.get()
            print(texto_cep)
            texto_cep = texto_cep.replace('-','')
            int(texto_cep)
            if len(texto_cep) == 8:
                print('texto CEP limpo: ', texto_cep)
                return texto_cep
            elif len(texto_cep) > 8:
                messagebox.showerror("Erro dado", "Tamanho do número CEP maior que o permitido!")
            else:
                messagebox.showerror("Erro dado", "Tamanho do número CEP menor que o permitido!")
        except:
            messagebox.showerror("Erro dado", "Você inseriu um valor incorreto!")

    def buscar_cep(self):
        cep_para_busca = self.limpar_texto_entry()
        try:
            link = f'https://viacep.com.br/ws/{cep_para_busca}/json'
            requisicao = requests.get(link)
            dict_cep = requisicao.json()
            print(dict_cep)
            for dado in dict_cep:
                print(dado, dict_cep[dado])
                if dado == 'logradouro':
                    self.entry_rua.insert(0, dict_cep[dado])
                if dado == 'bairro':
                    self.entry_bairro.insert(0, dict_cep[dado])
                if dado == 'cep':
                    self.entry_cep.insert(0, dict_cep[dado])
        except:
            ...

    def salvar(self):
        try:
            todos_os_dados = []
            if self.validar_nome() is not None:
                todos_os_dados.append(self.validar_nome())
            if self.validar_sobrenome() is not None:
                todos_os_dados.append(self.validar_sobrenome())
            if self.validar_cpf() is not None:
                todos_os_dados.append(self.validar_cpf())
            if len(todos_os_dados) == 3:
                print('salvar dados: ', todos_os_dados)
            else:
                messagebox.showerror("Error", 'Algum campo foi inserido dado inválido!')
        except:
            messagebox.showerror("Error", 'Erro ao Salvar.')

class MainWindow(Funcs):
    def __init__(self):
        self.root = root
        self.frame()
        root.mainloop()

    def frame(self):
        self.root.title("Ficha Cadastral")
        self.root.configure(background='#CCFFCC')
        self.root.geometry("500x500")
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
        self.lbl_cnh = Label(self.root, text='CNH:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_cnh.place(relx=.52,rely=.255)
        self.nivel_escolaridade = Label(self.root, text='Escolaridade:', font=('verdana',10),bg='#CCFFCC',anchor='e')
        self.nivel_escolaridade.place(relx=.05,rely=.40)

        #Combobox
        self.combo_civil = ttk.Combobox(self.root,values=['Solteiro','Casado', 'Divorciado', 'Viúvo'], font=('Verdana',10))
        self.combo_civil.place(relx=.25,rely=.35,relwidth=.2)
        self.combo_escolaridade = ttk.Combobox(self.root,values=['Fundamental incompleto','Fundamental completo', 'Superior incompleto', 'Superior completo'], font=('Verdana',10))
        self.combo_escolaridade.place(relx=.25,rely=.40,relwidth=.45)


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

        #Checkbox CNH
        self.checkbox_cnh_a = Checkbutton(self.root, text='A', font=('verdana',10),bg='#CCFFCC')
        self.checkbox_cnh_a.place(relx=.60,rely=.25)
        self.checkbox_cnh_b = Checkbutton(self.root, text='B', font=('verdana',10),bg='#CCFFCC')
        self.checkbox_cnh_b.place(relx=.7,rely=.25)

        # label trabalho
        self.lbl_trabalho = Label(self.root, text=' Trabalha?', font=('verdana',10,'bold'),borderwidth=1,anchor='nw', relief="solid",bg='#CCFFCC')
        self.lbl_trabalho.place(relx=.05,rely=.45,relheight=.17, relwidth=.9)
        self.lbl_empresa = Label(self.root, text='Empresa:', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_empresa.place(relx=.40,rely=.46,relwidth=.2)
        self.lbl_funcao = Label(self.root, text='Função:', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.lbl_funcao.place(relx=.40,rely=.51,relwidth=.2)
        self.faixa_salarial = Label(self.root, text='Salárial atual:', font=('verdana',10),anchor='e',bg='#CCFFCC')
        self.faixa_salarial.place(relx=.40,rely=.56,relwidth=.2)
        # botões trabalho
        self.btn_trabalha_sim = Button(self.root, text='Sim', font=('verdana',10),state='disabled',command=self.clicar_trabalha)
        self.btn_trabalha_sim.place(relx=.22,rely=.46)
        self.btn_trabalha_nao = Button(self.root, text='Não', font=('verdana',10),command=self.clicar_nao_trabalho)
        self.btn_trabalha_nao.place(relx=.30,rely=.46)
        #Entry trabalho
        self.entry_empresa = Entry(self.root, font=('verdana',10))
        self.entry_empresa.place(relx=.60,rely=.46)
        self.entry_funcao = Entry(self.root, font=('verdana',10))
        self.entry_funcao.place(relx=.60,rely=.51)
        self.entry_salarial = Entry(self.root, font=('verdana',10))
        self.entry_salarial.place(relx=.60,rely=.56)

        # label endereço
        self.lbl_endereco = Label(self.root, text='Endereço:', font=('verdana',10,'bold'),bg='#CCFFCC')
        self.lbl_endereco.place(relx=.15,rely=.64)
        self.lbl_rua = Label(self.root, text=' Rua:', font=('verdana',10),anchor='nw', relief='solid',borderwidth=1,bg='#CCFFCC')
        self.lbl_rua.place(relx=.05,rely=.71,relheight=.17, relwidth=.9)
        self.lbl_numero = Label(self.root, text='Numero:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_numero.place(relx=.60,rely=.72)
        self.lbl_cep = Label(self.root, text='CEP:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_cep.place(relx=.06,rely=.76)
        self.lbl_cidade = Label(self.root, text='Cidade:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_cidade.place(relx=.45,rely=.76)
        self.lbl_bairro = Label(self.root, text='Bairro:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_bairro.place(relx=.06,rely=.81)
        self.lbl_uf = Label(self.root, text='UF:', font=('verdana',10),bg='#CCFFCC')
        self.lbl_uf.place(relx=.45,rely=.81)

        # entradas endereço
        self.entrada_cep = Entry(self.root, font=('verdana',10,'italic'))
        self.entrada_cep.insert(0, "CEP")
        self.entrada_cep.place(relx=.31,rely=.64,relwidth=.18)

        # Botões endereço
        self.btn_buscar_cep = Button(self.root, text='Buscar CEP', font=('verdana',10),command=self.buscar_cep)
        self.btn_buscar_cep.place(relx=.50,rely=.63)
        self.btn_buscar_logradouro = Button(self.root, text='Buscar Endereço', font=('verdana',10), state='disabled')
        self.btn_buscar_logradouro.place(relx=.70,rely=.63)

        #entradas Endereço
        self.entry_rua = Entry(self.root, font=('verdana', 10))
        self.entry_rua.place(relx=.14,rely=.72, relwidth=.45)
        self.entry_numero = Entry(self.root, font=('verdana', 10))
        self.entry_numero.place(relx=.75,rely=.72, relwidth=.15)
        self.entry_cep = Entry(self.root, font=('verdana', 10))
        self.entry_cep.place(relx=.14,rely=.77, relwidth=.25)
        self.entry_cidade = Entry(self.root, font=('verdana', 10))
        self.entry_cidade.place(relx=.57,rely=.77, relwidth=.25)
        self.entry_bairro = Entry(self.root, font=('verdana', 10))
        self.entry_bairro.place(relx=.16, rely=.82, relwidth=.25)
        self.entry_uf = Entry(self.root, font=('verdana', 10))
        self.entry_uf.place(relx=.52, rely=.82, relwidth=.10)

        # botões Main
        self.btn_salvar = Button(self.root, text='SALVAR', font=('verdana',10),bg='lightgreen', command=self.salvar)
        self.btn_salvar.place(relx=.8, rely=.90)
        self.btn_limpar = Button(self.root, text='LIMPAR', font=('verdana',10),bg='lightcoral',state='disabled')
        self.btn_limpar.place(relx=.65, rely=.9)
        self.btn_ver_lista = Button(self.root, text='VER CADASTRADOS', font=('verdana',10),state='disabled')
        self.btn_ver_lista.place(relx=.15, rely=.9)
MainWindow()