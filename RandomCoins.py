numberOfCoin = int(input("Enter the number of coins   :")) # I get the number of coins the user wants to drop.

attempt=0 # I make the number of attempts 0 at the beginning. Because I have to count the coins.

counter1=0 # Here I opened a separate counter for each chamber.
counter2=0
counter3=0
counter4=0
counter5=0
counter6=0
counter7=0
counter8=0
counter9=0
counter10=0

while attempt<numberOfCoin: # I use the while loop to drop all the user's coins.
                            # And I finish when the number of attempts is equal to the number of coins.
    import random

    random_ = random.randint(0, (2 ** 9)) # I use random numbers because this mechanism based on chance.
                                          # And a coin has 2^9 different path combinations.

    if (random_<(2**9)*(1/10)): # I divided the number 2^9 into ten separate sections and assigned each section to a chambers.
        counter1=counter1+1 #I increased the counters in each chamber to count a coin enters the chamber.
    elif ((2**9)*(1/10)<random_<(2**9)*(2/10)):
        counter2=counter2+1
    elif ((2**9)*(2/10)<random_<(2**9)*(3/10)):
        counter3=counter3+1
    elif ((2**9)*(3/10)<random_<(2**9)*(4/10)):
        counter4=counter4+1
    elif ((2**9)*(4/10)<random_<(2**9)*(5/10)):
        counter5=counter5+1
    elif ((2**9)*(5/10)<random_<(2**9)*(6/10)):
        counter6=counter6+1
    elif ((2**9)*(6/10)<random_<(2**9)*(7/10)):
        counter7=counter7+1
    elif ((2**9)*(7/10)<random_<(2**9)*(8/10)):
        counter8=counter8+1
    elif ((2**9)*(8/10)<random_<(2**9)*(9/10)):
        counter9=counter9+1
    elif ((2**9)*(9/10)<random_<(2**9)*(10/10)):
        counter10=counter10+1


    attempt = attempt + 1 # I increased the number of attempts before the while loop repeats.

print('Number of coins in chamber 1 is...:', counter1)
print('Number of coins in chamber 2 is...:', counter2)
print('Number of coins in chamber 3 is...:', counter3)
print('Number of coins in chamber 4 is...:', counter4)
print('Number of coins in chamber 5 is...:', counter5)
print('Number of coins in chamber 6 is...:', counter6)
print('Number of coins in chamber 7 is...:', counter7)
print('Number of coins in chamber 8 is...:', counter8)
print('Number of coins in chamber 9 is...:', counter9)
print('Number of coins in chamber 10 is...:', counter10)

print('**************<HISTOGRAM>**************')

# And after that I wrote for the histogram.
a = '- '*20
print("{}\n|1| {}\n{}\n|2| {}\n{}\n|3| {}\n{}\n|4| {}\n{}\n|5| {}\n{}\n|6| {}\n{}\n|7| {}\n{}\n|8| {}\n{}\n|9| {}\n{}\n|10| {}\n{}".format(a,counter1*"o ",a,counter2*"o ",a,counter3*"o ",a,counter4*"o ",a,counter5*"o ",a,counter6*"o ",a,counter7*"o ",a,counter8*"o ",a,counter9*"o ",a,counter10*"o ",a))