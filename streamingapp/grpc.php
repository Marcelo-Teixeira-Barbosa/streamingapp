<?php
// grpc.php

require 'vendor/autoload.php';

use Grpc\Server;
use Grpc\ServerBuilder;

class MusicService extends \MusicService\Greeter\GreeterInterface {
    // Implemente as funções do serviço aqui (getAllUsers, getAllSongs, etc.)
}

$server = ServerBuilder::create()->addInterface(MusicService::class)->build();
$server->start();
