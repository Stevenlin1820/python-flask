from flask import Flask
from flask import render_template, request
import xlrd
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/myname")
def jaySayHi():
    return render_template("myname.html", chineseName="林嵩憲", englishName="Steven")


@app.route("/agetest")
def agetest():
    age = 0
    try:
        age = int(request.args.get("age"))
    except Exception as e:
        print(e)
    return render_template("age.html", age=age)


@app.route("/store")
def store():
    cart = {"可樂": 12, "檸檬紅茶": 34, "咖啡": 101}
    return render_template("store.html", cart=cart)


@app.route("/ntu")
def ntu():
    return render_template("ntu.html")

  
@app.route("/ntu/<departmentCode>")
def department(departmentCode):
    workbook = xlrd.open_workbook_xls("dpt_code.xls")
    worksheet = workbook[0]
    info = f"{departmentCode} 沒有這個科系"
    for row, code in enumerate(worksheet.col(1)):
        if (code.value == departmentCode):
            info = f"{departmentCode}－{worksheet.cell_value(row , 2)} {worksheet.cell_value(row , 6)}"
    return render_template("department.html", info=info)


if __name__ == "__main__":
    app.run(debug=True)
