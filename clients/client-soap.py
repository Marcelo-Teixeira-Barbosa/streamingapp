from zeep import Client

# URL do serviço SOAP
soap_url = "http://localhost:3000/?wsdl"

# Criação do cliente SOAP
client = Client(soap_url)

# Chama a função getAllUsers do serviço
result_users = client.service.getAllUsers()
result_songs = client.service.getAllSongs()
result_user_playlists = client.service.getUserPlaylists(user_id)
result_playlist_songs = client.service.getPlaylistSongs(playlist_id)
result_song_playlists = client.service.getSongPlaylists(song_id)

# Exibe os resultados
print("Lista de Usuários:")
for user in result_users:
    print(f"ID: {user['id']}, Nome: {user['nome']}, Idade: {user['idade']}")

