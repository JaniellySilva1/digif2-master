from app import db

class Despesas(db.Model):
	__tablename__="despesas"
	id_despesa = db.Column(db.Integer, primary_key = True)
	valor = db.Column(db.String)
	descricao = db.Column(db.String)
	data = db.Column(db.String)

def __init__(self, valor, descricao, data):
	self.valor = valor
	self.descrcao = descricao
	self.data = data

def __repr__(self):
		return "<Despesas {}>".format(self.valor)

























'''from app import db

class Despesas (db.Model):
	__tablename__= "despesas"
	id = db.Column(db.Integer, primary_key = True)
	valordecimal = db.Column(db.Float)
	

	def __init__(self,valordecimal):
		self.valordecimal = valordecimal

	def __repr__(self):
			return "<Despesas {}>".format(self.valordecimal) 


	id = db.Column(db.Integer, primary_key = True)
	descrição = db.Column(db.Script(100))

	def __init__(self, descrição):
		self.descrição = descrição
			
		
	def __repr__(self):
			return "<Despesas {}>".format(self.descrição)
'''