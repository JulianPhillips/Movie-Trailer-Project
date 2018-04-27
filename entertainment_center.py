import fresh_tomatoes
import media
# instantializes the code
avengers = media.Movie("Avengers Infinity War", "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos",
                       "https://cdn.movieweb.com/img.news.tops/NEn12cZhepITqr_8_b/Avengers-Infinity-War-Trailer.jpg", "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
toy_story = media.Movie("Toy Story", "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "http://www.123posters.com/images/movie/f-toystory2.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A Marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=6ziBFh3V1aM")
# puts it into a list
movies = [avatar, toy_story, avengers]
# runs final function
fresh_tomatoes.open_movies_page(movies)
