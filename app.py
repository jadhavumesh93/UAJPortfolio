from flask import Flask, jsonify, render_template, request
from requests import Request, Response
from Utility import PortUtility

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('home.html', title="Welcome Page")

@app.route("/projectdesc", methods=['POST'])
def projectdesc():
    data = request.get_json()
    project_id = data.get("project_id", 1)
    port_util = PortUtility.PortUtility()
    video_url, tech_stack, project_url, desc = port_util.project_desc(project_id)
    result = {
        "video_url" : video_url,
        "tech_stack" : tech_stack,
        "project_url" : project_url,
        "desc" : desc
    }
    
    return jsonify(result)

if(__name__ == "__main__"):
    app.run(debug=True)