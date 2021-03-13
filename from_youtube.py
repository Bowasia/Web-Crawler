# coding=utf-8
from pyquery import PyQuery as pq
from datetime import timedelta, date
import json

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2018, 2, 1)
end_date = date(2018, 2, 10)

res = {}

for day in daterange(start_date, end_date):
    d = day.strftime("%Y-%m-%d")
    page = pq(url="http://www.goal.com/en/results/"+d)
    res[d] = {}
    print( d )

    for comp in page('.competition-matches'):
        comp = pq( comp )

        comp_name = pq(comp('.competition-name')[0]).text()
        res[d][comp_name] = []

        for match_row in comp('.match-row'):
            match_res = {}
            match_row = pq(match_row)
            m_name = match_row('[itemprop="name"]').attr('content')

            home = pq(match_row('.team-home'))
            away = pq(match_row('.team-away'))

            h_goals=int(home('.goals').text())
            a_goals=int(away('.goals').text())

            h_name=home('.team-name').text()
            a_name=away('.team-name').text()

            winner = "none"
            if( h_goals > a_goals ):
                winner = h_name
            elif ( a_goals > h_goals ):
                winner = a_name

            match_res[h_name] = h_goals
            match_res[a_name] = a_goals
            match_res['winner'] = winner
            match_res['name'] = m_name
            res[d][comp_name].append( match_res )

data_file = open('data.json', 'w', encoding="utf8")
data_file.write( json.dumps( res ) )
data_file.close()
