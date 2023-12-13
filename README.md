# Trabalho de computação distribuida

# Aplicação escolhida: Serviço de Streaming de Músicas

# Equipe:
- Erick Bernardo
- Marcelo Barbosa
- Leonardo Pontes

# Professor:
- Nabor Mendonça

# Introdução

# Introdução - Comparação entre Tecnologias de Comunicação

Este documento apresenta uma breve comparação entre quatro tecnologias populares de comunicação: SOAP, REST, GraphQL e gRPC.

## SOAP (Simple Object Access Protocol)

- **Origem:** Introduzido pela Microsoft na década de 1990.
- **Principais Características:**
  - Utiliza XML como formato de mensagem.
  - Define regras rígidas e estritas.
  - Suporta transações ACID.
  - Requer contrato formal (WSDL).
- **Vantagens:**
  - Suporte a transações ACID.
  - Contratos formais através de WSDL.
  - Extensibilidade e segurança integradas.
- **Desvantagens:**
  - Overhead devido ao uso de XML.
  - Menos eficiente em termos de desempenho.
  - Menos flexível comparado a tecnologias mais recentes.

## REST (Representational State Transfer)

- **Origem:** Proposto por Roy Fielding em 2000.
- **Principais Características:**
  - Arquitetura centrada em recursos.
  - Opera com operações HTTP padrão.
  - Utiliza formatos de dados leves como JSON ou XML.
  - Stateless (sem estado).
- **Vantagens:**
  - Simplicidade e facilidade de uso.
  - Eficiência e desempenho devido à leveza dos formatos de dados.
  - Stateless para facilitar escalabilidade.
- **Desvantagens:**
  - Falta de um padrão formal para descrição de serviços.
  - Limitações na descrição e descoberta de serviços.

## GraphQL

- **Origem:** Desenvolvido pelo Facebook em 2015.
- **Principais Características:**
  - Permite ao cliente especificar estrutura da resposta desejada.
  - Utiliza uma única URL para todas as operações.
  - Fornece linguagem de consulta flexível.
  - Pode ser usado com qualquer sistema de armazenamento de dados.
- **Vantagens:**
  - Evita over-fetching e under-fetching de dados.
  - Flexibilidade na definição da estrutura da resposta.
  - Pode ser mais eficiente para redes com largura de banda limitada.
- **Desvantagens:**
  - Maior complexidade na implementação em comparação com REST.
  - Requer camada de tradução para converter consultas GraphQL em chamadas de serviço.

## gRPC (gRPC Remote Procedure Calls)

- **Origem:** Desenvolvido pela Google em 2015.
- **Principais Características:**
  - Usa Protocol Buffers como formato de dados padrão.
  - Baseado em HTTP/2 para melhor eficiência e desempenho.
  - Suporta RPC bidirecional.
  - Gera código cliente e servidor automaticamente.
- **Vantagens:**
  - Alta eficiência com Protocol Buffers e HTTP/2.
  - Geração automática de código facilita o desenvolvimento.
  - Suporte nativo para comunicação bidirecional.
- **Desvantagens:**
  - Pode ser complexo para iniciantes devido à ênfase em RPC.
  - Menos legível do que JSON ou XML para humanos.

Escolher a tecnologia adequada dependerá dos requisitos específicos do projeto, das preferências da equipe e do contexto de uso. Cada tecnologia possui seus próprios pontos fortes e limitações.

# Aplicação principal: Serviço de Streaming de Músicas

## Instalação local

### Inicialização para linux
- python3 -m venv .venv
- source .venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- apt-get update
- apt install php8.1-cli

### Inicializando servidor soap
- cd streamingapp
- python3 soap.py

### Inicializando client soap
- cd clients
- python3 client-soap.py

### Iniciandlizando servidor rest
- cd streamingapp
- python3 rest.py

### Inicializando client rest
- cd streamingapp
- php client-rest.php