N=int(input("시험을 본 갯수 : "))
M=list(map(int, input("시험점수 : ").split()))
# list(map(int, input("").split()))는 입력한 여러 값을 하나의 list로 만들어주는 것
#max 함수는 최댓값을 찾는 함수 아래 코드에서는 M함수에 있는 수 중 가장 큰 값
max_=max(M)

for i in range(N):
    M[i]=M[i]/max_ * 100

print("%.2f"%(sum(M)/N))

#%.2f 는 소숫점 둘째짜리까지 출력하게하는것