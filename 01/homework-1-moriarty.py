#Sean Moriarty
#23 May 2016
#Homework 1

DoB=input('Enter the year of your birth - ')
if int(DoB)>2016:
    print("You know that's in the future, right?")
    DoB=input('Try that again, dummy - ')
AgeYe=2016-int(DoB)
AgeMi=AgeYe*365*24*60
print('You are approximately', AgeYe, 'years old.')
print('Your heart has beaten roughly', AgeMi*60, 'times.')
print("Meanwhile, a blue whale's heart has beaten about", AgeMi*9, 'times.')
if AgeMi*130<1000000000:
    print("A rabbit's heart, on the other hand, has beaten around", AgeMi*130, 'times.')
else:
    print("A rabbit's heart, on the other hand, has beaten around", '%.3G' % (AgeMi*130/1000000000), 'billion times.')
#the '%.3G' % part comes from http://randlet.com/blog/python-significant-figures-format/
print('You are also', '%.4G' % (AgeYe*365/255), 'Venusian years old.')
print("And for that matter, you're", '%.3G' % (AgeYe/165), 'Neptunian years old.')
#older or younger that me
if AgeYe==33:
    print("Well hey there buddy, you're the same age as lil' ol' me.")
elif AgeYe>33:
    print('You are', AgeYe-33, 'years older than me, and therefore that much closer to death.')
else:
    print('You are', 33-AgeYe, 'years younger than me, and therefore probably sillier.')
#even odd else if
if AgeYe%2==0:
    print('The year you were born in happens to have been even.')
else:
    print('The year you were born in happens to have been odd.')
#long else if statement for the footballs
if int(DoB)<=1974:
    print('The Pittsburgh Steelers have won the Superbowl 6 times since you were born. This no doubt gravely saddens you if you are from anywhere other than Pittsburgh.')
elif int(DoB)<=1975:
    print('The Pittsburgh Steelers have won the Superbowl 5 times since you were born. This no doubt severely saddens you if you are from anywhere other than Pittsburgh.')
elif int(DoB)<=1978:
    print('The Pittsburgh Steelers have won the Superbowl 4 times since you were born. This no doubt seriously saddens you if you are from anywhere other than Pittsburgh.')
elif int(DoB)<=1979:
    print('The Pittsburgh Steelers have won the Superbowl 3 times since you were born. This no doubt moderately saddens you if you are from anywhere other than Pittsburgh.')
elif int(DoB)<=2005:
    print('The Pittsburgh Steelers have won the Superbowl 2 times since you were born. This no doubt somewhat saddens you if you are from anywhere other than Pittsburgh.')
elif int(DoB)<=2008:
    print('The Pittsburgh Steelers have won the Superbowl once since you were born. This no doubt lightly saddens you if you are from anywhere other than Pittsburgh.')
else:
    print("The Pittsburgh Steelers have not wont the Superbowl since you were born. Also, look at you! Using a computer at your age! Aren't you a smart lil' guy!")
#that last else if was long. this one is longer
if int(DoB)<=1945:
    print('Either FDR was president when you were born or you are just too dang old for this program to know.')
elif int(DoB)<=1953:
    print('Harry Truman was either president when you were born, or it was an inagural year. I dunno.')
elif int(DoB)<=1961:
    print('Eisenhower was probably president when you were born. What were your feelings on Ike, and did you like him?')
elif int(DoB)<=1963:
    print('JFK was probably president when you were born. Too bad about that whole thing, eh?')
elif int(DoB)<=1969:
    print("LBJ was likely president when you were born. Vietnam war aside, I hear his name wasn't 'Johnson' for nothing, if you catch my drift.")
elif int(DoB)<=1974:
    print('Nixon was probably president when you were born. Despite what you may have heard, he was definitely a crook. Dat EPA, tho.')
elif int(DoB)<=1976:
    print('Gerald Ford was probably president when you were born. Is he remebered for anything? Honest question.')
elif int(DoB)<=1980:
    print('Jimmy Carter was probably president when you were born. Just the nicest peanut farmer you could ever ask for.')
elif int(DoB)<=1988:
    print('Reagan was probably president when you were born. Mmm, I can still feel those sweet, sweet economics trickling down all over me.')
elif int(DoB)<=1992:
    print("Daddy Bush was probably president when you were born. Definitely raised taxes in spite of what those pillowy lips may have said.")
elif int(DoB)<=2000:
    print('Slick Willy was probably president when you were born. That was some smooth sax, if you know what I mean.')
elif int(DoB)<=2008:
    print('Dubya was probably president when you were born. Notable for being the smartest man in any given room in which he found himself alone.')
else:
    print('Obama was president when you were born. More like NObama, amirite?! High five, bro.')
