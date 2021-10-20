from flask_restful import Api, Resource, marshal_with, abort, reqparse, fields
import config
from flask import jsonify
from models.director import Director, director_field
from models.film import Film, film_field

from middleware import test_decorator, login_mdw

app = config.app
db = config.db
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', type=str, help="The title of the movie")
parser.add_argument('director', type=str, help="Name of the director")
parser.add_argument('year', type=str, help="The released year of the movie")

@api.resource('/test')
class Test(Resource):

    test_field = {
        'director_id': fields.String,
        'name': fields.String,
    }

    @test_decorator()
    @marshal_with(director_field)
    def get(self):
        result = Director.query.filter_by(director_id=1).first()
        print(result.films[0].title)
        if not result:
            abort(404, message="Video doesnt exist")
        return result, 201

@api.resource('/login')
class Login(Resource):
    @login_mdw()
    def post(self):
        return {'message': 'login successfull'}, 200

@api.resource('/film/<int:film_id>')
class FilmDetail(Resource):
    @marshal_with(film_field)
    def get(self, film_id):
        result = Film.query.filter_by(film_id=film_id).first()
        if not result:
            abort(404, message='Movie doesnt exist')
        return result, 200

@api.resource('/search')
class SearchResult(Resource):
    @marshal_with({'data': fields.List(fields.Nested(film_field))})
    def post(self):
        args = parser.parse_args()
        title = args['title']
        director = args['director']
        year = args['year']
        if year:
            year = '(' + year + ')'
        result_by_title = Film.query.filter_by(title=title).all()
        result_by_year = Film.query.filter_by(release_year=year).all()
        result_by_director = Director.query.filter_by(name=director).first()
        final_result = []
        if result_by_director:
            final_result += result_by_director.films
        if result_by_title:
            final_result += result_by_title
        if result_by_year:
            final_result += result_by_year
        final_result = set(final_result)
        if result_by_director:
            final_result = final_result.intersection(set(result_by_director.films))
        if result_by_title:
            final_result = final_result.intersection(set(result_by_title))
        if result_by_year:
            final_result = final_result.intersection(set(result_by_year))

        final_result = list(final_result)
        return {'data': final_result}, 200

        
if __name__ == "__main__":
    app.run(debug=True)
