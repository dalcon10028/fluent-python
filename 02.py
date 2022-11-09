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
import array
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
latitude, longtitude = lax_coodinates # 튜플 언패킹
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
import os
_, filename = os.path.split('/home/aaa/bbb')
print(filename)

# 전통적으로 _는 gettext.gettext()함수의 대한 별명으로 사용된다. 그 외의 경우에는 _를 플레이스홀더로 사용하는 것이 좋다.

# 초과 항목을 잡기 위해 * 사용하기
