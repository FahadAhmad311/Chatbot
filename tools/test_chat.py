import requests

BASE = 'http://127.0.0.1:8000/api'

# Login
resp = requests.post(f'{BASE}/login/', json={'username':'testuser','password':'TestPass123'})
print('LOGIN', resp.status_code)
print(resp.text)
if resp.status_code != 200:
    raise SystemExit('login failed')

token = resp.json()['token']
print('TOKEN', token)

headers = {'Authorization': f'Token {token}', 'Content-Type': 'application/json'}
# Chat
r = requests.post(f'{BASE}/chat/', json={'query':'Hello from test script'}, headers=headers)
print('CHAT', r.status_code)
print(r.text)
