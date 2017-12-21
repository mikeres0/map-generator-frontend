from flask import Flask, render_template, redirect

app = Flask(__name__)
app.secret_key = "kdadjhdjfjodfuohd72344j23u97egiqbweyayuidouiasfdgo"

@app.route('/')
def index():
    return render_template('index.html')



# API routes

### retrieve api information
@app.route('/api')
def api():
    return ""


if __name__ == "__main__":
    app.run()