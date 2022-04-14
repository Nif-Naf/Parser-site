from time import sleep


meal = [{'A': ['78.46.66.203'],
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

# result = [
#     url = None,
#     domains = None,
#     create_data = None,
#     update_data = None,
#     country = None,
#     is_dead = None,
#     a = None,
#     ns = None,
#     cname = None,
#     mx = None,
#     txt = None
# ]

for count in meal:
    print()
    print()
    for i in count:  
        res = count[i]
        print()
        print(res)

                # result = {'A': ['78.46.66.203'],
                #         'CNAME': None,
                #         'MX': [{'exchange': 'http-s.de', 'priority': 10}],
                #         'NS': ['ns1.star-dns.de', 'ns2.star-dns.de'],
                #         'TXT': ['v=spf1 a -all'],
                #         'country': 'DE',
                #         'create_date': '2022-04-03T05:57:57.204070',
                #         'domain': 'http-s.de',
                #         'isDead': 'False',
                #         'update_date': '2022-04-03T05:57:57.204073'}

                # #Сохраняем данные в бд
                # js_res = result.json.loads()

                # for count in meals: #Выбрали словарь в списке.

                #     for i in count: #Проходимся по словарю
                #         res = count[i]
                #         meal_data = Result(
                #             url = i['domain'], 
                #             domains = i['domain'],
                #             create_data = i['create_date'],
                #             update_data = i['update_date'],
                #             country = i['country'],
                #             is_dead = i['isDead'],
                #             a = i['A'],
                #             ns = i['NS'],
                #             cname = i['CNAME'],
                #             mx = i['MX'],
                #             txt = i['TXT']
                #         )
                        # meal_data.save()

                # for i in meals: #Выбрали словарь в списке.

                #         meal_data = Result(
                #             url = i['domain'], 
                #             domains = i['domain'],
                #             create_data = i['create_date'],
                #             update_data = i['update_date'],
                #             country = i['country'],
                #             is_dead = i['isDead'],
                #             a = i['A'],
                #             ns = i['NS'],
                #             cname = i['CNAME'],
                #             mx = i['MX'],
                #             txt = i['TXT']
                #         )
                #         meal_data.save()


                # json_form = Js_form(result)

                # if json_form.is_valid():
                #     json_form.save()
                #     result = 'True'

                # else:
                #     result = 'False'

                    # sdb = Result(
                    #     url = '', 
                    #     domains = 'domain',
                    #     create_data = 'create_date',
                    #     update_data = 'update_date',
                    #     country = 'country',
                    #     is_dead = 'is_Dead',
                    #     a = 'A',
                    #     ns = 'NS',
                    #     cname = 'CNAME',
                    #     mx = 'MX',
                    #     txt = 'TXT'
                    # )

                    # sdb.save()
