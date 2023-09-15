import sqlalchemy
from sqlalchemy import create_engine, text


# once you have a db, this is the way to create the engine (pip install pymysql)
engine = create_engine(
    "mysql+pymysql://user:pass@host/dbname?charset=utf8mb4",
    connect_args={
        'ssl': {
            'ssl_ca': "value/from/the/db/provider",
            'ssl_cert': "if/needed",
            'ssl_key': "if/needed"

        }
    }
)


def load_jobs_from_db():
   with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
      # print(result.all())

      jobs = []
      for row in result.all():
        jobs.append(dict(row))
      return jobs



def load_job_from_db(id):
   with engine.connect() as conn:
      result = conn.execute(text(
         "SELECT * FROM jobs WHERE id = :val",
         val=id
      ))
      rows = result.all()
      if len(rows) == 0:
         return None
      else:
         return dict(rows[0])
      

def save_application_to_db(job_id, application):
   with engine.connect() as conn:
      query = text(
         'INSERT INTO applications (job_id, full_name, email, linkedin_url, education, experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :experience, :resume_url)'
      )
      conn.execute(query, 
                   job_id=job_id, 
                   full_name=application['full_name'], 
                   email=application['email'], 
                   linkedin_url=application['linkedin_url'], 
                   education=application['education'], 
                   experience=application['experience'], 
                   resume_url=application['resume_url'])
   