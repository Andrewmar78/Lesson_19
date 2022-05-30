from app.dao.models.user import User


class UserDAO:
	def __init__(self, session):
		self.session = session

	def get_user_bu_name(self, username):
		return self.session.query(User).filter(User.username == username).first()

	def get_one(self, uid):
		return self.session.query(User).get(uid)

	def create_user(self, user_data):
		entity = User(**user_data)
		self.session.add(entity)
		self.session.commit()
		return entity

	def update(self, user_data):
		self.session.add(user_data)
		self.session.commit()

	def delete(self, uid):
		user_data = self.get_one(uid)
		self.session.delete(user_data)
		self.session.commit()
