
#함수를 포함하는 모듈
def plus(a,b):
  return a+b

def minus(a,b):
  return a-b

# __name__ 과 __main__ 은 파이썬이 내부적으로 자동으로 지정한 특수한 시스템 변수
# __name__ 현재 모듈의 이름 변수
# __main__ 은 프로그램의 진입점 실행 시작 파일일 떄 __name__ 이 가지는 값

#이 파일을 직접 실행했을 떄에만 실행하게 되는 테스트 코드

if __name__ == "__main__":    
  print(plus(10,20))
  print(minus(10,20))
