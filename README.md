# infra-imagem-basica
Exemplo de criação de imagens básicas através infraestrutura automatizada.

## Pré-requisitos
- [Packer](https://packer.io/) instalado
- [Drone.io](https://drone.io/) instalado e integrado com o Github
- Credenciais de acesso à AWS cadastradas como _secret_ no Drone

## Geração das AMIs

### MySQL
- `cd mysql`
- `packer build mysql.json`

### Apache/PHP
- `cd apache-php`
- `packer build apache-php.json`
