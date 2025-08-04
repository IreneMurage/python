# for ,while , do_while

to_loop=True
i=0

# while (<condition>):

while to_loop:
   if i>10:
      to_loop=False
   print("i is",i)
   i=i+1 

k=0

while k<10:
   print("k is",k)
   k=k+1


#for(let i=0;i<10;i++)
for i in range(10,1, -1):
   print("For loop i is",i)

#for(let i=0;i<10;i++)

for i in range(2,10):
   print("For loop is is",i)

for i in range(0, 500, 2):
    print ("Even numbers are", i)

for x in range (5,1000,100):
    print(x)

      ## ARRAYS
fruits=["Mango","Papaya","Orange"]

for fruit in fruits:
   print(fruit)
     ## OR
for i in range(0,3):
    fruit=fruits[i]
    print(fruit)