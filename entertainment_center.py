#import needed python files
import fresh_tomatoes
import media
#define films with class movie
bedazzled = media.Movie("Bedazzled",
                       "October 20, 2000",
                       "A young man finds himself after being granted 7 wishes by the Devil",
                       "Brendan Fraser, Elizabeth Hurley & Francis O'Connor",
                       "http://ia.media-imdb.com/images/M/MV5BMTc2ODI5NDg3NF5BMl5BanBnXkFtZTcwMzU4NzgyMQ@@._V1_SY317_CR5,0,214,317_AL_.jpg",
                       "http://youtu.be/5xUnFbyqNr4")
contact = media.Movie("Contact",
                       "July 11, 1997",
                       "A young man finds himself after being granted 7 wishes by the Devil",
                       "Jodie Foster, Mathew McConaughey & James Woods",
                       "http://ia.media-imdb.com/images/M/MV5BMjEyMDQxMTMxMF5BMl5BanBnXkFtZTcwNTU0ODcyMg@@._V1_SX214_AL_.jpg",
                       "http://youtu.be/SRoj3jK37Vc")
vickycristina = media.Movie("Vicky, Cristina, Barcelona",
                       "May 17, 2008",
                       "Two girlfriends on a Summer holiday in Barcelona become enamored with the same man, unaware of his ex-wife",
                       "Javier Bardem, Penelope Cruz, Scarlet Johansson & Rebecca Hall",
                       "http://ia.media-imdb.com/images/M/MV5BMTU2NDQ4MTg2MV5BMl5BanBnXkFtZTcwNDUzNjU3MQ@@._V1_SY317_CR0,0,214,317_AL_.jpg",
                       "http://youtu.be/B-RdUcXAKiw")
beforesunrise = media.Movie("Before Sunrise",
                       "January 27, 1995",
                       "An American man and French woman share a night in Vienna after a chance encounter",
                       "Ethan Hawke & Julie Delpy",
                       "http://ia.media-imdb.com/images/M/MV5BMTQyMTM3MTQxMl5BMl5BanBnXkFtZTcwMDAzNjQ4Mg@@._V1_SY317_CR2,0,214,317_AL_.jpg",
                       "http://youtu.be/9v6X-Dytlko")
ihearthuckabees = media.Movie("I Heart Huckabees",
                       "September 10, 2004",
                       "A man seeking answers hires existential detectives but gets more than he bargains for",
                       "Dustin Hoffman, Isabelle Huppert, Jude Law & Jason Schwartzman",
                       "http://ia.media-imdb.com/images/M/MV5BNTAyNTg5NTY2OV5BMl5BanBnXkFtZTcwMzQwODYyMQ@@._V1_SX214_AL_.jpg",
                       "http://youtu.be/2eOLOmCjRPY")
#create array of films
movies = [bedazzled, contact, vickycristina, beforesunrise, ihearthuckabees]
fresh_tomatoes.open_movies_page(movies)
