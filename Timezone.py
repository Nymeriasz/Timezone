from datetime import datetime
ddd_fuso_area = {
    '68': 'GMT -5 (Horário do Acre)', 
    '82': 'GMT -3 (Horário de Brasília)',
    '96': 'GMT -3 (Horário de Brasília)',
    '92': 'GMT -4 (Horário da Amazônia)',
    '71': 'GMT -3 (Horário de Brasília)',
    '85': 'GMT -3 (Horário de Brasília)',
    '27': 'GMT -3 (Horário de Brasília)',
    '62': 'GMT -3 (Horário de Brasília)',
    '98': 'GMT -3 (Horário de Brasília)',
    '65': 'GMT -4 (Horário da Amazônia)',
    '67': 'GMT -4 (Horário da Amazônia)',
    '31': 'GMT -3 (Horário de Brasília)',
    '91': 'GMT -3 (Horário de Brasília)',
    '83': 'GMT -3 (Horário de Brasília)',
    '41': 'GMT -3 (Horário de Brasília)',
    '81': 'GMT -3 (Horário de Brasília)',
    '86': 'GMT -3 (Horário de Brasília)',
    '21': 'GMT -3 (Horário de Brasília)',
    '84': 'GMT -3 (Horário de Brasília)',
    '51': 'GMT -3 (Horário de Brasília)',
    '69': 'GMT -4 (Horário da Amazônia)',
    '95': 'GMT -4 (Horário da Amazônia)',
    '47': 'GMT -3 (Horário de Brasília)',
    '11': 'GMT -3 (Horário de Brasília)',
    '79': 'GMT -3 (Horário de Brasília)',
    '63': 'GMT -3 (Horário de Brasília)',}

def validar_numero(numero):
    return len(numero) == 10 and numero.isdigit()

def verificar_timezone(numero):
    ddd = numero[:2]
    if ddd in ddd_fuso_area:
        return ddd_fuso_area[ddd]
    else:
        return "Fuso horário desconhecido"

def enviar_mensagem(numero, mensagem):
    print(f"Enviando mensagem para o número {numero}:")
    print(f"Timezone: {verificar_timezone(numero)}")
    print(f"Mensagem: {mensagem}")
while True:
    num_celular = input("Digite o número de telefone (ex: 8399999999): ")
    if validar_numero(num_celular):
        break
    else:
        print("Número de telefone inválido. Tente novamente.")
mensagem = input("Digite a mensagem que deseja enviar: ")
enviar_mensagem(num_celular, mensagem)
hora_atuais = datetime.now()
hora_em_texto = hora_atuais.strftime('%H:%M')
print(f'Horário de envio: {hora_em_texto}')