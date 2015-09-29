import sys

ratings_file = open("scores.txt")

restaurant_ratings = {}

#read and process ratings from file
for line in ratings_file:
    # data = line.split(":")
    # name = data[0]
    # rating = int(data[1])

    name, rating = line.split(":")
    restaurant_ratings[name] = int(rating)




#sort ratings alphabetically by restaurant name
sorted_restaurant_ratings = sorted(restaurant_ratings.items())

#print out the ratings
for name,rating in sorted_restaurant_ratings:
    print "{name} is rated at {rating}".format(name=name, rating=rating)

ratings_file.close()

#prompt user to update rating
print "Would you like to update a rating or add a new one?"


user_input = raw_input("Choose 1 to update a restaurant or 2 to add a new one.\nPress enter to exit. >")

input_valid = False
while (not input_valid):
    #quit if user has pressed <enter>
    if user_input == "":
        sys.exit()
    else:
        try:
            user_input = int(user_input)
        except:
            print "Error: please enter <1> or <2>"
            user_input = raw_input("Choose 1 to update a restaurant or 2 to add a new one.\nPress enter to exit. >") 
            break
        input_valid = True

#now we have integral user input

if user_input == 1:
    restaurant_to_update = raw_input("Which restaurant would you like to update? >")
    input_valid = False
    while (not input_valid):
        if restaurant_to_update in restaurant_ratings:
            input_valid = True
            break
        else:
            print "ERROR: Please enter a restaurant from the list."
            restaurant_to_update = raw_input("Which restaurant would you like to update? >")

    new_rating = raw_input("Please enter a new rating on a scale of 1 to 5. >")
    input_valid = False
    while (not input_valid):
        try:
            new_rating = int(new_rating)
            if new_rating >= 1 and new_rating <= 5:
                input_valid = True
                break
            else:
                print "ERROR: rating needs to be between 1 and 5. >"
                new_rating = raw_input("Please enter a new rating on a scale of 1 to 5. >")
        except:
            print "ERROR: rating needs to be an integer"
            new_rating = raw_input("Please enter a new rating on a scale of 1 to 5 >")
            continue
        input_valid = True

    restaurant_ratings[restaurant_to_update] = new_rating

elif user_input == 2:
    new_restaurant_name = raw_input("What's the name of the new restaurant? ")
    new_rating = raw_input("Please enter a new rating on a scale of 1 to 5 >")
    input_valid = False
    while (not input_valid):
        try:
            new_rating = int(new_rating)
            if new_rating >= 1 and new_rating <= 5:
                input_valid = True
                break
            else:
                print "Error: please enter a rating between 1 and 5"
                new_rating = raw_input(" >")
        except:
            print "Error: please enter a new rating"
            new_rating = raw_input("Please enter a new rating on a scale of 1 to 5 >")
            continue
        input_valid = True

    restaurant_ratings[new_restaurant_name] = new_rating

else:
    print "ERROR: you suck"
    sys.exit()

sorted_restaurant_ratings = sorted(restaurant_ratings.items())
print sorted_restaurant_ratings