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

    def print_info(self):
        return f"{self.movieTitle} was released in {self.movieYear} and has a rating of {self.movieRating}"

inception = Film("Inception", 2010, 8.8)
theMartian = Film("The Martian", 2015, 8.0)
joker = Film("Joker", 2019, 8.4)

print(inception.print_info(), theMartian.print_info(), joker.print_info(), sep="\n")


