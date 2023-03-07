import datetime

from requests import get, post, delete, put

# print(get('http://localhost:5000/api/jobs').json())
# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/999').json())
# print(get('http://localhost:5000/api/jobs/a').json())

# print(post('http://localhost:5000/api/jobs',
#            json={'team_leader': 3, 'job': 'aaaaaaaa', 'work_size': 2, 'is_finished': False,
#                  'start_date': str(datetime.datetime.now()), 'id': 10}).json())
# print(post('http://localhost:5000/api/news', json={
#     'title': 'Заголовок3',
#     'content': 'Текст новости3',
#     'user_id': 3,
#     'is_private': False,
#     'is_published': True}).json())
# print(delete('http://localhost:5000/api/news/999').json()) # новости с id = 999 нет в базе
# print(delete('http://localhost:5000/api/news/10').json())
# print(delete('http://localhost:5000/api/jobs/3').json())
# print(delete('http://localhost:5000/api/jobs/999').json())

# wrong id
print(put('http://localhost:5000/api/jobs/90', json={'team_leader': 2}).json())
# correct
print(put('http://localhost:5000/api/jobs/1', json={'work_size': 2}).json())
# wrong json
print(put('http://localhost:5000/api/jobs/1', json={'aaa': 2}).json())
# without json
print(put('http://localhost:5000/api/jobs/1').json())

