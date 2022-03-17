print("Hello World")
print("Mary\'s cosmetics")
print("신씨가 소리질렀다. \"도둑이야\".")
print("\"c:\\Windows\"")

print("안녕하세요.\n만나서\t\t반갑습니다.") # \n는 줄바꿈 \t는 문자열 사이에 탭 간격을 줄때 사용합니다

movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

movie_rank.append('배트맨') # 마지막 원소로 배트맨 추가

movie_rank.insert(1, '슈퍼맨') # 2번째 원소에 슈퍼맨 추가

nums = [1, 2, 3, 4, 5]

sum = 0

for i in range(len(nums)):
    sum += nums[i]

print(sum) # nums의 모든 원소의 합

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

print(len(cook)) # cook 배열의 길이

print(sum/len(nums)) # 모두 더한값을 배열전체길이로 나눈 평균 값

print(3==5) # 거짓이므로 false
print(3<5) # 참이므로 true
x=4 
print(1<x<5) # 참이므로 true
print((3==3)and(4!=3)) # 두개가 모두 참이므로 true