from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, save_application_to_db

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': '$150,000'
  }
]


@app.route("/")
def hello_jovian():
    jobs = load_jobs_from_db()
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


@app.route('/job/<id>')
def show_job(id):
   job = load_job_from_db(id)
   if not job:
      return "not found", 404
   
   return render_template('jobPage.html', job=job)


@app.route('/job/<id>/apply', methods=['post'])
def application(id):
   data = request.form
   job = load_job_from_db(id)
   save_application_to_db(id, data)
   return render_template('application_submitted.html', application=data, job=job)
   

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)