# The Game of Life - a Command Line Life Simulator

## About the project

This project is a remake of me and my friends' The Game Of Life ([Elämän Peli](https://github.com/ehkuitti/elaman-peli-java)) school game project made in Java. That project
was a school project for the course "The Basics of Programming" I took in my school, Laurea University of Applied Sciences. The idea of the original project was to
be a "game of life". The player plays through different stages of life, like birth, going to schools and attending various exams. There are also random
accidents that can lead to the player's death. Basically the game's purporse is to simulate life in a fun yet simple way. 

## Implementation

This project is made with PyCharm 2022.3 and Python 3.10.

## Improvements

The game is written from the ground up using Python. There are certain improvements on top of the original Java version. For instance,
this version always validates the user's input. For example, if the required input type is an integer, the program will print an error if the input contains letters. This version also has 
some minor improvements, like randomly generated welcome messages using `switch`. On top of that, this version also comes with installation and playing instructions, which are read using `open` from a text file within the build directory.
