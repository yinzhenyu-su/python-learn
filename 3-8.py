place = ['长城', '金字塔', '迪拜塔', '西湖', '非洲']

print('\nHere is sorted list:', sorted(place, key=len))
print('Here is original list:', place)
place.sort()
print('\nHere is sort list', place)
print('\nHere is original list again:', place)
