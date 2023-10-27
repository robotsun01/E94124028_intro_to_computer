class Animal(): #建立Animal class
    def __init__(self, weight, mood): #建立建構式
        self.weight = weight
        self.mood = mood
    def feed(self, N):
        pass
    def walk(self, N):
       pass
    def bath(self, N): #相同的bath
        self.mood -= 2*N

class Dogs(Animal): #建立Dogs繼承Animal
    def feed(self, N): #建立feed行為
        self.weight += 0.2*N
        self.mood += 1*N
    def walk(self, N): #建立walk行為
        self.weight -= 0.2*N
        self.mood += 2*N
    def bath(self, N): #呼叫Animal的bath
        super().bath(N)
    def action(self , n_feed , n_walk , n_bath):
        dog.feed(n_feed)
        dog.walk(n_walk)
        dog.bath(n_bath)
        print(f"狗狗現在的體重= {self.weight}, 心情= {self.mood}")

class Shiba(Dogs): #建立shiba繼承Dogs
    def feed(self, N): #建立feed行為
        self.weight += 0.3*N
        self.mood += 5*N
    def walk(self, N): #呼叫Dogs walk
        super().walk(N)
    def bath(self, N): #呼叫Dogs bath
        super().bath(N)
    def action(self , n_feed , n_walk , n_bath): #輸入個行為次數
        shiba.feed(n_feed)
        shiba.walk(n_walk)
        shiba.bath(n_bath)
        print(f"柴犬現在的體重= {self.weight}, 心情= {self.mood}") #print出狀態
    def mood_max(self, mood_max): #定義最大值
        self.mood_max = mood_max
        print(f"mood最高只能為= {self.mood_max}")
        if self.mood > self.mood_max and self.mood < 300: #判別mood是否大於最大值
            self.mood = mood_max
            print(f"所以，柴犬現在的心情= {self.mood}")
            print("mood最高只能為= 300")
        elif self.mood > self.mood_max:
            self.mood = mood_max
            print(f"所以，柴犬現在的心情= {self.mood}")


dog = Dogs(4.8, 65)

shiba = Shiba(5 , 70)
shiba.action(20 , 10 , 3)
shiba.mood_max(90)

