'''
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
sum = int(input("Enter sum: "))
multiply = int(input("Enter multiply: "))
X=1
Y=sum-X
sum1=2
multiply1=1
flag = False
while sum!=sum1 and multiply!=multiply1 :
    Y -= 1
    X += 1 
    if X * Y == multiply:
        flag = True
        sum1= X + Y
        multiply1= X * Y
    
if flag:
    print(X, Y)
else:
    print("uncorrect")
