# Joshua Martin CIS261 LAB: Movie Guide Version 2
# Defining Call Functions 

def movie_guide():
    print("Welcome to the movie list!\n")
    print("Please Enter a Command to Continue...\n  ")
    print("list --> List all movies")
    print("add --> Add a movie")
    print("delete --> Delete a movie")
    print("exit --> Close the application\n")

# Function to read movie list from file
def read_movie_list(filename):
    try:
        with open(filename, 'r') as file:
            movies = file.readlines()
            return [movie.strip() for movie in movies]  # Remove any extra newlines
    except FileNotFoundError:
        # If file doesn't exist, return an empty list
        return []

# Function to save movie list to file
def save_movie_list(filename, movie_list):
    with open(filename, 'w') as file:
        for movie in movie_list:
            file.write(movie + '\n')

# Create a function that flows into the program that allows users to read and write to a file.
def list(movie_list):
    if movie_list:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie}")
        print()
    else:
        print("No movies available. Please add some movies.\n")

def add(movie_list, filename):
    movie = input("Name:  ")
    movie_list.append(movie)
    save_movie_list(filename, movie_list)  # Save to file after adding
    print(f"{movie} was added.\n")

def delete(movie_list, filename):
    number = int(input("Number:  "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number - 1)
        save_movie_list(filename, movie_list)  # Save to file after deletion
        print(f"{movie} was deleted.\n")

def main():
    filename = "movies.txt"
    movie_list = read_movie_list(filename)  # Load the movie list from file
    movie_guide()
    
    while True:
        command = input("\nPlease type a command:  ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list, filename)
        elif command.lower() == "delete":
            delete(movie_list, filename)
        elif command.lower() == "exit":
            break
        else:
            print("\nNot a valid command, please try again.\n")
            print("Please Enter a Command to Continue...\n\n\n")

if __name__ == '__main__':
    main()
