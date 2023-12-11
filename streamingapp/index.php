<?php

class StreamService {

    private $db;

    public function __construct() {
        $this->db = new PDO('mysql:host=mysql;dbname=streamingapp', 'stream', '123456');
        $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }

    public function getAllUsers() {
        $stmt = $this->db->query('SELECT * FROM users');
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getAllSongs() {
        $stmt = $this->db->query('SELECT * FROM songs');
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getUserPlaylists($userId) {
        $stmt = $this->db->prepare('SELECT * FROM playlists WHERE user_id = :userId');
        $stmt->bindParam(':userId', $userId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getPlaylistSongs($playlistId) {
        $stmt = $this->db->prepare('SELECT songs.* FROM songs 
            JOIN playlist_songs ON songs.id = playlist_songs.song_id
            WHERE playlist_songs.playlist_id = :playlistId');
        $stmt->bindParam(':playlistId', $playlistId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function getSongPlaylists($songId) {
        $stmt = $this->db->prepare('SELECT playlists.* FROM playlists
            JOIN playlist_songs ON playlists.id = playlist_songs.playlist_id
            WHERE playlist_songs.song_id = :songId');
        $stmt->bindParam(':songId', $songId, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}

$options = array('uri' => 'http://localhost:3000');
$server = new SoapServer('streamingapp.wsdl', $options);
$server->setClass('StreamService');
$server->handle();
