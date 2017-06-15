from flask import Flask, send_from_directory

app = Flask(__name__)

# send everything from client as static content
@app.route('/Storage/<fname>')
def storage_server():
	return send_from_directory(app.root_path, "Storage/"+fname)

if __name__ == '__main__':
	app.run()
