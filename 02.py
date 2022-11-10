from collections import namedtuple
import os
import array
symbols = "ÄÄ123213"

codes = [ord(symbol) for symbol in symbols]

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]


print(codes)
print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii)

# 데카르트 곱 1차원 곱 -> 2차원
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print(tshirts)

# 제너레이터 표현식
# 다른 생성자에 전달할 리스트를 통쨰로 만들지 않고 이터레이터 프로토콜을 이용해서 항목을 하나씩 생성하는 제너레이터 표현식은 메모리를 더 적게 사용한다.
# 제너레이터 표현식은 지능현 리스트와 동일한 구문을 사용하지만 대괄호 대신 괄호를 사용한다.
tuple(ord(symbol) for symbol in symbols)
print(array.array('I', (ord(symbol) for symbol in symbols)))

# 2.3
# 튜플은 단순한 불변 리스트가 아니다.
# 튜플은 불변 리스트로 사용할 수도 있지만 필드명이 없는 레코드로 사용할 수도 있다.

lax_coodinates = (33.9425, -118.408056)
# 튜플 언패킹 (iterable unpacking)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)

# 병렬할당 (parallel assignment)
lax_coodinates = (33.9425, -118.408056)
latitude, longtitude = lax_coodinates  # 튜플 언패킹
print(latitude)
print(longtitude)

# 값의 교환
a = 'a'
b = 'b'
b, a = a, b
print(a, b)

# *을 이용한 언패킹
print(*(1, 2))

# 파일 시스템경로에서 경로명과 파일명 가져오기
_, filename = os.path.split('/home/aaa/bbb')
print(filename)

# 전통적으로 _는 gettext.gettext()함수의 대한 별명으로 사용된다. 그 외의 경우에는 _를 플레이스홀더로 사용하는 것이 좋다.

# 초과 항목을 잡기 위해 * 사용하기
# js의 spread syntax랑 비슷한거 같음
a, b, *rest = range(5)
print(a, b, rest)

a, *body, c, d = range(5)
print(a, body, c, d)

# 내포된 튜플 언패킹
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Tokyo', 'JP', 20.142, (19.433333, -99.133333)),
    ('Tokyo', 'JP', 20.104, (40.808611, -74.020386)),
    ('Tokyo', 'JP', 19.649, (-23.547778, -46.635833)),  # trailing comma를 지원하는군
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
# 마지막 필드를 튜플에 할당하면서 언패킹 - js의 구조분해할당 비슷함 (destructuring assignment)
for name, cc, pop, (latitude, longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))


# namedtuple
# 튜플은 레코드로 사용하기에 부족한 점이 있다. 때로는 필드에 이름을 붙일 필요가 있다.
# 필드명이 클래스에 저장되브로 namedtuple()로 생성한 객체는 튜플과 동일한 크기의 메모리만 사용한다.
# 속성을 객체마다 존재하는 __dict__에 저장하지 않으므로 일반적인 객체보다 메모리를 적게 사용한다.


City = namedtuple('City', 'name country population coodinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139, 691667))
print(tokyo)

print(tokyo.population)

print(tokyo.coodinates)

print(tokyo[1])

# namedtuple은 튜플에서 상속받은 속성 외 몇 가지 속성을 더 가지고 있다.

print(City._fields)

LatLong = namedtuple('LatLong', 'lat long')

delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))

delhi = City._make(delhi_data)

print(delhi._asdict())

# k v 뿌리기
for key, value in delhi._asdict().items():
    print(key + ':', value)

# slicing

l = [10, 20, 30, 40, 50, 60]

# stride s[a:b:c] c 보폭(stride)만큼 항목을 건너뛴다.

s = 'bicycle'
s[::3]

# 다차원 슬라이싱과 생략기호
# ...는 Ellipsis 객체의 별명으로서 하나의 ellipsis클래스의 객체다.
#

# 시퀀스 곱셈 연산자 주의

my_list = [[]] * 3

my_list[1].append(1)
print(my_list)

# 리스트의 리스트 만들기

board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

# [['_'] * 3] * 3 동일한 리스트에 대한 세 개의 참조를 가진 리스트는 쓸모없다.

weired_board = [['_'] * 3] * 3
print(weired_board)

weired_board[1][2] = '0'
print(weired_board)

# 시퀀스의 복합할당