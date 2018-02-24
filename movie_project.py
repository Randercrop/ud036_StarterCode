import fresh_tomatoes as ft
import media as media
import entertainment_center as ec

#executes this main function when file is opened with python
if __name__=="__main__":
     
     #grabs movie information from entertainment_center.py
     allMovies = ec.getMovieList()
     
     #initiates movie page with movie information in the allMovies array
     ft.open_movies_page(allMovies)