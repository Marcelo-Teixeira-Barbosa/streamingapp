<?php

// Verifica se a extensão mysqli está habilitada
if (extension_loaded('mysqli')) {
    error_log("A extensão mysqli está habilitada.");
} else {
    error_log("A extensão mysqli NÃO está habilitada.");
    print_backtrace();
    exit;
}

// Obtém informações sobre a versão do MySQLi
error_log("Versão do MySQLi: " . mysqli_get_client_version());

// Tenta criar uma conexão rápida para testar a disponibilidade do MySQL
$mysqli = new mysqli("mysql", "stream", "123456", "streamingapp", 3306);

if ($mysqli->connect_error) {
    error_log("Erro de conexão: " . $mysqli->connect_error);
    print_backtrace();
    exit;
}

error_log("Conexão bem-sucedida!");

// Fecha a conexão
$mysqli->close();

function print_backtrace() {
    $trace = debug_backtrace();
    error_log("Trace:");
    foreach ($trace as $entry) {
        error_log("Arquivo: " . $entry['file'] . ", Linha: " . $entry['line']);
    }
}
?>
