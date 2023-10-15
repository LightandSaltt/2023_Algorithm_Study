while True :
    try :
        print(input())
    except EOFError:
        break

#EOFError를 제외한 나머지는 가능이기에 11718과 같이 쓸 수 있음