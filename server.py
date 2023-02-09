from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def level_one():
    return render_template("index.html")

@app.route('/play/<int:x>')
def level_two(x):
    return render_template("index_lvl2.html", num=x)

@app.route('/play/<int:x>/<string:color>')
def level_three(x, color):
    return render_template("index_lvl3.html", num=x, color=color)
    
if __name__=="__main__":
    app.run(debug=True, port = 5500)