games={'Badminton':'Indoor','Table Tennis':'Indoor','Pool':'Indoor','Football':'Outdoor','Hockey':'Outdoor','Ice Hockey':'Indoor','Cricket':'Outdoor','Squash':'Indoor','Lawn Tennis':'Outdoor','Baseball':'Outdoor'}

Indoor_games={}
Outdoor_games={}
for k,v in games.items():
    if v=='Indoor':
        Indoor_games[k]=v

for k,v in games.items():
    if v=='Outdoor':
        Outdoor_games[k]=v

print(Indoor_games)
print(Outdoor_games)                