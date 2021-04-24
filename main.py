from flask import Flask, session
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    # app.run()


if __name__ == '__main__':
    main()


job = Jobs()
job.team_leader = 1
job.job = "deployment of residential modules 1 and 2"
job.work_size = 15
job.collaborators = '2, 3'
job.start_date = '(now)'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()