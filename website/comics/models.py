from website.server import db


class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Comic(Base):
	number = db.Column(db.Numeric(), nullable=False)
	title = db.Column(db.String(120), nullable=False)
	notes = db.Column(db.Text, nullable=False)

	def __init__(self, number, title, notes):
		self.number = number
		self.title = title
		self.notes = notes

	def __repr__(self):
		return '<Comic %r>' % self.title
