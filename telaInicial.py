import PySimpleGUI as sg
from calculo import calculo
from mensagem import mensagem

sg.theme('Green')

layout = [
    [sg.Text("Altura(em centímetros)",size=(17,1)),sg.Input(key='altura',size=(5,1))],
    [sg.Text("Peso(em quilos)",size=(17,1)),sg.Input(key='peso',size=(5,1))],
    [sg.Text(key='alerta')],
    [sg.Text(key='imc')],
    [sg.Button('Calcular',key='calcular')]
]

window = sg.Window('IMC', layout=layout)
#leitura
while True:
    envent,values = window.read()
    #print(envent)

    if envent == sg.WIN_CLOSED:
        break
    
    if envent == 'calcular':
        imc = calculo(values['altura'],values['peso'])
        resposta = mensagem(imc)
        if resposta == 'Sobrepeso':   
            window['alerta'].update(resposta,text_color='yellow')
        elif resposta == 'Obesidade Grau II':   
            window['alerta'].update(resposta,text_color='orange')
        elif resposta == 'Obesidade Grave':   
            window['alerta'].update(resposta,text_color='red')
        else:
            window['alerta'].update(resposta,text_color='black')
        window['imc'].update(f'IMC {imc:.1f}')