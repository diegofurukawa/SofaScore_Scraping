import requests
import pandas as pd

# Variaveis Globais
game_id = 12778135

url = f'https://www.sofascore.com/api/v1/event/{game_id}/statistics'

var_excel_nome = str(game_id) + '_statisticas.xlsx'

print(url)

# you'll be blocked if you don't use some type of user agent
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0'
    }

response =  requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    all_data = []

    for match_stat in data['statistics']:
        period = match_stat['period']

        for group in match_stat['groups']:
            group_name = group['groupName']

            for item in group['statisticsItems']:
                stat_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')


                all_data.append({
                    'GameId': game_id,
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stat_name,
                    'Home': home_value,
                    'Away': away_value
                })


df = pd.DataFrame(all_data)

excel_file = var_excel_nome
df.to_excel(excel_file, index=False)