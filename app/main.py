from flask  import Flask, jsonify
import os
import datetime

app = Flask(__name__)

boot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route('/')
def hello():
	return "Hello! Infastructure Health Check API is running."


@app.route('/health')
def health_check():
	return jsonify({"status": "OK"}), 200


@app.route('/ready')
def ready():
	return jsonify({"status": "ready"}), 200

@app.route('/version')
def get_version():
	version = os.getenv('APP_VERSION', 'unknown')
	return jsonify({"version": version})


@app.route('/env')
def env():
	environment = os.getenv('APP_ENV', 'development')
	return jsonify({"environment": environment, "start_time": boot_time})


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
