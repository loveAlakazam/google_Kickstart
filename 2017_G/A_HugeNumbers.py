# https://code.google.com/codejam/contest/3254486/dashboard
'''
Kick start G- 1

OUTPUT CASE #X: RESULT
TEST CASE : T

1) N!
2) A^N!
3) A^N! /P

'''

def nFactorial(N):
    if N==0: #N=0, 0! = 1
        return 1
    else:# N != 0
        return N* nFactorial(N-1)
    

def power(lower, upper):
    if upper==0:
        return 1
    else: #upper !=0
        return lower * power(lower,upper-1)
   
# a^(n!) %P
def divide(result, P):
    return int(result%P)

def main(A,N,P):
    #upper= N!
    upper=nFactorial(N)
    print('N!=',upper)
    
    #A: lower, poweredA= A^(N!)
    powerA= A**upper 
    #print('A^(N!)=',powerA)

    #result=A^(N!)%P
    result=divide(powerA,P)
    
    return result
    
if __name__=='__main__':
    test=open("A-small-practice.in", "r") #읽기모드로 데이터를 읽는다.
    T=int(test.readline()) #맨위 테스트케이스
    print('T=',T)

    
    #파일 메모장을 만든다. => 메모장에 내용을 입력한다.
    file1= open("result_a.txt", "a") #쓰기모드(기존에 덧붙여서 쓸수있음)
    for t in range(1, T+1): # 1<=t && t<=T
        s=test.readline()
        #print(s)

        A,N,P=[int(i) for i in s.split(' ')]

        result=main(A,N,P)
        file1.write('Case #{}: {}\n'.format(t,result))
           
    test.close()
    file1.close()
