from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Define the list of featured jobs
featured_jobs = [
    {
        "id": 1,
        "title": "Software Engineer",
        "company": "OpenAI",
        "minExperience": 2,
        "maxExperience": 5,
        "location": "Chennai, TN",
        "workType": "Full-time",
        "minSalary": 11,
        "maxSalary": 17,
        "tags": ["JavaScript", "React", "CSS"],
        "iconUrl": "/assets/openAI.webp",
        "posted": "16-May-2023",
    },
    {
        "id": 2,
        "title": "Backend Developer",
        "company": "OpenAI",
        "minExperience": 3,
        "maxExperience": 6,
        "location": "San Francisco, CA",
        "workType": "Remote",
        "minSalary": 105,
        "maxSalary": 150,
        "tags": ["Node.js", "Express", "MongoDB"],
        "iconUrl": "/assets/openAI.webp",
        "posted": "20-May-2023",
    },
    {
        "id": 3,
        "title": "Graphic Designe Intern",
        "company": "Red String",
        "minExperience": 4,
        "maxExperience": 7,
        "location": "Noida, HR",
        "workType": "Contract",
        "minSalary": 6,
        "maxSalary": 9,
        "tags": ["JavaScript", "React", "Node.js"],
        "iconUrl": "/assets/redString.svg",
        "posted": "21-May-2023",
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "company": "Amazon",
        "minExperience": 2,
        "maxExperience": 5,
        "location": "Pune, MH",
        "workType": "Full-time",
        "minSalary": 10,
        "maxSalary": 25,
        "tags": ["Python", "Machine Learning", "SQL"],
        "iconUrl": "/assets/amazon.webp",
        "posted": "21-May-2023",
    },
]

@app.route('/jobs/featured')
def get_featured_jobs():
    response = make_response(jsonify(featured_jobs))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run()