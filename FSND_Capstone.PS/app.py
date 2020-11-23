from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from auth import requires_auth, AuthError
from models import setup_db, db_drop_and_create_all, Skaters, Goalies

def create_app(test_config=True):
    app = Flask(__name__)
    setup_db(app)

    #CORS configuration
    CORS(app, resources={r"/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true'
        )
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PATCH,POST,DELETE,OPTIONS'
        )
        return response

    #uncomment below on initial run to setup the required tables in database
    #db_drop_and_create_all()

    @app.route('/')
    def greeting():
        return jsonify({
            'success': True,
            'FSND Capstone project': 'a simple NHL season stats recorder.'
            }), 200

    @app.route('/login-results')
    def login_results():
        return jsonify({
            'success': True,
            'You have made it in successfully.': 'Check the address bar for your JWT for testing.'
            }), 200


    """
    The following are the only routes available to the fans:
    Viewing the skaters and the goalies, but not detailed stats
    """

    @app.route('/skaters')
    @requires_auth("get:skaters")
    def get_skaters(payload):
        try:
            skaters = Skaters.query.order_by(Skaters.id).all()
            sks = []
            for skater in skaters:
                sks.append(skater.short())

        except:
            abort(422)

        return jsonify({
            'success': True,
            'skaters': sks
            }), 200


    @app.route('/goalies')
    @requires_auth("get:goalies")
    def get_goalies(payload):
        try:
            goalies = Goalies.query.order_by(Goalies.id).all()
            gs = []
            for goalie in goalies:
                gs.append(goalie.short())

        except:
            abort(422)

        return jsonify({
            'success': True,
            'gs': gs
            }), 200
           
#All other routes require GM auth to get/patch/delete stats

    @app.route('/skaters/<int:id>')
    @requires_auth("get:skaters-info")
    def get_skaters_by_id(payload, id):
        try:
            skater = Skaters.query.get(id)
            skate = skater.long()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'skater': skate
            }), 200

    @app.route('/skaters', methods=['POST'])
    @requires_auth("post:skater")
    def create_skater(payload):
        try:
            body = request.get_json()
            if 'name' and 'pos' not in body:
                abort(422)

            name = body['name']
            pos = body['pos']
            pts = body['pts']
            gls = body['gls']

            new_Skater = Skaters(name=name, pos=pos, pts=pts, gls=gls)
            new_Skater.insert()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'new_Skater': [new_Skater.long()]
            }), 200

    @app.route('/skaters/<int:id>', methods=['PATCH'])
    @requires_auth('patch:skater')
    def edit_skater(payload, id):
        fix_skater = Skaters.query.get(id)

        if fix_skater is None:
            abort(422)

        try:
            body = request.get_json()
    
            new_name = body['name']
            new_pos = body['pos']
            new_pts = body['pts']
            new_gls = body['gls']

            if new_name:
                fix_skater.name = new_name
            if new_pos:
                fix_skater.pos = new_pos
            if new_pts:
                fix_skater.pts = new_pts
            if new_gls:
                fix_skater.gls = new_gls

            fix_skater.update()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'edited_skater': [fix_skater.long()]
            }), 200    

    @app.route('/skaters/<int:id>', methods=['DELETE'])
    @requires_auth('delete:skater')
    def delete_skater(payload, id):
        skater = Skaters.query.get_or_404(id)

        try:
            skater.delete()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'Deleted': skater.id
            }), 200

    @app.route('/goalies/<int:id>')
    @requires_auth("get:goalies-info")
    def get_goalies_by_id(payload, id):
        try:
            goalie = Goalies.query.get(id)
            goal = goalie.long()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'goalie': goal
            }), 200

    @app.route('/goalies', methods=['POST'])
    @requires_auth("post:goalies")
    def create_goalie(payload):
        try:
            body = request.get_json()

            name = body['name']
            gaa = body['gaa']
            so = body['so']
            w = body['w']

            new_Goalie = Goalies(name=name, gaa=gaa, so=so, w=w)
            new_Goalie.insert()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'new_Goalie': [new_Goalie.long()]
            }), 200

    @app.route('/goalies/<int:id>', methods=['PATCH'])
    @requires_auth('patch:goalie')
    def edit_goalie(payload, id):
        fix_goalie = Goalies.query.get(id)
        if fix_goalie is None:
            abort(422)

        try:
            body = request.get_json()
    
            new_name = body['name']
            new_gaa = body['gaa']
            new_so = body['so']
            new_w = body['w']

            if new_name:
                fix_goalie.name = new_name
            if new_gaa:
                fix_goalie.gaa = new_gaa
            if new_so:
                fix_goalie.so = new_so
            if new_w:
                fix_goalie.w = new_w

            fix_goalie.update()

        except:
            abort(422)

        return jsonify({
            'success': True,
            'fix_goalie': fix_goalie.long()
            }), 200

    @app.route('/goalies/<int:id>', methods=['DELETE'])
    @requires_auth("delete:goalie")
    def delete_goalie(payload, id):
        goalie = Goalies.query.get_or_404(id)

        try:
            goalie.delete()
            
        except:
            abort(422)

        return jsonify({
            'success': True,
            'Deleted': goalie.id
            }), 200
        

## Error Handling

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'Forbidden'
            }), 403
   
    @app.errorhandler(401)
    def not_authorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'Authentication error'
            }), 401

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False, 
            'error': 422,
            'message': 'unprocessable'
            }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            'success': False, 
            'error': 404,
            'message': 'resource not found'
            }), 404

    @app.errorhandler(500)
    def internalservererror(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'Internal Service Error'
            }), 500

    @app.errorhandler(AuthError)
    def AuthError_issue(error):
        return jsonify({
            'success': False, 
            'error': error.status_code,
            'message': error.error['description']
            }), error.status_code


    return app

app = create_app()

if __name__ == '__main__':
    app.run()
