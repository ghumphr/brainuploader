# BrainUploader
BrainUploader powers a structured learning program to let you memorize large amounts of information quickly.  Upload information to your brain!

## Executive Summary
BrainUploader implements a streamlined and simplified adaptation of the [Leitner Cardfile System](https://mindedge.com/learning-science/the-leitner-system-how-does-it-work/), a study method based on scheduling flashcards for optimal learning. BrainUploader builds upon the Leitner System with commonsense improvements that take advantage of modern technology to remove the constraints inherent in physical flashcards. See below for the nitty-gritty details.

## Installation
Installing BrainUploader is easy. First, clone the repository. Next, execute the following commands:

```bash
# First, check out the repository and set the working directory to the repository root
more LICENSE
docker compose up -d
docker compose exec brainuploader python manage.py makemigrations brainuploader
docker compose exec brainuploader python manage.py migrate
docker compose exec brainuploader python manage.py createsuperuser
docker compose exec brainuploader python generate_sample_flashcards.py
docker compose down
```

These commands are contained in the INSTALL.sh script.

## Getting Started
To launch BrainUploader locally (after installation), simply run
```bash
docker compose up
```
from within the repository.

You can start using BrainUploader at http://localhost:8000/, or you can visit the administration interface at http://localhost:8000/admin/. Please be aware that this is only a prototype; some things are broken, some things are not working, and some things are deliberately disabled. What is working? A card review interface is in place, along with some database connectivity. 

## How Is BrainUploader Different Than the Leitner Cardfile System?
The Leitner Cardfile System specifies that a series of boxes are to be used to hold flashcards. Flashcards are to be moved between boxes depending on whether they are answered correctly. One box is to be reviewed every day, one every other day, one every five days, and so on in increasing intervals. BrainUploader follows similar philosophy but doesn't use boxes. Instead, the statistics are tracked (virtually) on the cards themselves.

## How BrainUploader Works
BrainUploader uses flashcards, scheduling them for review based on a few key statistics tracked on each flashcard for each user. In particular, BrainUploader tracks the number of times the user has gotten the flashcard right in a row and the last time the flashcard was reviewed. Once the user has gotten the flashcard right twice, the user will not see the flashcard again until the next day.

In later review sessions, if the user has gotten the flashcard right three times, the user will not see the flashcard for three days. If the user has gotten the flashcard right four times, they won't see it for seven days, four times fifteen days, ... following the equation $$\text{Days to  Next Review} = 2^{\text{Times Right in a Row - 1}} - 1$$. But if the user gets the flashcard wrong, the times-right-in-a-row counter will be reset to 0, so the card will be scheduled for review immediately, and when it is answered correctly twice, it will be scheduled again on the very next day.

In this way, the user will regularly review information that is not yet memorized, while flashcards containing information that is already known will be reviewed with diminishing frequency.

# License

Copyright (C) Geoffrey Humphreys 2024
All Rights Reserved

BrainUploader is made available to the community under the Gnu Affero General Public License, which is the strongest copyleft license available. Please see LICENSE for details.

