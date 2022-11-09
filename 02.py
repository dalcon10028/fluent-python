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
#
tuple(ord(symbol) for symbol in symbols)
import array
print(array.array('I', (ord(symbol) for symbol in symbols)))