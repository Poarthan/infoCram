# infoCram
An open source customizable tool for studying aid.

## Basic Setup
This is developed primarily for a debian-flavored linux system, so the README instructions will mirror that, but the match game is runnable on other systems.
```
sudo apt-get update && sudo apt install python3 python3-pip -y
pip install -r requirements.txt
```

## Match
The matching game is still in the works, has some obvious flaws with longer words, no timer and no way to replay and no leaderboard.

To run just do:
```
python3 match.py
```

## Learn
More important is learn, which is a good way to quickly memorise a bunch of things. The algorithm for this is a bit basic, will try to improve later on, but I like the typing to answer format that quizlet requires compared to other learning software just using flashcards. With quizlet's recent paywalls this project has become slightly more useful.

To run just do:
```
python3 learn.py
```
