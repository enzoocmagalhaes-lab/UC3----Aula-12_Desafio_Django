# The Witcher — Catálogo da trilogia

Projeto Django completo baseado no desafio **Back-end com Python — Aula 12**. Inclui os três jogos cadastrados, análise de cada título, autenticação, CRUD, SQLite e Bootstrap. Interface e documentação em português.

## Iniciar no Windows (CMD)

1. Extraia todo o ZIP. Não execute arquivos de dentro do ZIP.
2. Abra a pasta `catalogo_the_witcher` no Visual Studio Code.
3. Abra o CMD nessa mesma pasta, onde estão `manage.py` e `requirements.txt`.
4. Com Python 3.10 ou superior instalado, execute:

```cmd
iniciar_windows.bat
```

O script cria um ambiente `.venv`, instala o Django, aplica as migrações e pede a criação de um usuário se ainda não existir nenhum. Depois inicia o servidor local. A instalação inicial das dependências requer internet; o CSS do Bootstrap está incluído e não depende de CDN.

Abra **http://127.0.0.1:8000/** no navegador. Deixe o CMD aberto. Para encerrar, use `Ctrl+C`. Se a porta 8000 já estiver ocupada pelo catálogo anterior, encerre aquele servidor antes de iniciar este.

O script é uma conveniência para CMD. Os comandos manuais abaixo executam o mesmo procedimento e ajudam a diagnosticar qualquer erro.

## Instalação manual pelo CMD

Execute um comando por vez:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Se o comando `py` não existir, tente `python -m venv .venv`. Escolha seu login e senha em `createsuperuser`; os caracteres da senha não aparecem enquanto você digita. Não há credenciais padrão. Nos próximos acessos, basta ativar o ambiente e executar `python manage.py runserver`.

Para usar outra porta:

```cmd
python manage.py runserver 8001
```

Nesse caso, abra **http://127.0.0.1:8001/**.

Linux/macOS: use `python3 -m venv .venv`, ative com `source .venv/bin/activate` e prossiga com os mesmos comandos `python` da instalação manual.

## Os três jogos

| Jogo | Lançamento original | Foco da análise |
| --- | --- | --- |
| The Witcher | 2007 | Identidade, escolhas morais, alquimia e acabamento da estreia |
| The Witcher 2: Assassins of Kings | 2011 | Política, ramificações, dificuldade e aprendizado dos sistemas |
| The Witcher 3: Wild Hunt | 2015 | Mundo aberto, histórias pessoais, interface e escala |

Cada ficha contém história, jogabilidade, pontos fortes, pontos fracos, resultado comercial, melhorias, aprendizados e links para as fontes. `CONTEUDO_E_FONTES.md` oferece os mesmos textos para leitura fora do programa.

A análise distingue fatos documentados, recepção crítica e inferências editoriais. As plataformas são as do lançamento original, não uma lista de todos os ports. Os anos são os das estreias, não os das Enhanced Editions. Os números de vendas são marcos históricos explicitamente datados, não totais atuais. A análise não revela os finais.

## Requisitos do PDF atendidos

| Requisito | Onde está |
| --- | --- |
| Model com atributos | `jogos/models.py`: classe `Jogo` |
| Migrações criadas e aplicadas | `jogos/migrations/` e banco `db.sqlite3` |
| Página inicial de boas-vindas | `/` e `home.html` |
| Listagem pelo ORM e `{% for %}` | `/jogos/`, `Jogo.objects.all()` e `lista.html` |
| Detalhes ao clicar em um item | `/jogos/<id>/` e `detalhe.html` |
| Create e Update com ModelForm | `JogoForm` em `forms.py`; edição usa `instance` |
| Delete com confirmação e POST | `confirmar_exclusao.html` e `excluir_jogo`; GET nunca exclui |
| Login nativo do Django | `include('django.contrib.auth.urls')` em `config/urls.py` |
| Tela de login | `jogos/templates/registration/login.html` |
| `@login_required` | Nas views criar, editar e excluir |
| Botões ocultos para visitantes | `{% if user.is_authenticated %}` |
| Herança de templates | Páginas estendem `base.html` |
| Bootstrap, menu e rodapé | `base.html` e CSS local do Bootstrap |
| Proteção dos formulários | `{% csrf_token %}` e middleware CSRF |

São cinco templates principais: Home, Listagem, Detalhes, Formulário (compartilhado entre criar e editar) e Confirmação de exclusão. O login é uma tela adicional exigida pelo PDF. O Django Admin é um recurso extra.

## Uso e edição no Visual Studio Code

Visitantes podem consultar as fichas. Clique em **Entrar** e use sua conta para adicionar, editar e excluir. Qualquer usuário autenticado pode modificar registros, conforme o exercício. O botão **Sair** utiliza POST.

Para demonstrar o CRUD sem alterar a trilogia, cadastre um jogo de teste com ordem 4, edite-o e depois exclua-o. O painel `/admin/` aceita usuários com acesso administrativo.

| Arquivo | Função |
| --- | --- |
| `jogos/models.py` | Dados persistidos: o Model |
| `jogos/views.py` | Consultas, formulários e respostas: as Views |
| `jogos/templates/` | Páginas HTML: os Templates |
| `jogos/forms.py` | Formulário de criação e edição |
| `jogos/validators.py` | Validação das referências HTTP/HTTPS |
| `jogos/urls.py` | Endereços das páginas |
| `jogos/static/jogos/estilo.css` | Aparência do catálogo |
| `config/settings.py` | Configurações do projeto |
| `jogos/tests.py` | Testes automatizados |

Ao alterar campos do model, execute:

```cmd
python manage.py makemigrations
python manage.py migrate
```

Para alterar apenas o texto das análises, use o formulário de edição no navegador. Nas referências, escreva uma fonte por linha: `Nome da fonte | https://endereco`.

## Banco e verificação

O SQLite entregue contém apenas os três jogos e as migrações aplicadas, sem usuários ou sessões. A migração `0002_trilogia_inicial.py` também preenche automaticamente um banco novo. Executar `migrate` novamente não duplica os jogos nem desfaz suas edições. Este catálogo é independente do projeto de O Senhor dos Anéis.

```cmd
python manage.py check
python manage.py test
```

A suíte tem 14 testes de páginas, dados iniciais, CRUD, autenticação, redirecionamento, validação, fontes, CSRF, exclusão por POST e catálogo vazio. Os testes usam um banco temporário, sem modificar seus dados.

Configuração para uso local em aula, com `DEBUG` ativo por padrão. Publicação real exige configuração própria de servidor, estáticos, domínio, HTTPS e chave secreta. Recuperação de senha por e-mail não faz parte do exercício.

## Tecnologias e créditos

Python 3.10+, Django 5.2.17, SQLite e Bootstrap 5.3.3. Bootstrap incluído com sua licença MIT em `jogos/static/vendor/BOOTSTRAP-LICENSE.txt`. Os ornamentos visuais são CSS; não são capas oficiais. Este é um projeto acadêmico independente, sem afiliação à CD PROJEKT RED.

Referência técnica: https://docs.djangoproject.com/en/5.2/topics/auth/default/
