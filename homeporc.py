import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

def lista_de_arquivos():
    arquivos = os.listdir()
    arquivos_txt = [arquivo for arquivo in arquivos if arquivo.endswith('.txt')]
    arquivo_sem_extensao = [os.path.splitext(arquivo)[0] for arquivo in arquivos_txt]
    return arquivo_sem_extensao

def adicionar_porcos(nome_arquivo):
    idade = int(simpledialog.askstring("Idade", "Digite a idade do seu animal: "))
    sexo = simpledialog.askstring("Sexo", "Digite o sexo do seu animal: ")
    raca = simpledialog.askstring("Raça", "Digite a raça do seu animal: ")
    peso = int(simpledialog.askstring("Peso", "Digite o peso do seu animal(Kg): "))
    racao_dia = int(simpledialog.askstring("Ração por dia", "Digite a quantidade de ração que o seu animal come por dia: "))
    
    vacina = []
    op = tk.messagebox.askyesno("Vacina", "O seu animal já tomou vacina?")
    
    if op:
        ask = int(simpledialog.askstring("Vacinas", "Quantas vacinas o seu animal tomou?"))
        for _ in range(ask):
            vacina.append(simpledialog.askstring("Vacinas", "Digite o nome da vacina: "))
    
    por = {'Idade': idade, 'Sexo': sexo, 'Raça': raca, 'Peso': peso, 'Ração por dia': racao_dia, 'Vacinas': vacina}
    
    try:
        with open(f'{nome_arquivo}.txt', 'r+') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = {}  # Se o JSON estiver vazio ou inválido, inicializa com um dicionário vazio
    except FileNotFoundError:
        dados = {}
    
    identificacao = simpledialog.askstring("Identificação", "Digite uma identificação para o animal: ")
    dados[identificacao] = por
    
    with open(f'{nome_arquivo}.txt', 'w') as f:
        json.dump(dados, f)

def remover_baia(nome_baia):
    try:
        os.remove(f'{nome_baia}.txt')
        arquivo_sem_extensao.remove(nome_baia)
        baia_listbox.delete(tk.ACTIVE)
        messagebox.showinfo("Sucesso", f"Baia '{nome_baia}' removida com sucesso!")
    except FileNotFoundError:
        messagebox.showerror("Erro", f"Baia '{nome_baia}' não encontrada!")

