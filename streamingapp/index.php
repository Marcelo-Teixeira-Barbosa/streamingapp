<?php

class StreamService {

    public function getAllUsers() {
        $users = array(
            array('id' => 1, 'nome' => 'John Doe', 'idade' => 25),
            array('id' => 2, 'nome' => 'Jane Smith', 'idade' => 30),
            array('id' => 3, 'nome' => 'Bob Johnson', 'idade' => 22)
        );

        return array('users' => $users);
    }

}

$options = array('uri' => 'http://localhost:3000');
$server = new SoapServer('streamingapp.wsdl', $options);
$server->setClass('StreamService');
$server->handle();
