from flask import Flask, render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
def hello():
  return render_template('index.html')
print(__name__)
if __name__ =="__main__":
  app.run(host="0.0.0.0",debug='true')
  