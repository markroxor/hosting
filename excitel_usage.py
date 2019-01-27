from bs4 import BeautifulSoup

with open('Excitel.htm', 'r') as f:
    html = f.read()

parsed_html = BeautifulSoup(html)

total_usage = 0
for i, a in enumerate(parsed_html.findAll('table')[0].findAll('td')):
    if i % 6 == 4:
        usage = float(a.text.split()[0])
        total_usage += usage

print('Total usage - ' + '%.2f' % (total_usage / 1024) + 'GB')
