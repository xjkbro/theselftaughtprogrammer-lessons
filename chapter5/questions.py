# Q1 List favorite musicians
musicians = ["Childish Gambino", "Keshi", "Joji"]

# Q2 List of tuples, with each tuple containing the longitude and latitude of somewhere you've lived or visited
locations = [ (40.7128, 74.0060), (34.0522, 118.2437), (37.7749, 122.4194)]

# Q3 Dictionary containing attributes about yourself: height, favorite color, favorite movie, etc.
myself = {
    "height": "5'10",
    "favorite color": "red",
    "favorite movie": "Magic Mike",
    "favorite food": "sushi",
    "favorite programming language": "Javascript"
    }
print(myself)
# Q4 Write a program that lets the user ask your height, favorite color, or favorite author, and returns the result from the dictionary you created in the previous challenge.
user = {
    "height": input("What is your height? "),
    "favorite color": input("What is your favorite color? "),
    "favorite movie": input("What is your favorite movie? "),
    "favorite food": input("What is your favorite food? "),
    "favorite programming language": input("What is your favorite programming language? ")
}
print(user)

# Q5 Create a dictionary mapping your favorite musicians to a list of your favorite songs by them.
artists = {
	"Childish Gambino": ["This is America", "Redbone", "3005"],
	"Keshi": ["Right Here", "2 soon", "over u"],
	"Joji": ["Slow Dancing in the Dark", "Will He", "Demons"]
}

print(artists["Childish Gambino"])

# Q6 Research the other containers Python provides. What is a set? When would you use it?
# A set is a collection of unordered, unique elements. 
# You would use it when you want to store a collection of unique elements.
