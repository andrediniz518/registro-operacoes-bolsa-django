# Sistema de Registro de Operações na Bolsa - V2

Projeto desenvolvido em **Python** utilizando o framework **Django**, representando a evolução de um sistema de registro de operações na bolsa criado inicialmente para o terminal. Nesta versão, a aplicação ganhou uma interface web e implementa um CRUD completo para cadastro, listagem, edição e exclusão de operações.

## Funcionalidades

* Cadastro de operações
* Listagem de operações cadastradas
* Edição de operações
* Exclusão de operações
* Interface web utilizando Templates do Django
* Painel administrativo do Django

## Tecnologias Utilizadas

* Python 3
* Django
* SQLite (banco de dados padrão do Django)

## Estrutura do Projeto

```text
bolsa/
│
├── bolsa/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── operacoes/
│   ├── migrations/
│   ├── templates/
│   │   └── operacoes/
│   │       ├── home.html
│   │       ├── nova_operacao.html
│   │       ├── editar_operacao.html
│   │       └── excluir_operacao.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
└── db.sqlite3
```

## Conceitos Aplicados

* Arquitetura MTV (Model, Template e View)
* Models
* Views
* Templates
* URLs
* Forms (ModelForm)
* ORM do Django
* Migrations
* CRUD (Create, Read, Update e Delete)

## Como Executar

1. Clone este repositório.

2. Acesse a pasta do projeto.

3. Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
```

4. Ative o ambiente virtual.

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

5. Instale as dependências:

```bash
pip install django
```

6. Execute as migrações:

```bash
python manage.py migrate
```

7. Inicie o servidor:

```bash
python manage.py runserver
```

8. Abra o navegador e acesse:

```
http://127.0.0.1:8000/
```

## Objetivo do Projeto

Este projeto foi desenvolvido como prática de desenvolvimento web com Django, aplicando conceitos de banco de dados, ORM, formulários, rotas e operações CRUD.

## Autor

**André Diniz**

