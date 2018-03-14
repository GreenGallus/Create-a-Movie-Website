import fresh_tomatoes
import Make_A_Movie

# List for class to initialize based on sequence of movie_title, movie_storyline,
# poster_image, trailer_youtube of each movie.
the_greatest_showman = Make_A_Movie.Movie("The Greatest Showman",
                                        "Inspired by the imagination of P. T. Barnum, The Greatest Showman is an original musical that celebrates the birth of show business & tells of a visionary who rose from nothing to create a spectacle that became a worldwide sensation.",
                                        "http://t3.gstatic.com/images?q=tbn:ANd9GcSIBSGJLB8aasi7cB1FCPjg0L6XAw9GYZ4uQY1MsQGX2e8H_mCq",
                                        "https://www.youtube.com/watch?v=EodWwczRIe4")
# print the_greatest_showman.storyline
# the_greatest_showman.pop_trailer()

la_la_land = Make_A_Movie.Movie("La La Land",
                            "Sebastian (Ryan Gosling) and Mia (Emma Stone) are drawn together by their common desire to do what they love. But as success mounts they are faced with decisions that begin to fray the fragile fabric of their love affair, and the dreams they worked so hard to maintain in each other threaten to rip them apart.",
                            "http://t2.gstatic.com/images?q=tbn:ANd9GcRhFtgdSYQ89vUMjMJal2D8H39qBCkh9ptCEoZEsafOzkeQPTu2",
                            "https://www.youtube.com/watch?v=d9DtsfjgnZ8")
# print la_la_land.storyline
# la_la_land.pop_trailer()

my_fair_lady = Make_A_Movie.Movie("My Fair Lady",
                                "In this beloved musical, pompous phonetics professor Henry Higgins (Rex Harrison) is so sure of his abilities that he takes it upon himself to transform a Cockney working-class girl into someone who can pass for a cultured member of high society. His subject turns out to be the lovely Eliza Doolittle (Audrey Hepburn), who agrees to speech lessons to improve her job prospects. Higgins and Eliza clash, then form an unlikely bond -- one that is threatened by an aristocratic suitor (Jeremy Brett).",
                                "http://static.tvtropes.org/pmwiki/pub/images/My_Fair_Lady_poster_7599.jpg",
                                "https://www.youtube.com/watch?v=q5fW7sERw7I")
# print my_fair_lady.storyline
# my_fair_lady.pop_trailer()

breakfast_at_tiffany = Make_A_Movie.Movie("Breakfast At Tiffany's",
                                        "Based on Truman Capotes novel, this is the story of a young woman in New York City who meets a young man when he moves into her apartment building. He is with an older woman who is very wealthy, but he wants to be a writer. She is working as an expensive escort and searching for a rich, older man to marry.",
                                        "https://swh-826d.kxcdn.com/wp-content/uploads/2011/05/Breakfast-at-Tiffany%E2%80%99s.jpg",
                                        "https://www.youtube.com/watch?v=7sL5AwACbjw")
# print breakfast_at_tiffany.storyline
# breakfast_at_tiffany.pop_trailer()

titanic = Make_A_Movie.Movie("Titanic",
                            "James Cameron's 'Titanic' is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era -- the 'ship of dreams' -- which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.",
                            "https://static.rogerebert.com/uploads/movie/movie_poster/titanic-1997/large_s2Z25JcBWS9tKAysSKuWyon5lwP.jpg",
                            "https://www.youtube.com/watch?v=zCy5WQ9S4c0")
# print titanic.storyline
# titanic.pop_trailer()

avatar = Make_A_Movie.Movie("Avatar",
                            "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planets environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                            "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                            "https://www.youtube.com/watch?v=6ziBFh3V1aM")
# print avatar.storyline
# avatar.pop_trailer()

movies = [the_greatest_showman, la_la_land, my_fair_lady, breakfast_at_tiffany, titanic, avatar]
# fresh_tomatoes.open_movies_page(movies)
# print (Make_A_Movie.Movie.VALID_RATING)
# print (Make_A_Movie.Movie.__doc__)
# print (Make_A_Movie.Movie.__name__)
# print (Make_A_Movie.Movie.__module__)
