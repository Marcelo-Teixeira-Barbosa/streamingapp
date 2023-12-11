<?php
// soap.php

class MusicService {
    // Implemente as funções do serviço aqui (getAllUsers, getAllSongs, etc.)
}

$options = [
    'uri' => 'http://localhost/soap.php',
    'location' => 'http://localhost/soap.php',
];

$server = new SoapServer(null, $options);
$server->setClass('MusicService');
$server->handle();
?>
