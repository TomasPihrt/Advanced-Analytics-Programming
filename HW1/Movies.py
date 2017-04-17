# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 21:58:09 2017

@author: Tomas Pihrt

"""

def loadMovieLibrary():
    
    movie_library = {} # Dictionary used - movie as a key, actors in a list as values    
    
    fp = open('data/movies.csv', 'r')
                    
    for line in fp:
        line = line.strip()
        attributes = line.split(',')
        actor = attributes[0]
        movies = attributes[1:]
        for movie in movies:
            if movie in movie_library:
                movie_library[movie].append(actor)
            else:
                movie_library[movie] = [actor]
    
    return movie_library

def validateUserInput(input_text, movie_library):
    if input_text in movie_library:
        return True
    else:
        return False
    
def getUserInput(movie_library, text):
    movie = ''
    while movie == '':    
        input_text = raw_input('Please enter the '+text+' movie: ')
        if validateUserInput(input_text, movie_library):
            movie=input_text
        else:
            print "Sorry, this movie doesm't exist, repeat your input"
    return movie

def matchActors(movie1, movie2, movie_library):    
    actor_list1 = movie_library[movie1]
    actor_list2 = movie_library[movie2]
    actor_list12 = []
    
    for actor1 in actor_list1:
        for actor2 in actor_list2:
            if actor1==actor2:
                actor_list12.append(actor1)
                actor_list1.remove(actor1)
                actor_list2.remove(actor2)
    return [actor_list12, actor_list1, actor_list2]

def genOutput(matched_actors):
    print 'Starring in both movies:', matched_actors[0]
    print 'Starring in the first movie only:', matched_actors[1]
    print 'Starring in the second movie only:', matched_actors[2]

    
def main():
    movie_library = loadMovieLibrary()
    movie1 = getUserInput(movie_library, 'first')
    movie2 = getUserInput(movie_library, 'second')
    
    genOutput(matchActors(movie1, movie2, movie_library))

########################################################

main()