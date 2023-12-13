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
response_playlists = client.service.list_user_playlists(username="User1")
print("Playlists do usuário User1:", response_playlists)

# Exemplo de chamada para listar músicas de uma playlist específica
response_playlist_songs = client.service.list_playlist_songs(playlist_name="Playlist1")
print("Músicas da Playlist1:", response_playlist_songs)

# Exemplo de chamada para listar playlists que contêm uma música específica
response_song_playlists = client.service.list_song_playlists(song_name="SongA")
print("Playlists que contêm a música SongA:", response_song_playlists)
