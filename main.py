import folium
from geopy.geocoders import Nominatim


def find_coordinates(place):
    """

    str -> (number, number)

    Return coordinates of the place

    """
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    location = geolocator.geocode(place)
    return location.latitude, location.longitude


def add_films_to_list(path, year):
    """

    (str, str, number) -> list

    Return the list of films from file

    """
    with open(path, encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        films = []
        films_names = set()
        for line in lines:
            try:
                checking = float(line[line.index('(', line.index('{')) + 2:
                                      line.index(')', line.index('{'))])
                if line[0] == '"' and line[line.index('(') + 1: line.index(')')] == year \
                        and '}' in line and line[line.index('"') + 1:line.index('"', line.index('"') + 1)] \
                        not in films_names:
                        films.append(line)
                        films_names.add(line[line.index('"') + 1:line.index('"', line.index('"') + 1)])
            except:
                pass
    return films


def add_films_to_map(films, map, film_number):
    """

    (list, Map, number) -> None

    Add markers of films to map

    """
    counter = 0
    for film in films:
        try:
            coordinates = find_coordinates(film[film.index('}') + 1:])
            text = film[film.index('"') + 1:film.index('"', film.index('"') + 1)] + \
                   " " + "(" + film[film.index('{') + 1:film.index('}')] + ")"
            map.add_child(folium.Marker(location=coordinates,
                                        popup=text,
                                        icon=folium.Icon()))
            counter += 1
        except:
            pass
        if counter == film_number:
            break


def add_population_to_list(path):
    """

    str -> list

    Return the list of cities from file

    """
    cities = []
    with open(path, encoding='utf-8', errors='ignore') as file:
        file.readline()
        lines = file.readlines()
        for line in lines:
            cities.append((line[line.index('"') + 1: line.index('"', line.index('"') + 1)],
                           line[line.index(',') + 1: line.index(',', line.index(',') + 1)]))
    return cities


def add_cities_to_map(map, cities, city_number):
    """

    (Map, list, int) -> None

    Add markers of cities with the biggest population

    """
    counter = 0
    for city in cities:
        try:
            coordinates = find_coordinates(city[0])
            counter += 1
            map.add_child(folium.CircleMarker(location=coordinates,
                                              radius=10,
                                              popup=city[0] + " " +
                                                    str(round(float(city[1])/1000000, 1))
                                                    + " mln",
                                              fill_color='red',
                                              color='red',
                                              fill_opacity=0.5))
        except:
            pass
        if counter == city_number:
            break


if __name__ == "__main__":
    while True:
        try:
            year = input("Enter a year of films: ")
            film_number = int(input("Enter a number of films: "))
            city_number = int(input("Enter a number of cities: "))
            out_path = input("Enter a path of output file: ")
            print("Please wait for some minutes...")
            map = folium.Map()
            in_path = "locations.list"
            cities = add_population_to_list("data.csv")
            add_cities_to_map(map, cities, city_number)
            films = sorted(add_films_to_list(in_path, year), reverse=True,
                           key=lambda x: float(x[x.index('(', x.index('{')) + 2:
                                                 x.index(')', x.index('{'))]))
            add_films_to_map(films, map, film_number)
            map.save(out_path)
            break
        except:
            print("Please, try again")

