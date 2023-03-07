import flask
from flask import request, jsonify

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint('news_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {'jobs': [item.to_dict(only=('id', 'team_leader', 'job',
                                     'work_size', 'collaborators',
                                     'start_date', 'end_date', 'is_finished')) for item in jobs]})


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({'job': job.to_dict(only=('id', 'team_leader', 'job',
                                             'work_size', 'collaborators',
                                             'start_date', 'end_date', 'is_finished'))})


@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job',
                  'work_size', 'is_finished']) \
            or any(key not in ['id', 'team_leader', 'job',
                               'work_size', 'collaborators',
                               'start_date', 'end_date', 'is_finished'] for key in request.json):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if list(db_sess.query(Jobs).filter(Jobs.id == request.json.get('id'))):
        return jsonify({'error': 'Id already exists'})
    job = Jobs(**request.json)
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def change_job_id(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif any(key not in ['id', 'team_leader', 'job',
                               'work_size', 'collaborators',
                               'start_date', 'end_date', 'is_finished'] for key in request.json):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Wrong id'})
    job.id = request.json.get('id', job.id)
    job.team_leader = request.json.get('team_leader', job.team_leader)
    job.job = request.json.get('job', job.job)
    job.work_size = request.json.get('work_size', job.work_size)
    job.collaborators = request.json.get('collaborators', job.collaborators)
    job.start_date = request.json.get('start_date', job.start_date)
    job.end_date = request.json.get('end_date', job.end_date)
    job.is_finished = request.json.get('is_finished', job.is_finished)
    db_sess.commit()
    return jsonify({'success': 'OK'})

