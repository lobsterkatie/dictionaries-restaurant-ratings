ratings_file = open("scores.txt")

restaurant_ratings = {}

#read and process ratings from file
for line in ratings_file:
    data = line.split(":")
    name = data[0]
    rating = int(data[1])
    restaurant_ratings[name] = rating

#sort ratings alphabetically by restaurant name
sorted_restaurant_ratings = sorted(restaurant_ratings.items())

#print out the ratings
for name,rating in sorted_restaurant_ratings:
    print "{name} is rated at {rating}".format(name=name, rating=rating)

ratings_file.close()