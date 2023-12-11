from zeep import Client

# URL do serviço SOAP
soap_url = "http://localhost:3000/?wsdl"

# Criação do cliente SOAP
client = Client(soap_url)

# Chama a função getAllUsers do serviço
result = client.service.getAllUsers()

# Exibe os resultados
print("Lista de Usuários:")
for user in result:
    print(f"ID: {user['id']}, Nome: {user['nome']}, Idade: {user['idade']}")

