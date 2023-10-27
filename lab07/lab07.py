class Animal(): #創建一個Animal class
    def __init__(self, weight, mood): #建立建構式
        self.weight = weight
        self.mood = mood
    def feed(self, N):
        pass
    def walk(self, N):
       pass
    def bath(self, N): #bath相同，所以兩動物繼承
        self.mood -= 2*N

class Dogs(Animal): #建立Dogs class
    def feed(self, N): #建立feed行為
        self.weight += 0.2*N
        self.mood += 1*N
    def walk(self, N): #建立walk行為
        self.weight -= 0.2*N
        self.mood += 2*N
    def action(self , n_feed , n_walk , n_bath): #輸入行為個別執行次數
        dog.feed(n_feed)
        dog.walk(n_walk)
        super().bath(n_bath) #呼叫Animal的bath
        print(f"狗狗現在的體重= {self.weight}, 心情= {self.mood}") #print出狀態

class Cats(Animal):
    def feed(self, N):
        self.weight += 0.1*N
        self.mood += 1*N
    def walk(self, N):
        self.weight -= 0.1*N
        self.mood -= 1*N
    def action(self, n_feed, n_walk, n_bath):
        cat.feed(n_feed)
        cat.walk(n_walk)
        super().bath(n_bath) #呼叫Animal的bath
        print(f"貓貓現在的體重= {self.weight}, 心情= {self.mood}") #print出狀態

dog = Dogs(4.8, 65) #輸入Dogs基本數值
dog.action(18, 10, 4) #輸入行為的個別次數

cat = Cats(8.2, 60) #輸入Cats基本數值
cat.action(40, 7 , 1) #輸入行為的個別次數
