# [ 문제 ] 세 수
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.
# [ 입력 ]
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)
# [ 출력 ]
# 두 번째로 큰 정수를 출력한다.

data = list(input().split(' '))

for i in range(len(data)):
    data[i] = int(data[i])

sorted_list = sorted(data, reverse = True)
print(sorted_list[1])