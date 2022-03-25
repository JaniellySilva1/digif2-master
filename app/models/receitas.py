from app import db

class Receitas(db.Model):
	__tablename__="receitas"
	id_receita = db.Column(db.Integer, primary_key = True)
	valor = db.Column(db.Integer)

def __init__(self, valor):
	self.valor = valor

def __repr__(self):
		return "<Receitas {}>".format(self.valor)

