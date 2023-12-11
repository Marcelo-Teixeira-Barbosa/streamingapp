<?php

// Importa a conexão com o banco de dados
require_once 'db.php';

// Obtém a conexão do arquivo db.php
global $DB;

// Obtém o método da requisição (GET, POST, etc.)
$method = $_SERVER['REQUEST_METHOD'];

// Rota para listar todos os usuários
if ($_GET['resource'] === 'users') {
    if ($method === 'GET') {
        // Operação para listar todos os usuários
        $result = $DB->query("SELECT * FROM users");
        $users = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($users);
    }
}

// Rota para listar todas as músicas
elseif ($_GET['resource'] === 'songs') {
    if ($method === 'GET') {
        // Operação para listar todas as músicas
        $result = $DB->query("SELECT * FROM songs");
        $songs = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($songs);
    }
}

// Rota para listar todas as playlists de um usuário específico
elseif ($_GET['resource'] === 'playlists' && isset($_GET['user_id'])) {
    $user_id = $_GET['user_id'];

    if ($method === 'GET') {
        // Operação para listar todas as playlists de um usuário
        $result = $DB->query("SELECT * FROM playlists WHERE user_id = $user_id");
        $playlists = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($playlists);
    }
}

// Rota para listar todas as músicas de uma determinada playlist
elseif ($_GET['resource'] === 'songs' && isset($_GET['playlist_id'])) {
    $playlist_id = $_GET['playlist_id'];

    if ($method === 'GET') {
        // Operação para listar todas as músicas de uma playlist
        $result = $DB->query("SELECT songs.* FROM songs
                             JOIN playlist_songs ON songs.id = playlist_songs.song_id
                             WHERE playlist_songs.playlist_id = $playlist_id");
        $songs = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($songs);
    }
}

// Rota para listar todas as playlists que contêm uma determinada música
elseif ($_GET['resource'] === 'playlists' && isset($_GET['song_id'])) {
    $song_id = $_GET['song_id'];

    if ($method === 'GET') {
        // Operação para listar todas as playlists que contêm uma música
        $result = $DB->query("SELECT playlists.* FROM playlists
                             JOIN playlist_songs ON playlists.id = playlist_songs.playlist_id
                             WHERE playlist_songs.song_id = $song_id");
        $playlists = $result->fetch_all(MYSQLI_ASSOC);
        echo json_encode($playlists);
    }
} else {
    // Rota inválida
    http_response_code(404);
    echo json_encode(['error' => 'Rota inválida']);
}

?>
