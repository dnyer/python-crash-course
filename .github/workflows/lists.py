motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0]="ducati"
print(motorcycles)
del motorcycles[0]
print(motorcycles)
print(motorcycles[0])
popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

actors = ['brad','angelina','tom','steven','geordi']
print(actors)
print(sorted(actors))
actors.reverse()
print(actors)
print(len(actors))

squares=[value**2 for value in range(1,11)]
print(squares)

letters=['a','b','c','d','e','f','g','h']
print(letters[2:5])
print(letters[:3])
print(letters[-3:])
favorite_letters=letters[:]
del favorite_letters[0::2]
print(favorite_letters)
