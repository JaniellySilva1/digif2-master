from app import db

class Usuario(db.Model):
	__tablename__= "usuario"
	id = db.Column(db.Integer, primary_key = True)
	email = db.Column(db.String(100))
	nome = db.Column(db.String(100))
	senha = db.Column(db.String(100))

	def __init__(self, nome, email, senha):
			self.email = email
			self.nome = nome
			self.senha = senha
		
	def __repr__(self):
			return "<Usuario {}>".format(self.nome)