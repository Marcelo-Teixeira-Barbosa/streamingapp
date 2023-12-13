from zeep import Client

# Substitua a URL pelo endereço do seu serviço SOAP
url = 'http://localhost:8000/?wsdl'
client = Client(url)

# Exemplo de chamada para listar todos os usuários
response_users = client.service.list_all_users()
print("Lista de usuários:", response_users)

# Exemplo de chamada para listar todas as músicas
response_songs = client.service.list_all_songs()
print("Lista de músicas:", response_songs)

# Exemplo de chamada para listar playlists de um usuário específico
response_playlists = client.service.list_user_playlists(id_usuario=2)
print("Playlists do usuário com o id 2:", response_playlists)

# Exemplo de chamada para listar músicas de uma playlist específica
response_playlist_songs = client.service.list_playlist_songs(nome="Playlist D")
print("Músicas da Playlist D:", response_playlist_songs)

# Exemplo de chamada para listar playlists que contêm uma música específica
response_song_playlists = client.service.list_song_playlists(song_name="Song A")
print("Playlists que contêm a música Song A:", response_song_playlists)
