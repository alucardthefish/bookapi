from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/api/book*": {"origins": "*"}})

# Model

class BookModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    read = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Book(title = {title}, author = {author}, read = {read})"


db.create_all()

book_put_args = reqparse.RequestParser()
book_put_args.add_argument("title", type=str, help="Title of the book is required", required=True)
book_put_args.add_argument("author", type=str, help="Author of the book", required=True)
book_put_args.add_argument("read", type=bool, help="Read the book", required=True)

book_update_args = reqparse.RequestParser()
book_update_args.add_argument("title", type=str, help="Title of the book is required")
book_update_args.add_argument("author", type=str, help="Author of the book")
book_update_args.add_argument("read", type=bool, help="Read the book")

resource_fields = {
    'id' : fields.Integer,
    'title' : fields.String,
    'author' : fields.String,
    'read' : fields.Boolean
}


# API

class Books(Resource):

    @marshal_with(resource_fields)
    def get(self):
        books = BookModel.query.all()
        if len(books) > 0:
            return books, 200
        return None, 401

    @marshal_with(resource_fields)
    def post(self):
        args = book_put_args.parse_args()
        book = BookModel(title=args['title'], author=args['author'], read=args['read'])
        db.session.add(book)
        db.session.commit()
        return book, 200


class Book(Resource):

    @marshal_with(resource_fields)
    def get(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message="Book not found")
        return result
    

    @marshal_with(resource_fields)
    def put(self, book_id):
        args = book_update_args.parse_args()
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message="book doesn't exist, cannot update")
        
        if args['title']:
            result.title = args['title']
        if args['author']:
            result.author = args['author']
        if args['read']:
            result.read = args['read']
        
        db.session.commit()
        return result


    def delete(self, book_id):
        result = BookModel.query.filter_by(id=book_id).first()
        if not result:
            abort(404, message="Book doesn't exist")
        db.session.delete(result)
        db.session.commit()
        return 'Book deleted successfully', 204
    

api.add_resource(Books, "/api/book")
api.add_resource(Book, "/api/book/<int:book_id>")


if __name__ == "__main__":
    app.run(debug=True)

