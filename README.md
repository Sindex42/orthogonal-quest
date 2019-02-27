# Team Super Slack Bros - Final Project
[![Build Status](https://travis-ci.com/Sindex42/orthogonal-quest.svg?branch=master)](https://travis-ci.com/Sindex42/orthogonal-quest)
[![Maintainability](https://api.codeclimate.com/v1/badges/8ed18253d38f39e5ff4e/maintainability)](https://codeclimate.com/github/Sindex42/orthogonal-quest/maintainability)

A two week group project to build a game in Python using Pygame

* Our [Trello board](https://trello.com/b/mXUdQOWW/final-project-team-super-slack-bros)

Contributors:

* [Chris Hassan](https://github.com/CKKH)
* [Connor Kam-Cheong](https://github.com/sindex42)
* [James Hotblack](https://github.com/hotblack86)
* [Michael Nguyen](https://github.com/michaelnguyen974)
* [Thomas Lawrence](https://github.com/matharotheelf)

## Getting Started

### System Requirements

`python 3.7` and The Python Package Installer `pip 18.1` are required to install and
play Orthogonal Quest.

Please check that your system has these requirements before attempting Orthogonal
Quest installation.

To do this open your operating system's terminal. Once in your terminal:

1. run `python3 -V`. If you see the Output `Python 3.7.X`
2. run `pip -V`. If the Output starts with `pip 18.1` at the beginning, please see
the game installation section.

If you do not have `python 3.7` or your version is less than `3.7`, you will need to
install/ upgrade it. The guides from DigetalOcean are recommended for this. They
also cover installation of `pip`. The following are some examples but you may need
to find the guide relavant to your computer's exact operating system:

- [Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-18-04)
- [macOS](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-macos)
- [Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)


### Game Installation

#### Virtual Environment

We recommend using a virtual environment for your Pygames to keep your Python
packages separate. Please refer to the DigitalOcean links above for more information
on virtual environments and why it is a good idea to use them.

To do this:

1. In your terminal navigate to the location you want your environments to be saved.
2. Create your virtual environment using venv `python3.7 -m venv [name_of_your_env]`
3. Activate your environment `source /[path_to_your_env]/bin/activate`

#### Clone & build dependancies

From your termainal, navigate to the directory you would like to save your game
directory and input the following commands:

```
mkdir PyGames
cd PyGames
git clone git@github.com:Sindex42/orthogonal-quest.git
cd orthogonal-quest
source /[path_to_your_env]/bin/activate
pip install -r requirements.txt
```


### Begin your quest!

From the `orthogonal-quest` directory root, run `python ./src/main.py`. Your virtual 
environment must be activated in order for this to work.


## User Stories

```
As a user
So I can play the game
I would like to be able to boot it up from the console

As a user
So I can play the game
I would like to be able to see a game screen

As a game dev
So I can build a map
I would like the game world to be divided into a grid

As a user
So I can begin my quest
I would like to be able to see a hero

As a user
So I know who I control
I would like to be able to move the hero orthogonally

As a user
So I can control my hero
I would like to be able to move one tile at a time

As a user
So I know what I’m up against
I would like to be able to see an enemy

As a user
So I know what I’m up against
I would like the enemy to be static

As a user
So I know the boundaries of the game
I would like to be able to collide with the walls

As a user
So I know how big the game world is
I would like there to be only one room

As a game dev
So I know I bumped into the wall
I would like to be able to see the collision in the console

As a user
So I know I bumped into a wall
I would like the hero to not leave the edge of the screen

As a game dev
So I know I bumped into an enemy
I would like to be able to see the collision in the console

As a user
So I know I bumped into an enemy
I would like the hero and the enemy to not overlap

As a game dev
To make the game more interactive
I would like to give enemies random movement

As a game dev
To make the game a challenge
I would like enemies to kill heros on collision

As a game dev
To make the game look good
I would like enemies to appear as sprites

As a game dev
To make the game look good
I would like wall tiles to be textured

As a game dev
To make the game look good
I would like background tiles to be textured

As a user
So I can kill my enemies
I would like to be able to attack them

As a user
So I can kill my enemies
I would like them to die when I hit them

As a game dev
So the game is more of a challenge
I would like there to be multiple enemies

As a game dev
To make my game sound good
I would like to embed sounds on events

As a user,
So I can know how to play the game, 
I want to see instructions on a start screen

As a user, 
So I know when I die
I want to see a game over screen

As a user, 
So I can play again after game over,
I want to be redirected to the start screen

As a user, 
So I can win the game when I kill all enemies,
I would like to have a win screen

As a user, 
So I can play again after winning,
I want to be redirected to the start screen

As a user,
So I don't die as as easily,
I would like some Hitpoints

As a user, 
So I know how much health I have,
I would like see my health bar

As a game dev,
So I can go to various levels of the game when I defeat all enemies,
I would like progress to different maps

As a game dev, 
So I can feel the adrenaline,
I would like to defeat a Boss
```


## Testing

- Install packages `pip install -e .`


## Usage


## Technologies used

Tech | Description
------------- | -------------
[Python3](https://www.python.org/) | Main language
[Pygame](https://www.pygame.org/news) | Ruby web application framework
[Travis CI](https://travis-ci.org/) | Continuous integration running tests and linters before merging branches
[Code Climate](https://codeclimate.com/) | Automated code reviview for code quality and complexity


## Learning log

* To see a log of our learnings throughout this project, please refer to our project [wiki](https://github.com/Sindex42/super-slack-bros/wiki)


## How to Contribute

We'd love to hear from you if have anything to contribute to help us improve Orthonogal Quest. To do so: 

1. Fork the repo
2. Make as regular and as small commits as possible
3. Leave super clear commit messages along the way
4. Make a pull request back to this repo explaining the contributions you made

Your name will of course be added to our list of contributors if your pull request is approved.
