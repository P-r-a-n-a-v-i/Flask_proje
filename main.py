from flask import Flask, jsonify,request


app = Flask(__name__)

internship = [
  {"ID" :"22D", "company":"TATA", "Title": "Python Developer Intern","location": "Remote"},
  {"ID" :"23A", "company":"JP_Morgan", "Title": "Full Stack Developer Intern","location": "Virtual"},
  {"ID" :"14E", "company":"Turing", "Title": "Backend developer Intern","location": "At Work Place"},
  {"ID" :"87K", "company":"Zerodha", "Title": "Data Analyst Intern","location": "Remote"},
  {"ID" :"P00", "company":"Angel_List", "Title": "Data Analyst Intern","location": "At Work Place"},
]


@app.route("/internship", methods = ["GET"]) 
def get_internship():
  # return jsonify({"internship": internship})

  company = request.args.get("company")
  Title = request.args.get("Title")
  location = request.args.get("location")

  filter_internship = internship

  if company:
    filter_internship = [i for i in filter_internship if i["company"].lower() == company.lower()]

  if Title:
    filter_internship = [i for i in filter_internship if i["Title"].lower() == title.lower()]

  if location:
    filter_internship = [i for i in filter_internship if i["location"].lower() == location.lower()]

  return jsonify({"internship": filter_internship})    


if __name__ == "__main__":
  app.run(debug=True)


