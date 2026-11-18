import hashlib
# from win10toast import ToastNotifier # pip install win10toast
import time

def gerar_numero(servico):
    # Cria o hash SHA-1 do nome do serviço
    hash_servico = hashlib.sha1(servico.encode()).hexdigest()
    # Filtra apenas os dígitos do hash e mantém os 5 primeiros para formar o "número aleatório"
    numero_aleatorio = ''.join(filter(str.isdigit, hash_servico))[:5]
    if len(numero_aleatorio) < 5:
        numero_aleatorio = numero_aleatorio.ljust(5, '0')
    return numero_aleatorio

def gerar_simbolo(servico):
    simbolos = ['!', '@', '#', '$', '%', '&', '*']
    hash_servico = hashlib.sha1(servico.encode()).hexdigest()
    indice_simbolo = int(hash_servico, 16) % len(simbolos)
    return simbolos[indice_simbolo]


print("Gerador automático de senhas.")
print(u'\u2500' * 50)

servico = input("Entre com o serviço: ")
base = "redstone"
numero = gerar_numero(servico)
simbolo = gerar_simbolo(servico)
senha = base + servico + numero + simbolo

print(u'\u2500' * 50)

print(f"Senha: {senha}")
print("PS: A senha pode sofrer alterações dependendo do site (geralmente mudança no símbolo ou relacionados a letra maíuscula).")
print("Encerrando serviço.")
# toaster = ToastNotifier()
# toaster.show_toast("Senha", f"A senha para {servico} foi gerada com sucesso.", duration=7)
time.sleep(10)
