# -*- coding: utf-8 -*-
# 문제10 : 별 찍기
# 크리스마스 날, 은비는 친구들과 함께 파티를 하기로 했습니다. 
# 그런데, 크리스마스 트리를 사는 것을 깜빡하고 말았습니다. 
# 온 가게를 돌아다녀 봤지만 크리스마스 트리는 모두 품절이었습니다. 
# 하는 수 없이 은비는 프로그래밍으로 트리를 만들기로 합니다. 

# 은비를 위해 프로그램을 작성해 주세요.

# 입출력 예시

# >> 입력
# 5

# >> 출력
#     *
#    ***
#   *****
#  *******
# *********


# 해결
# 5층으로 만들라는 의도
# 공백이 4,3,2,1,0 개
# 별은 1,3,5,7,9 개

# 4 1
# 3 3
# 2 5 
# 1 7
# 0 9
# 공백: n-1
# 별: 2*i-1

n = 5
for i in range(1,6):
    print(' '*(n-i) + ('*'*(2*i-1)))

print('숫자입력')

user_input = int(input())
for i in range(1,user_input+1):
	print(' '*(user_input-i) + ('*'*(2*i-1)))