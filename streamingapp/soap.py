from spyne import Application, rpc, ServiceBase, Iterable, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class MusicService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def list_all_users(self):
        # Implementar lógica para listar dados de todos os usuários
        return ["User1", "User2", "User3"]

    @rpc(_returns=Iterable(Unicode))
    def list_all_songs(self):
        # Implementar lógica para listar dados de todas as músicas
        return ["Song1", "Song2", "Song3"]

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_user_playlists(self, username):
        # Implementar lógica para listar dados de todas as playlists de um usuário
        return ["Playlist1", "Playlist2", "Playlist3"]

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_playlist_songs(self, playlist_name):
        # Implementar lógica para listar dados de todas as músicas de uma playlist
        return ["SongA", "SongB", "SongC"]

    @rpc(Unicode, _returns=Iterable(Unicode))
    def list_song_playlists(self, song_name):
        # Implementar lógica para listar dados de todas as playlists que contêm uma música
        return ["PlaylistX", "PlaylistY", "PlaylistZ"]

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
