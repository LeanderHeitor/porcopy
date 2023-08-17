from json import dumps, loads
import os
import tkinter as tk

def BiogasEnergia():
    biogas = quantidadePorcos * 0.24
    biogas_label['text'] = f'Produção de biogás: {biogas}m³'
    energia_label['text'] = f'Produção de Energia: {round(biogas * 1.25)}KWh'

arquivos = os.listdir()
arquivos_txt = (arquivo for arquivo in arquivos if arquivo.endswith('.txt'))
ArquivoNaovazio = (arquivo for arquivo in arquivos_txt if os.stat(arquivo).st_size != 0)

quantidadePorcos = 0
for arquivo in ArquivoNaovazio:
    f = open(f'{arquivo}', 'r')
    por_disserializado = loads(f.read())
    f.close()
    quantidadePorcos += len(por_disserializado)

def ciclo_completo():
    producaoDejetos = 100 * quantidadePorcos
    producaoDejetos_label['text'] = f'Produção de dejetos: {producaoDejetos}L/dia'
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30}L/mês'
    BiogasEnergia()

def produtora_leitao():
    producaoDejetos = 60 * quantidadePorcos 
    producaoDejetos_label['text'] = f'Produção de dejetos: {producaoDejetos} L/dia'
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30} L/mês'
    BiogasEnergia()

def producao_terminados():
    producaoDejetos = 7.5 * quantidadePorcos
    producaoDejetos_label['text'] = f'Produção de dejetos: {producaoDejetos} L/dia'
    producaoDejetos_mes_label['text'] = f'Produção de dejetos: {producaoDejetos * 30} L/mês'
    BiogasEnergia()

root = tk.Tk()
root.title('Biogás e Energia')
root.geometry('500x300')

frame1 = tk.Frame(root)
frame1.pack(side='top', pady=10)

label1 = tk.Label(frame1, text='Defina o tipo de produção de sua granja:')
label1.pack(side='left')

frame2 = tk.Frame(root)
frame2.pack(side='top', pady=10)

button1 = tk.Button(frame2, text='Ciclo Completo', command=ciclo_completo)
button1.pack(side='left')

button2 = tk.Button(frame2, text='Produtora de Leitão', command=produtora_leitao)
button2.pack(side='left')

button3 = tk.Button(frame2, text='Produção de terminados', command=producao_terminados)
button3.pack(side='left')

frame3 = tk.Frame(root)
frame3.pack(side='top', pady=10)

producaoDejetos_label = tk.Label(frame3, text='')
producaoDejetos_label.pack(side='top')

producaoDejetos_mes_label = tk.Label(frame3, text='')
producaoDejetos_mes_label.pack(side='top')

biogas_label = tk.Label(frame3, text='')
biogas_label.pack(side='top')

energia_label = tk.Label(frame3, text='')
energia_label.pack(side='top')

root.mainloop()
