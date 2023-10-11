from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create the extension
db = SQLAlchemy()
# Initialise the app with the extension
db.init_app(app)


# Create table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional element to identify each book object by its title
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database, Requires application context.
with app.app_context():
    db.create_all()

# Create record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
