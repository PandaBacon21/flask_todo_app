from core import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    category = db.Column(db.String, db.ForeignKey('category.id'))
    user_id = db.Column(db.String, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Todo {self.title}>'