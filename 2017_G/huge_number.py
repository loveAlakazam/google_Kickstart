def solutions(N,A):
    result=A
    for i in range(1,N+1):
        result= result**i
    return result
    
def main():
    #input_file= open('A-small-practice.in', 'r') #smalldataset: 성공
    input_file= open('A-large-practice.in', 'r')
    output_file = open('hugeNum_large.txt', 'w')
    
    cases=int(input_file.readline())
    for case in range(cases):
        #"1 10 2" => 
        A,N,P = map(lambda x: int(x), (input_file.readline()).split(' '))
        ans=solutions(N,A)%P
        output_file.write('Case #{}: {}\n'.format(case+1, ans))
        print('Case #{}: {}\n'.format(case+1, ans))
        print('A,N,P: ', A,N,P)
if __name__=='__main__':
    main()
