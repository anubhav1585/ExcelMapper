from   flask import Flask
from flask import render_template
from flask import request

Excel_Mapper_app = Flask(__name__)

@Excel_Mapper_app.route('/',methods=["GET", "POST"])

def Excel_Mapper():
    if request.method == "POST":
        print("Post request received")
    return render_template("Excel_mapper.html")



if __name__ == "__main__":
    Excel_Mapper_app.run(debug=True)
