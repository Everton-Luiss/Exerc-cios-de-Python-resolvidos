times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')