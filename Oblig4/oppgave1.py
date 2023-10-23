# AUTHOR EMIL BERGLUND #

'''
Opprett en klasse for filmer med inneholder instansvariabler for filmtittel, utgivelsesår og score.  

Bruk denne klassen til å opprette et objekt for hver av de følgende filmene: 

Inception - Utgivelsesår: 2010, Score: 8.8 
The Martian - Utgivelsesår: 2015, Score: 8.0 
Joker - Utgivelsesår: 2019, Score: 8.4 '''

class Film:
    def __init__(self, movieTitle, movieYear, movieRating):
        self.movieTitle = movieTitle
        self.movieYear = movieYear
        self.movieRating = movieRating

    def get_navn(self):
        return self.movieTitle
    def get_år(self):
        return self.movieYear
    def get_score(self):
        return self.movieRating
    def print_info(self):
        return f"{self.movieTitle} was released in {self.movieYear} and has a rating of {self.movieRating}"

inception = Film("Inception", 2010, 8.8)
theMartian = Film("The Martian", 2015, 8.0)
joker = Film("Joker", 2019, 8.4)

print(f"{inception.get_navn()} was released in {inception.get_år()} and has a rating of {inception.get_score()}")
print(f"{theMartian.get_navn()} was released in {theMartian.get_år()} and has a rating of {theMartian.get_score()}")
print(f"{joker.get_navn()} was released in {joker.get_år()} and has a rating of {joker.get_score()}")

print("\n",inception.print_info(), theMartian.print_info(), joker.print_info(), sep="\n")