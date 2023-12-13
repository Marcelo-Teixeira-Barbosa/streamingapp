from spyne import Application, rpc, ServiceBase, Iterable, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import json

class MusicService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def list_all_users(self):
        with open('../db/users.json', 'r') as file:
            users_data = json.load(file)

        user_names = [user["name"] for user in users_data]
        return user_names

    @rpc(_returns=Iterable(Unicode))
    def list_all_songs(self):
        with open('../db/songs.json', 'r') as file:
            songs_data = json.load(file)

        songs_data = [song["nome"] for song in songs_data]
        return songs_data

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_user_playlists(self, id_usuario):
        with open('../db/playlists.json', 'r') as file:
            playlists_data = json.load(file)
        
        # Filtrar playlists com base no id_usuario
        user_playlists = [playlist["nome"] for playlist in playlists_data if playlist["id_usuario"] == int(id_usuario)]

        return user_playlists

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_playlist_songs(self, nome):
        with open('../db/playlists.json', 'r') as file:
            playlists_data = json.load(file)
        
        # Encontrar a playlist com o nome fornecido
        playlist = next((playlist for playlist in playlists_data if playlist["nome"] == nome), None)

        if playlist:
            # Retornar a lista de músicas da playlist encontrada
            return [str(song_id) for song_id in playlist["songs"]]
        else:
            return []

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_song_playlists(self, song_name):
        # Ler dados do arquivo songs.json
        with open('../db/songs.json', 'r') as file:
            songs_data = json.load(file)

        # Encontrar o ID da música com o nome fornecido
        song_id = next((song["id"] for song in songs_data if song["nome"] == song_name), None)

        if song_id is not None:
            # Ler dados do arquivo playlists.json
            with open('../db/playlists.json', 'r') as file:
                playlists_data = json.load(file)

            # Encontrar playlists que contenham o ID da música na lista de músicas
            playlists_containing_song = [playlist["nome"] for playlist in playlists_data if song_id in playlist["songs"]]

            return playlists_containing_song
        else:
            return []

application = Application([MusicService],
                          tns='music_service',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(application)

    server = make_server('0.0.0.0', 8000, wsgi_app)
    print("Listening on port 8000...")
    server.serve_forever()
