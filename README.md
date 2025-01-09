# TMS.CLOUD [![Build Status](https://sistrom.com.br/site/)](https://sistrom.com.br/site/#sistemas)

Sistema Integrado de Gestão de Transporte baseado em Flet

Projeto independente open-source desenvolvido em Python 3 como Flet no Windows, multi plataforma: Web, Mobile, Tablet, GNU/Linux e Windows.


## Dependências

- [Python](https://www.python.org/downloads/) - Versão 3.12+
- [Flet](https://flet.dev/) == 0.24.x
- [google-auth-oauthlib] google-auth-oauthlib
- [firebase-admin] firebase-admin
- [Nuvem-Fiscal](https://nuvemfiscal.com.br) (Opcional) - Necessário para a geração de CT-e e MDF-e, comunicação com SEFAZ, geração do DACTE, DAMDFE, etc.
- [Nginx](https://nginx.org/) (Opcional)

## Instalação:

0. Instalar as bibliotecas/pacotes (no Linux):

```bash
sudo apt install -y ...
sudo apt update
```

1. Instalar dependências:

```bash
pip install -r requirements.txt
```

2. Edite o conteúdo do arquivo **tmscloud/configs/configs.py**

3. Gere um `.env` local


4. Sincronize a base de dados:

```bash
python manage.py migrate
```

5. Crie um usuário (Administrador do sistema):

```bash
python manage.py createsuperuser
```

6. Teste a instalação carregando o servidor de desenvolvimento (http://localhost:8000 no navegador):

```bash
python manage.py runserver
```

## Implementações

- Cadastro de produtos, clientes, empresas, ...
- Login/Logout
- Criação de perfil para cada usuário.
- Definição de permissões para usuários.
- Criação e geração de PDF para orçamentos e pedidos de compra/venda
- Módulo financeiro (Contas à Receber)
- Módulo para controle de ...
- Módulo fiscal:
    - Geração e armazenamento de conhecimento
    - Validação do XML de CT-e/MDF-es
    - Emissão, download, consulta e cancelamento de CT-e/MDF-es **(Testar em ambiente de homologação)**
    - Comunicação com SEFAZ (Consulta de cadastro)
- Interface simples e em português

## Créditos

- [AlgoAKi](...)

## Ajuda

Para relatar bugs ou fazer perguntas utilize o [Issues](https://github.com/nilton-medeiros/tmscloud/issues) ou via email suporte@sistrom.com.br

Como este é um projeto em desenvolvimento, qualquer feedback será bem-vindo.
