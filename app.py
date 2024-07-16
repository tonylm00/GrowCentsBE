from flask import jsonify
from app import create_app

app = create_app()


@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": f"Not found **{error}"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": f"Internal server error **{error}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
