menu = 0
totalmoney = 0
inmoney = 0
outmoney = 0

while (True):
    print("==========예금 입출금 프로그램==========")
    print("# 1 : 입금   # 2 : 출금   # 3 : 잔고 확인   # 4 : 종료 ")
    menu = int(input("원하는 서비스 번호를 입력하세요:"))

    if menu==1:
        inmoney=int(input("입금하실 금액을 입력하세요:"))
        totalmoney=totalmoney+inmoney
        print(inmoney,"원이 입금되었습니다.")
        print("현재 보유하신 잔액은",totalmoney,"원 입니다.")
        
    elif menu==2:
        outmoney=int(input("출금하실 금액을 입력하세요:"))
        if totalmoney>=outmoney:
            leftmoney=totalmoney-outmoney
            totalmoney=leftmoney
            print(outmoney,"원이 출금되었습니다.")
            print("현재 보유하신 잔액은",leftmoney,"원 입니다.")
        else:
            print("잔액을 초과합니다. 현재 잔액은",totalmoney,"입니다.")

    elif menu==3:
        print("현재 보유하신 잔액은",totalmoney,"원 입니다.")

    elif menu==4:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다. 다시 입력하세요. ")
    print("\n")
