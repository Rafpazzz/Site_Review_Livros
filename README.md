# Site de Reviews de Livros

Este projeto pessoal consistem em um site pode armazenar em um baco de dados varios livros e os usuarios podem escrever avaliações sobre oque acham do livro e tambem escolher um rating para cada livro

Esse site consite em um CRUD que o usuario pode adcionar sua avaliação, atualiza-la e excluir-la.

#Tecnologias utilizadas 
  -Python
  -Django
  -MySQLWorkbanch

#Detalhes de Desenvolvimento
O sistema possue uma altenticação basica ja presente no Django e as pagias que o usuario navegam possuem uma camada que somete os logados podem acessar.



SITE_REVIEW_LIVROS/
├── 📂 setup/                # ⚙️ Coração do projeto (Configurações Globais)
│   ├── settings.py          # Configurações de banco de dados, apps instalados e segurança
│   ├── urls.py              # Roteamento principal (a "portaria" das URLs)
│   └── asgi.py / wsgi.py    # Pontos de entrada para o servidor web
│
├── 📂 accounts/             # 👤 Módulo de Gestão de Usuários
│   ├── models.py            # Tabelas de usuários (se houver customização)
│   ├── views.py             # Lógica de Login, Cadastro e Logout
│   └── templates/           # Páginas HTML de login/registro
│
├── 📂 book/                 # 📚 Módulo de Catálogo de Livros
│   ├── models.py            # Definição da estrutura do Livro (Título, Autor, etc.)
│   ├── views.py             # Lógica de listagem e detalhes dos livros
│   └── urls.py              # Rotas específicas de livros (ex: /livro/1)
│
├── 📂 reviews/              # ⭐ Módulo de Avaliações/Resenhas
│   ├── models.py            # Tabela que liga Usuário + Livro + Nota
│   ├── forms.py             # Formulário para escrever a resenha
│   └── views.py             # Lógica para salvar e exibir comentários
│
├── 📂 django/               # Ambiente Virtual do Python para dowload das bibliotecas
├── db.sqlite3               # Banco de dados local (desenvolvimento)
└── manage.py                # Script utilitário do Django (rodar server, criar migrations)
