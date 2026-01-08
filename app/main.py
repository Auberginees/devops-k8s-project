from flask  import Flask, jsonify, request
import os
import datetime
import logging


app = Flask(__name__)

boot_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

logging.basicConfig(
	filename='/app/logs/access.log',
	level=logging.INFO,
	format='%(asctime)s - %(message)s'
)

@app.before_request
def log_reques_info():
	logging.info(f"Request: {request.path} from {request.remote_addr}")


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
