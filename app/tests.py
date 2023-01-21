from django.test import TestCase

# Create your tests here.
print('0')
# url='https://dog.ceo/api/breeds/image/random'
url = 'https://random.dog/doggos/image/random'

print('1')

get_result = requests.get(url).json()
result = [get_result]
print(result)

print('2')