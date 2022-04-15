from time import sleep
import datetime

res = [{'A': ['78.46.66.203'],
  'CNAME': None,
  'MX': [{'exchange': 'http-s.de', 'priority': 10}],
  'NS': ['ns1.star-dns.de', 'ns2.star-dns.de'],
  'TXT': ['v=spf1 a -all'],
  'country': 'DE',
  'create_date': '2022-04-03T05:57:57.204070',
  'domain': 'http-s.de',
  'isDead': 'False',
  'update_date': '2022-04-03T05:57:57.204073'},

 {'A': ['72.52.4.119'],
  'CNAME': None,
  'MX': [{'exchange': 'localhost', 'priority': 0}],
  'NS': ['ns1.sedoparking.com', 'ns2.sedoparking.com'],
  'TXT': ['v=spf1 ip6:fd92:59f3:510e::/48 -all'],
  'country': 'US',
  'create_date': '2022-04-03T05:57:57.203887',
  'domain': 'http-link.de',
  'isDead': 'False',
  'update_date': '2022-04-03T05:57:57.203890'}]

# for count in res:
#     for i in count:
#       print(i)
#       if i == 'create_date' or i == 'update_date':
#           e = count[i]
#           print(e)
#           try:
#               c = datetime.datetime.strptime(count[i], "%Y-%m-%dT%H:%M:%S")
#               print(c)
#           except:
              
#             print('dadwad')
#       else:
#           continue

a = res[0]
b = a['create_date']
q = b.split('.')
b = datetime.datetime.strptime(q[0], "%Y-%m-%dT%H:%M:%S")
print(b)