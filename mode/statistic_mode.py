from statistics import mode, multimode

points_per_game = [3, 15, 23, 42, 30, 10, 10, 12]
sponsorship = ['nike', 'adidas', 'nike', 'jordan',
               'jordan', 'rebook', 'under-armour', 'adidas']


print(mode(points_per_game))
print(mode(sponsorship))

print(multimode(points_per_game))
print(multimode(sponsorship))