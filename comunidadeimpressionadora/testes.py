from main import app, database
from comunidadeimpressionadora.models import Usuario, Post

# with app.app_context():
#     database.create_all()

# with app.app_context():
#     usuario = Usuario(username="Lira", email="lira@gmail.com", senha=123456)
#     usuario2 = Usuario(username="Joao", email="joao@gmail.com", senha=123456)

#     database.session.add(usuario)
#     database.session.add(usuario2)

#     database.session.commit()

# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario =  Usuario.query.first()
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)
#     print(primeiro_usuario.posts)
#     print("******")
#     usuario_teste = Usuario.query.filter_by(email='lira@gmail.com').first()
#     print(usuario_teste)
#     print(usuario_teste.username)

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Meu primeiro post", corpo='Corpo do primeiro post')

#     database.session.add(meu_post)

#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post.titulo)
#     print(post.autor.email)

# with app.app_context():
#     database.drop_all()
#     database.create_all()
