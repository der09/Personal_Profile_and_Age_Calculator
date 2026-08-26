# Personal_Profile_and_Age_Calculator


print()
print()

#the introduction 
print("Hello! Welcome!!")
print("I will be asking some questions!")
print("Then I'll calculate how long you've lived!")

print()

#asking for the users name
name = input("What's your name?: ")

#asks user for birth year then converts into integer 
birth_year = input("What year were you born? ")
birth_year_num = int(birth_year)

print() 

#asking for their favorites 
favorite_food = input("What's your favorite food?: ")
favorite_hobby = input("What's your favorite hobby?: ")

#asking what city they live in 
city = input("What city do you live in?: ")

#additional questions for the user, which asks for their favorites as well 
favorite_season = input("What's your favorite season?: ")
favorite_game = input("What's your favorite game?: ")

#the calculations for how long the user has lived in years 
age = 2026 - birth_year_num

#calculations for how long they've lived specifically 
months_alive = age * 12
days_alive = age * 365
hours_alive = days_alive * 24 
minutes_alive = hours_alive * 60
seconds_alive = minutes_alive * 60 

print() 
#the beginning of the personalized profile (the final product)
print("This is your profile!")

print()
print()

print("Hello! " + name)
print("You were born in the year " + birth_year)
print("You live in the city " + city)

print()

#telling the user their favorites 
print("Your favorite food is " + favorite_food)
print("Your favorite hobby is " + favorite_hobby)
print("Your favorite season is " + favorite_season)
print("Lastly, your favorite game is " + favorite_game)


print()
print()

#telling the user how long they've lived 
print("Your age is ", age)
print("You've lived ", months_alive, " months!")
print("You've lived ", days_alive,  " days!")
print("You've lived ",  hours_alive, " hours!")
print("You've lived ", minutes_alive, " minutes!") 
print("You've lived ",  seconds_alive,  " seconds!")


print() 
print() 

#the closing statements 
print("Thank you so much for participating!")
print("Have a good day, and enjoy " + favorite_food + "!")
