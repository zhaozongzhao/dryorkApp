import requests

url = 'https://www.ketangpai.com/SummaryApi/attence'
params= {'courseid':'MDAwMDAwMDAwMLOGvd6H36-w'}
cookie= {'ketangpai_home_remember':'think%3A%7B%22username%22%3A%22MDAwMDAwMDAwMLOGy96Gqatphc6KlbLPn54%22%'
                                   '2C%22expire%22%3A%22MDAwMDAwMDAwMLOGud2GqclrhM563LKmdZ4%22%2C%22token%22%3A%22MDAwM'
                                   'DAwMDAwMMurrpWavLehhs1-3LHfkdqFp52VepuomcWmmqaMiHtnr5ylzYWosKKZq6HQxtOK0ZCme5p-q6'
                                   'iZu2yrn4uNhJ3KedDYk7ivboS4it2xqZuUg8133H96YW0%22%7D'}
r = requests.get(url,params=params,cookies=cookie)
result = r.json()
print(result['data'])


