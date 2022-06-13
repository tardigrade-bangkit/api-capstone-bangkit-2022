from flaskr.__init__ import app
from flask import jsonify

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"msg" : error}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')