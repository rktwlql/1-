Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #문제 2번
>>> 
>>> #속도 상승을 위한 함수를 설정하기 위해서는 매개변수 self를 사용하여 정리하는 것이 옳다.
>>> class Car :
	color = ""
	speed = 0

	
>>> class Car :
	color = ""
	speed = 0
	def upSpeed(self, value):
		self.speed = += value
		
SyntaxError: invalid syntax
>>> class Car :
	color = ""
	speed = 0
	def upSpeed(self, value):
		self.speed += value

		
>>> #문제 4번
>>> 
>>> #속도를 50으로 초기화하는 클래스의 생성자 코드이다.
>>> 
>>> class Horse :
	speed = 0
	def__init__(self):
		
SyntaxError: invalid syntax
>>> class Horse :
	speed = 0
	def __init__(self):
		self.speed=50

		
>>> #def __init__(self):	self.speed=50를 추가하여 해결한다.
>>> 
>>> #문제 6번
>>> 
>>> class Car :
	def method(self):
		print("슈퍼 클래스")

		
>>> class Sedan(Car) :
	def method(self):
		print("서브 클래스")

		
>>> myCar = Car()
>>> mySedan = Sedan()
>>> myCar.method()
슈퍼 클래스
>>> mySedan.method()
서브 클래스
>>> #정답은 3번 슈퍼 클래스 서브 클래스 이다.
>>> 
>>> 
>>> #문제 7번
>>> 
>>> class Car :
	speed=0
	def upSpeed(self, value():
		    
SyntaxError: invalid syntax
>>> class Car :
	speed=0
	def upSpeed(self, value):
		    self.speed=self.speed+value

		    
>>> #여기서 RVCar의 클래스를 정의해야한다.
		    
>>> #또한 Car의 상속을 받아야하기 때문에 다음과 같이 코드를 작성한다.
		    
>>> class RVCar(Car):
	seatNum=0

		    
>>> #후략
		    
>>> #그러니 해당 빈 칸에는 class RVCar(Car): 를 작성하는 것이 옳다.
		    
>>> 
