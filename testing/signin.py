from requests import put, get


print(put('http://localhost:5000/user1', data={'data': 'Ini adalah user 1'}).json())
print(get('http://localhost:5000/user1').json())
print(put('http://localhost:5000/user2', data={'data': 'Ini adalah user 2'}).json())
print(get('http://localhost:5000/user2').json())
