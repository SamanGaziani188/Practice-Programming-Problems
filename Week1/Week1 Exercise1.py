def frame(lst):
    Max = 0
    for i in range(len(lst)):
        if len(lst[i]) > Max:
            Max = len(lst[i])+1
    print('* ' * Max)
    for i in range(len(lst)):
        remaining = Max - len(lst[i]) 
        print('*', lst[i], ' '*remaining ,  '*')
    print('* ' * Max)

frame(["Hello", "World", "in", "a", "frame"])
    
def soundLyrics(num):
    for i in range(num):
        if i == num-1 :
            print(num-i, "bottle of beer on the wall," ,num-i ,"bottle of beer.")
        else:
            print(num-i , "bottles of beer on the wall" , num-i, "bottles of beer.")
        if i == num-2:
            print("Take one down and pass it around,", num-1-i, "bottle of beer on the wall.")
        elif i == num-1:
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            print("Take one down and pass it around,", num-1-i, "bottles of beer on the wall.")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

    
soundLyrics(99)
