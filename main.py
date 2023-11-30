from flask import Flask

website = Flask(__name__)

@website.route("/")
def hello():
  return ("Heng")

if __name__ == "__main__":
  website.run(host="0.0.0.0", debug = True)