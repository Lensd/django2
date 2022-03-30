# users = [
#     {'id': '1', 'age': '125', 'status': 'active'},
#     {'id': '2', 'age': '15', 'status': 'active'},
#     {'id': '3', 'age': '11', 'status': 'no'}
# ]
# print([user['age']for user in users])
#
# a = ('1','2','3')
# print(a[1])
#
# a = {x:y for x in range(1,10) for y in range(10,20)}
# print(a)

n1 = {'a': '300', 'b': '400'}
n2 = {'c': '500', 'd': '600'}
n3 = {**n1, **n2}
print(n3)

n1 = {'a': '300', 'b': '400'}
n2 = {'c': '500', 'd': '600'}
x = {}
x.update(n1)
x.update(n2)
print(x)

users = [
    {'id': '1', 'name': 'ruslan', 'active': 'yes'},
    {'id': '2', 'name': 'rus2lan', 'active': False},
    {'id': '3', 'name': 'rusl3an', 'active': True}
]
print([user['id'] for user in users if user['active'] == 'yes'])