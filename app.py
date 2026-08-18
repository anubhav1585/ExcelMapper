from   flask import Flask
from flask import render_template

Excel_Mapper_app = Flask(__name__)

@Excel_Mapper_app.route('/')

def Excel_Mapper():
    return render_template("Excel_mapper.html")



if __name__ == "__main__":
    Excel_Mapper_app.run(debug=True)
    