def listar_porcos(nome_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f:
            conteudo = f.read()
            if conteudo.strip() == "":
                return []  # Retorna uma lista vazia se o arquivo estiver vazio
            dados = json.loads(conteudo)
            porcos = []
            for identificacao, porco in dados.items():
                porcos.append(f"Identificação: {identificacao}, Idade: {porco['Idade']} anos, Sexo: {porco['Sexo']}")
            return porcos
    except FileNotFoundError:
        return []

def remover_porco(nome_arquivo, identificacao):
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f:
            dados = json.load(f)
        if identificacao in dados:
            del dados[identificacao]
            with open(f'{nome_arquivo}.txt', 'w') as f:
                json.dump(dados, f)
            messagebox.showinfo("Sucesso", f"Porco '{identificacao}' removido com sucesso!")
            listar_porcos_baia(nome_arquivo)  # Atualiza a lista de porcos na baia após a remoção
        else:
            messagebox.showerror("Erro", f"Porco '{identificacao}' não encontrado!")
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo da baia não encontrado!")
    except json.JSONDecodeError:
        messagebox.showerror("Erro", "Erro ao carregar dados da baia!")

def listar_porcos_baia(nome_arquivo):
    try:
        with open(f'{nome_arquivo}.txt', 'r') as f:
            conteudo = f.read()
            if conteudo.strip() == "":
                return []  # Retorna uma lista vazia se o arquivo estiver vazio
            dados = json.loads(conteudo)
            porcos = []
            for identificacao, porco in dados.items():
                porcos.append(f"Identificação: {identificacao}, Idade: {porco['Idade']} anos, Sexo: {porco['Sexo']}")
            return porcos
    except FileNotFoundError:
        return []

def main():
    root = tk.Tk()
    root.title("Gerenciamento de Porcos")
    root.geometry("1280x720")  # Definindo o tamanho da janela

    arquivo_sem_extensao = lista_de_arquivos()

    def listar_baias():
        baia_listbox.delete(0, tk.END)
        for i, nome in enumerate(arquivo_sem_extensao, start=1):
            baia_listbox.insert(tk.END, f'Baia {i}: {nome}')

    def adicionar_baia():
        nome_baia = simpledialog.askstring("Adicionar Baia", "Adicione o nome da baia:")
        if nome_baia:
            try:
                with open(f'{nome_baia}.txt', 'x'):
                    messagebox.showinfo("Sucesso", "Baia cadastrada com sucesso!")
                    arquivo_sem_extensao.append(nome_baia)
                    listar_baias()
            except FileExistsError:
                messagebox.showerror("Erro", "Baia já cadastrada!")

    def baia_selecionada_event(event):
        if baia_listbox.curselection():
            selected_index = baia_listbox.curselection()[0]
            nome_baia = arquivo_sem_extensao[selected_index]
            baia_label.config(text=f"Baia selecionada: {nome_baia}")
            baia_frame.pack()
            adicionar_porco_button.config(command=lambda: adicionar_porcos(nome_baia))
            listar_porcos_button.config(command=lambda: listar_porcos_baia(nome_baia))
            remover_porco_button.config(command=lambda: remover_porco(nome_baia, identificacao_entry.get()))
            baia_listbox2.delete(0, tk.END)  # Limpa a lista de porcos quando uma baia é selecionada
            porcos_text.config(state=tk.DISABLED)  # Desabilita a caixa de texto dos porcos

            # Lista os porcos da baia selecionada
            porcos = listar_porcos_baia(nome_baia)
            porcos_text.config(state=tk.NORMAL)
            porcos_text.delete(1.0, tk.END)
            if porcos:
                porcos_text.insert(tk.END, "\n".join(porcos))
            else:
                porcos_text.insert(tk.END, "Não há porcos nesta baia.")
            porcos_text.config(state=tk.DISABLED)

    baia_listbox = tk.Listbox(root, font=("Helvetica", 14))
    baia_listbox2 = tk.Listbox(root, font=("Helvetica", 14))
    listar_baias()

    baia_frame = tk.Frame(root)
    baia_label = tk.Label(baia_frame, text="Baia selecionada:", font=("Helvetica", 16))
    adicionar_porco_button = tk.Button(baia_frame, text="Adicionar Porco", font=("Helvetica", 14))
    listar_porcos_button = tk.Button(baia_frame, text="Listar Porcos", font=("Helvetica", 14))
    remover_porco_button = tk.Button(baia_frame, text="Remover Porco", font=("Helvetica", 14))
    identificacao_entry = tk.Entry(baia_frame, font=("Helvetica", 12))  # Campo de entrada para a identificação do porco a ser removido
    porcos_text = scrolledtext.ScrolledText(baia_frame, state=tk.DISABLED, height=10, width=60, font=("Helvetica", 12))  # Caixa de texto para listar porcos

    baia_label.pack()
    adicionar_porco_button.pack()
    identificacao_entry.pack()  # Adicionar o campo de entrada de identificação
    remover_porco_button.pack()
    listar_porcos_button.pack()
    porcos_text.pack()

    adicionar_baia_button = tk.Button(root, text="Adicionar Baia", command=adicionar_baia, font=("Helvetica", 14))
    sair_button = tk.Button(root, text="Sair", command=root.destroy, font=("Helvetica", 14))

    baia_listbox.pack()
    baia_listbox2.pack()
    adicionar_baia_button.pack()
    sair_button.pack()

    baia_listbox.bind("<<ListboxSelect>>", baia_selecionada_event)

    root.mainloop()

if __name__ == "__main__":
    main()
