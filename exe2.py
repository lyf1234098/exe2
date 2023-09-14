import sqlite3
stephen_king_adaptations_list = []
with open('stephen_king_adaptations.txt', 'r') as file:
    stephen_king_adaptations_list = file.read().splitlines()
connection = sqlite3.connect('stephen_king_adaptations.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS stephen_king_adaptations_table
                (movieID INTEGER PRIMARY KEY AUTOINCREMENT,
                movieName TEXT,
                movieYear INTEGER,
                imdbRating REAL)''')1
for adaptation in stephen_king_adaptations_list:
    try:
        movie_id,movie_name, movie_year, imdb_rating = adaptation.split(',')
        cursor.execute('''INSERT INTO stephen_king_adaptations_table 
                        (movieName, movieYear, imdbRating)
                        VALUES (?, ?, ?)''', (movie_name.strip(), int(movie_year), float(imdb_rating)))
    except ValueError:
        continue  

connection.commit()


while True:
    print("1. Search by movie name")
    print("2. Search by movie year")
    print("3. Search by movie rating")
    print("4. STOP")

    option = input("Enter your choice: ")

    if option == '1':
        movie_name = input("Enter movie name: ")
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table WHERE movieName LIKE ?''', ('%' + movie_name + '%',))
        result = cursor.fetchall()

        if result:
            for row in result:
                print("Movie Name:", row[1])
                print("Movie Year:", row[2])
                print("IMDB Rating:", row[3])
        else:
            print("No such movie exists in our database.")

    elif option == '2':
        movie_year = input("Enter movie year: ")
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table
                        WHERE movieYear = ?''', (int(movie_year),))
        result = cursor.fetchall()

        if result:
            for row in result:
                print("Movie Name:", row[1])
                print("Movie Year:", row[2])
                print("IMDB Rating:", row[3])
        else:
            print("No movies were found for that year in our database.")

    elif option == '3':
        rating_limit = float(input("Enter the minimum rating: "))
        cursor.execute('''SELECT * FROM stephen_king_adaptations_table
                        WHERE imdbRating >= ?''', (rating_limit,))
        result = cursor.fetchall()

        if result:
            for row in result:
                print("Movie Name:", row[1])
                print("Movie Year:", row[2])
                print("IMDB Rating:", row[3])
        else:
            print("No movies at or above that rating were found in the database.")

    elif option == '4':
        break

    print()  


connection.close()