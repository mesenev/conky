from urllib import request

with request.urlopen('http://wttr.in/vladivostok?n2AQT&lang=en') as response:
    html = response.read()
answer = html.decode('utf-8').split('\n')
answer = answer[9:12] + answer[19:22]
# print(*answer, sep='\n')
answer = list(map(lambda x: '  ' + x[16:30] + ' ' + x[46:61], answer))
answer = ['Tomorrow:'] + answer[:3] + ['Day after:'] + answer[3:]
print(*answer, sep='\n')
