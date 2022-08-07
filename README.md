# infoCram
This is in the works tool for studying, its going to stay pretty messy, as the goal is for this to help me, and anyone else who wants to use it or improve it can feel free to.
It takes obvious inspiration from quizlet, but the goal is to be able to develop some things that quizlet can't do that will be helpful for studying. I already have a few ideas in mind, but I needed an open source version of the mapping game for my AI project so that's what this first part is.

## Basic Setup
This is developed primarily for a debian-flavored linux system, so the README instructions will mirror that, but the match game is runnable on other systems.
```
sudo apt-get update && sudo apt install python3 python3-pip -y
pip install -r requirements.txt
```

## Match
The matching game is still in the works, has some obvious flaws with longer words, no timer and no way to replay and no leaderboard, these will be added soon.

To run just do:
```
python3 match.py
```

