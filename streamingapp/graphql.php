<?php
// graphql.php
require 'vendor/autoload.php';

use TheCodingMachine\GraphQLite\GraphQLite;

$graphql = new GraphQLite(/* options */);

// Implemente os tipos e resolvers do serviço aqui (getAllUsers, getAllSongs, etc.)

$graphql->handleRequest();
?>
