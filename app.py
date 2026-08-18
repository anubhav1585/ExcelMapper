from flask import Flask
from flask import render_template
from flask import request

Excel_Mapper_app = Flask(__name__)

@Excel_Mapper_app.route('/', methods=["GET", "POST"])

def Excel_Mapper():

    if request.method == "POST":
        print("Post request received")

        source_file = request.files["source_file"]

        print(source_file)

        source_file.save("Upload/Source/source.xlsx")

        print("source file sucessfully saved!!!!!!!!")
            

        target_file = request.files["target_file"]
        print("target file")

        target_file.save("Upload/Target/Target.xlsx")
        print("Target file files sucessfully saved !!!!!!!!!!")


    return render_template("Excel_mapper.html")



if __name__ == "__main__":
    Excel_Mapper_app.run()
