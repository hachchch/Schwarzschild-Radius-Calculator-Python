import math
def slogenie(a1, b1):
    return (a1 + b1)
  
  d = True
while (d):
    print("r=2GM/C^2でシュバルツシルト半径を求めます。")
  
  
    while True:
        try:
           menu = int(input("質量を入力してください："))
           break
        except ValueError:
             print("えらーだよ！")
