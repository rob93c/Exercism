def tally(tournament_results):
    teams = {}
    for line in tournament_results.split('\n'):
        if not line:
            break
        t1, t2, issue = line.split(';')
        if t1 not in teams:
            teams[t1] = {'mp': 0, 'w': 0, 'd': 0, 'l': 0}
        if t2 not in teams:
            teams[t2] = {'mp': 0, 'w': 0, 'd': 0, 'l': 0}

        if issue == 'win':
            teams[t1]['w'] += 1
            teams[t2]['l'] += 1
        elif issue == 'loss':
            teams[t1]['l'] += 1
            teams[t2]['w'] += 1
        elif issue == 'draw':
            teams[t1]['d'] += 1
            teams[t2]['d'] += 1

        teams[t1]['mp'] += 1
        teams[t2]['mp'] += 1
    teams_l = []
    for name, res in teams.items():
        res['p'] = 3 * res['w'] + res['d']
        res['name'] = name
        teams_l.append(res)

    teams_l.sort(key=lambda x: x['name'])  # alphabeticaly
    teams_l.sort(key=lambda x: -x['p'])  # based on points
    results = ['Team                           | MP |  W |  D |  L |  P']
    results.extend(
        '{name:30} | {mp:2} | {w:2} | {d:2} | {l:2} | {p:2}'.format(**team)
        for team in teams_l
    )
    return '\n'.join(results)
