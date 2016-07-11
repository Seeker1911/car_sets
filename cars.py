# Create an empty set literal
showroom = set()
print(type(showroom))
# Add new values to set
showroom.update(['GMC', 'Honda', 'Toyota', 'Ford'])
print(showroom)

# Print the length of set
print(len(showroom))

# Add more cars
showroom.update(['Nissan', 'Lincoln']) 
print(showroom)

# Delete a car
showroom.discard('Nissan')
print(showroom)

# Create another set of cars
junkyard = set()
# Add new cars (with some the same as showroom)
junkyard.update(['Nissan', 'Honda', 'Smart', 'Chevy'])

# return an intersection of the two sets
intersect = showroom.intersection(junkyard)
print(intersect)

# Add the junkyard to the showroom
new_showroom = showroom.union(junkyard)
print(new_showroom)

# Discard a car
new_showroom.discard('Smart')
print(new_showroom)
