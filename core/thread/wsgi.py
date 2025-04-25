#
# Author: Rohtash Lakra
#


#
# Author: Rohtash Lakra
#

import os

from flask import Flask, make_response, jsonify

from sqs import SQSTask

app = Flask(__name__)
SQSTask(app)


# Health probe endpoint
@app.route('/health-check')
def health_check():
    return make_response(jsonify({'message': 'ok'}), 200)


def runApp():
    debug = bool(os.getenv('APP_DEBUG', True))
    host = os.getenv('APP_HOST', '0.0.0.0')
    port = int(os.getenv('APP_PORT', 8080))
    app.run(debug=debug, host=host, port=port)


if __name__ == '__main__':
    runApp()

# Test: http://127.0.0.1:8080/health-check
