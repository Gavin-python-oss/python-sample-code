""""
a = "python is a useful language!"
print(a.title())
b = 'China is a powerful country'
print(b.upper())
c = 'Shang Hai Is a Beautiful City!'
print(c.lower())
charter = a + " " + b
print(charter)
first_name = 'James'
last_name = 'Daogelasi'
full_name = first_name + ' ' + last_name
print("Hello," + full_name + " !")

age = 25
message = 'Hello ' + str(age) + 'rd birthday!'
print(message)

a = 16
b = 2
c = 6
d = 8
e = 4.0
print( b + c)
print(a - d)
print(int(a/b))
print(b * int(e))

lucky_number = 24
article = 'my favourite number is ' + str(lucky_number) + ' !'
print(article)
"""

"""
print(bicycle[0])
bicycle[0] = 'ship'
print(bicycle[0])
print(bicycle)
bicycle.append('motor')
print(bicycle)
bicycle.insert(2, 'taxi')
print(bicycle)
"""
"""
bicycle = ['car', 'bick', 'board']
# message = 'My favourite means of transportation  is ' + bicycle[0] + ' !'
for car in bicycle:
    if car == 'car':
        print(car.upper())
    else:
        print(car.title())
        
        
"""
"""
request_pizza = 'Hamburger'
if request_pizza == 'A':
    print('please give me a cup of beers')
else:
    print("Thanks,I'like a dumplings")
"""
"""
banned_users = ['Audio', 'telephone', 'sound']
user = 'smell'
if user not in banned_users:
    print(user.upper() + ', can you change your name?')
print('please change your banned')

"""
"""
requested_toppings = ['A']
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Add" + requested_topping + "!")
    print(requested_toppings)  # 如果列表不为空则会将列表的内容加到列表里并进行输出
    print('\nFinish making yur pizza!')
else:
    print('Are you sure you want a plain pizza?')
"""
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) # 在打印输出的时候显示的是字典的元素，即列表信息
print(alien_0['points'])
alien_1 = {'color': 'blown', 'point' : 12 }
print(alien_1['color'])
new_point = alien_1['point']
print('You just earn ' + str(new_point) + ' points !')
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_1 )
alien_2 = { }  # 此处的意思为在该行创建一个新字典，然后根据需要填充字典
alien_2['color'] = 'blue'
alien_2['point'] = 15
print(alien_2)
alien_2['color'] = 'red'
print('now the alien_2 color is ' + alien_2['color'] + ' !')

"""
"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'slow'}
#print(alien_0)
alien_0['speed'] = 'fast'
print("original x_position:" + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print('now the alien_0 x_position is ' + str(alien_0['x_position']) + ' !')
del alien_0['y_position']
print(alien_0)

tortoise_0 = {'x_position': 2, 'y_position': 16, 'speed': 'slow'}
rabbit_0 = {'x_position': 3, 'y_position': 12, 'speed': 'fast'}
if tortoise_0['x_position'] < rabbit_0['x_position']:
    tortoise_0['x_position'] = tortoise_0['x_position'] + 1
    print('now the tortoise_0 x_position is ' + str(tortoise_0['x_position']))
if tortoise_0['y_position'] < rabbit_0['y_position']:
    print('That is what makes sense !')
if tortoise_0['speed'] > rabbit_0['speed']:
    print('Are you kidding me!')
"""

"""
favorite_language = {
    'surge': 'python',
    'carson': 'c',
    'david': 'jave',
    }
#if 'sam' not in favorite_language.keys():
    #print('sam, please enter the poll! ')
#friend = ['surge', 'david']
#for name in favorite_language.keys():
   # print(name.title())
    #if name in friend:
       # print('Hi ' + name.title() + ' , I saw your favorite_language is ' +
              #favorite_language[name].title() + ' !')

for name in favorite_language.keys():
    print(name.title())
for language in favorite_language.values():
    print(language.title())
for name, language in favorite_language .items():
    print(name.upper() + " 's favorite language is " + language.lower())

"""

"""
favorite_languages = {
    'surge': 'python',
    'carson': 'c',
    'david': 'java',
    'sam': 'java',
    }
#for name in sorted( favorite_language.keys()):
    #print(name.title() + ', thanks you for taking the poll!')
print('The following language were mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
"""
"""
alien_0 = {'color': 'red', 'size': 'small'}
alien_1 = {'color': 'green', 'size': 'medium'}
alien_2 = {'color':'blown', 'size': 'large'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
"""
"""
aliens =[]
#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'red', 'point' : 6}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")
#显示创建了多少个外星人
print("Total number of aliens is :" + str(len(aliens)))
"""


peoples = []
#创建50个人并显示人的特征
for people_number in range(50):
    new_people = {'age': 15, 'color': 'yellow', 'speed': 'medium'}
    peoples.append(new_people)
#对50个人进行切片，并更改特征
for people in peoples[:2]:
    if people['age'] == 15:
        people['age'] = 25
        people['color'] = 'white'
        people['speed'] = 'fast'
    #print(people)如果这句加上的话在此处切片的信息就会打印一次
for people in peoples[:5]:
    print(people)
#取出所有的人中的前五个元素
print("...")
print("Total number of people is :" + str(len(peoples)))