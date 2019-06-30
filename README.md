#PITCHES
A web application that lets users submit pitches based on different categories

## BY William Mango https://github.com/mangowilliam/   01/07/19

## Description
This is an application that allows a user to create a pitch depending on a certain category and add pitch content. A user can also be able to comment and vote on another user's pitches.

## user stories
* view pitches
* login
* pitch
* downvote and upvote
* view personal pitches on profile
* comment on pitches
## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | click horuku link url | view othr pitches  & vote          |
| click on a pitch   |                       | vote/comment                       |
| sign in/up         | details pass & user   | view,pitch & comment               |

## Prerequisites
* Python3.6
## Setup/Installation Requirements
* internet access
* git clone https://github.com/mangowilliam/pitch-perfect
* $ cd into pitch-perfect
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = * create_app('production') should be app = create_app('development')
* $ ./start.sh
* or click on this link and follow the steps in the BDD ""
## Known Bugs

No known bugs

## Technologies Used
Python3.6
Postgressql
flask botsrap
css
html  
## Support and contact details
contact williammango2015@gmail.com for any kind of support.
## Live Link
https://github.com/mangowilliam/pitch-perfect

### License

The project is licensed under MIT license https://opensource.org/licenses/MIT
Copyright (c) 2019, mango