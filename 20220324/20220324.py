from audioop import reverse


letters = 'python'
print(letters[0], letters[2]) # 1번째 3번째

string = "PYTHON"
reverse1 = string[::-1]
reverse2 = ''.join(reversed(string))
reverse3 = ''

for i in string:
    reverse3 = i + reverse3

print(reverse1) # slice
print(reverse2) # reversed
print(reverse3) # for loop

domain = ''
url = input('url: ')
print(url)

if url.rfind('kr')!=-1: # 오른쪽부터 kr 검색
    domain = 'kr'
    print(domain)

file_name = "2020_보고서.xlsx"

if file_name.endswith('xlsx'):
    print('xlsx로 끝납니다')
else:
    print('xlsx로 끝나지 않습니다')

if file_name.startswith('2020'):
    print('2020으로 시작합니다')
else:
    print('2020으로 시작하지 않습니다')

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

mypick = input('투자 종목 입력: ')
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

if mypick in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

리스트 = [100, 200, 300]

for i in 리스트:
    print(i+10)

종목 = ["SK하이닉스", "삼성전자", "LG전자"]

for i in 종목:
    print(len(i))
