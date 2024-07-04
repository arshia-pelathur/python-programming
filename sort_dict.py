dune = {'paul atreides':'timothee chalamet',
        'chani':'zendaya',
        'duncan idaho':'jason momoa',
        'jamis':'babs',
        'stilgar':'javier bardem',
        'lady jessica':'rebecca ferguson'}

sorted = {character:dune[character] for character in sorted(dune.keys())}

print(sorted)
