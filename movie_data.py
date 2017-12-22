import xlrd
import fresh_tomatoes
from media import Movie

wb = xlrd.open_workbook("movie_data.xls")
sheet = wb.sheet_by_index(0)

# Initialised global list variable based on number of rows
excel_values = [0] * sheet.nrows

def get_excel_data():
    """ Get movie details from excel and store in list by rows"""
    for r in range(sheet.nrows): 
        rows_values = []
        for c in range(sheet.ncols): 
            rows_values.append(sheet.cell_value(r,c))
        excel_values[r] = rows_values 

get_excel_data()

def split_movie_details(movie_details):
    """Split movie details from the movie details list and return a single 
    movie object """
    movie_obj = Movie(movie_details[1], # movie title
                      movie_details[2], # movie poster url
                      movie_details[3], # youtube trailer url
                      movie_details[4], # movie short info
                      movie_details[5]) # wiki url
    return movie_obj

def create_movie_list():
    """create movie list on the fly based on number of rows details in movie
    excel """
    movie_len = len(excel_values) -1
    movies_list = ['0']*movie_len
    for movie in range(movie_len):
        movies_list[movie] = split_movie_details(excel_values[movie+1])
    return movies_list

# creating movie list by calling create_movie_list function
movies = create_movie_list()
fresh_tomatoes.open_movies_page(movies)

