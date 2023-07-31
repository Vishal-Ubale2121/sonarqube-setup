from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    print('Server is Running......')
    return render_template('index.html')


# Start the server 127.0.0.1:9500
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9500, debug=True)