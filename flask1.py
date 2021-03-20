

from flask import Flask, render_template

app = Flask(__name__)



# routes
@app.route("/")
def index():
    return render_template('index.html')



def main():
    """Run the app."""
    app.run(host='localhost', port=8000)  # nosec


if __name__ == '__main__':
    main()