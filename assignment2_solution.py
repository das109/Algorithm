user = {'송현재' : [101010, []], '최환수' : [123456, []], '정광현' : [111111, []]} # 가입된 회원정보
booklist = ['창글', '학글', '영발', '영쓰', '컴사', '문알', '미적', '생과', '화학', '문학'] # 도서관에있는 책들
booklist.sort()

login_id = '' # 회원 로그인 아이디 변수
login_pw = 0 # 회원 로그인 비밀번호 변수
command = '' # 로그인 후 기능입력 (대출, 반납, 로그아웃) 변수
bookname= '' #대출 혹은 반납을 원하는 책 제목 변수

print("=======개인 도서관리 프로그램 =======")

while True : #로그인 기능 반복
    login_id = input("ID 입력(0 입력시 종료) : ") #사용자에게 아이디 입력받음
    if login_id == '0': # 프로그램 종료 조건
        print("======프로그램을 종료합니다=======")
        break  
    elif login_id in user.keys(): # 입력한 아이디가 user 딕셔너리에 존재한다면
        login_pw = int(input("PW 입력(6자리 정수) :")) # 비밀번호 입력받기
        if login_pw == user[login_id][0]: # 딕셔너리의 대응되는 value값과 맞다면 기능 사용 가능
            print(login_id, "님 반갑습니다.")
            while True :  # 기능입력 반복
                command = input("필요한 작업을 입력해주세요(대출, 반납, 로그아웃) :") #필요한 기능 입력
                
                if command == '로그아웃': # 기능이 로그아웃이라면
                    print("로그아웃 합니다. 로그인창으로 돌아갑니다.")
                    break
                
                elif command == '대출': # 대출기능
                    print("현재 대출 가능 도서 :")
                    print(booklist)
                    bookname = input("대출을 원하는 도서의 제목을 입력해주세요 :")
                    if bookname in booklist: # 입력한 책 제목이 booklist에 존재하는지 판단 
                        booklist.remove(bookname) #있다면 리스트에서 해당 책을 지우고 
                        user[login_id][1].append(bookname)# 로그인한 유저의 리스트에 저장                    
                        print(bookname,"책을 대출하였습니다.")
                    else :
                        print ("해당하는 책 제목이 없습니다. 기능으로 돌아갑니다.")
                    
                elif command == '반납': #반납기능    
                    print("현재 반납 가능 도서 :")
                    print(user[login_id][1])#로그인한 유저가 빌린 책 리스트를 보여줌              
                    bookname = input("반납을 원하는 도서의 제목을 입력해주세요 :")
                    if bookname in user[login_id][1]: # 반납하고자 하는 책이 유저의 리스트에 있다면 
                        user[login_id][1].remove(bookname) #유저의 대출 리스트에서 해당 책을 지우고 
                        booklist.append(bookname) #해당 책을 booklist에 다시 추가시키기
                        print(bookname, "책을 반납하였습니다.")

                        booklist.sort() # booklist 정렬 
                    else :
                        print("해당하는 책 제목이 없습니다. 기능으로 돌아갑니다.")                        
                else :
                    print("대출, 반납, 로그아웃 중 선택해주세요")
                    
        else:  # 비번 틀릴경우
            print("비밀번호가 틀렸습니다.")                     
    else : # 아이디 틀릴경우
        print("해당 아이디가 존재하지 않습니다.")


        
