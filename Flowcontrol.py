#if statement

#int marks =input('Please enter your marks and we will tell your grades...')
'''xString = input('Please enter your marks and we will tell your grades...')
marks = int(xString)

if (marks>80 ):
    print("Your grade ia A :)")
elif (marks> 40) & (marks < 60):
    print("Your grade ia B :|")
else:
    print("You fail :(")

#While statement

num=int(input('Please enter your value...'))
if (num<=0):
    print("Please enter a valid value")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
        print(num)

print(sum)


#for statement
## Beer song
for quant in range(99,0,-1):
    if (quant>1):
        print(quant, 'bottles of beer on the wall', quant ,'bottles of beer.')
        print('Take one down and pass it around, ',quant-1, 'bottles of beer on the wall.')
    elif (quant==1):
        print(quant, 'bottles of beer on the wall', quant, 'bottles of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
    else:
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print('Go to the store and buy some more, 99 bottles of beer on the wall.')


# break statement
count=0
while True:
    count+=1
    print(count)
    if(count>15):
        break
'''

# Continue statement

for x in range (20):
    if (x%2==0):
        continue
    print(x)
