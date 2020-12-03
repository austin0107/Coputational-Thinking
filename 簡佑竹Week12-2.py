season = "1995-1996"
team = "Chicago Bulls"
coach = "Phil Jackson"
records = [72, 10]
starting = ["Ron Harper", "Michael Jordan", "Scottie Pippen", "Dennis Rodman", "Luc Longley"]
champion = True

best_NBA = list((season, team, coach, records, starting, champion)) #要有兩個小括號
print(best_NBA)
['1995-1996', 'Chicago Bulls', 'Phil Jackson', [72, 10], ['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman', 'Luc Longley'], True]

print(type(best_NBA))
<class 'list'>

print(best_NBA[-2])
['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman', 'Luc Longley']

print(best_NBA[4])
['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman', 'Luc Longley']

print(best_NBA[0:3])
['1995-1996', 'Chicago Bulls', 'Phil Jackson']


best_NBA[2] = "Tommas Jian" 
print(best_NBA)
['1995-1996', 'Chicago Bulls', 'Tommas Jian', [72, 10], ['Ron Harper', 'Michael Jordan', 'Scottie Pippen', 'Dennis Rodman', 'Luc Longley'], True]