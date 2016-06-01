# Sean Moriarty
#2016-05-25
# Homework 2

numbers = [22, 90, 0, -10, 3, 22, 48]
print('There are', len(numbers), 'numbers in the list')
print('The 4th number in the list is', numbers[3])
print('The sum of the 2nd and 4th elements of the list is', numbers[1] + numbers[3])
sorted_numbers = sorted(numbers)
print('The second largest number in the list is', sorted_numbers[5])
print('The last number in the original list is', numbers[6])
print('As long as I understood the correct order of things in the silly list, the answers should be:')
for number in numbers:
    if number<10:
        if number%2==0:
                if number!=-10:
                    print(number*30+6-1)
                else:
                    print(number*30+6)
        else:
                if number!=-10:
                    print(number*30-1)
                else:
                    print(number*30)
    elif number>50:
        print(number-10-1)
    else:
        if number!=-10:
            print(number-1)
        else:
            print(number)

total=0
for number in numbers:
    total=total+number/2
print('The sum of each of the numbers divided by two is', total)
movie={'title': 'Bladerunner', 'year': '1982', 'director': 'Ridley Scott', 'budget': '28000000', 'boxoffice': '27000000'}
print('My favorite movie is', movie['title'], 'which was released in', movie['year'], 'and was directed by', movie['director'])
if int(movie['budget'])>int(movie['boxoffice']):
    print('It lost about $', int(movie['budget'])-int(movie['boxoffice']), 'in the theatres, which means it was a flop')
else:
    if int(movie['boxoffice'])>(5*int(movie['boxoffice'])):
        print('It made about $', int(movie['boxoffice'])-int(movie['budget']), 'in the theatres, which means it was a good investment')
    else:
        print('It made about $', int(movie['boxoffice'])-int(movie['budget']), 'in the theatres, which is meh')
boropop={'Manhattan': '1600000', 'Brooklyn': '2600000', 'The Bronx': '1400000', 'Queens': '2300000', 'Staten Island': '470000'}
print('The population of Brooklyn is', '%.3G' % (int(boropop['Brooklyn'])/1000000), 'million')
totalpop=int(boropop['Manhattan'])+int(boropop['Brooklyn'])+int(boropop['The Bronx'])+int(boropop['Queens'])+int(boropop['Staten Island'])
#print(totalpop/1000000)
print('The total population of the five boroughs is', int(totalpop)/1000000, 'million')
poppercent=int(boropop['Manhattan'])/int(totalpop)*100
print('%.3G' % poppercent + "% of the people in the five boroughs live in Manhattan")
