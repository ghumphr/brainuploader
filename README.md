# BrainUploader
BrainUploader implements a structured learning program to let you memorize large amounts of information quickly.  Upload information to your brain!

## Executive Summary
BrainUploader implements a streamlined and simplified adaptation of the [Leitner Cardfile System](https://mindedge.com/learning-science/the-leitner-system-how-does-it-work/) that is unconstrained by the limitations of physical flashcards.

## Installation
Installing BrainUploader is easy. First, clone out the repository. Next, execute the following commands:

```bash
# First, check out the repository and set the working directory to the repository root
more LICENSE
docker build -t brainuploader .
docker run -it brainuploader bash
python manage.py migrate
python manage.py createsuperuser
exit
```

## Getting Started
To launch BrainUploader locally, simply run
```bash
docker run brainuploader python manage.py runserver
```
You can start using BrainUploader at http://localhost:8000/, or you can visit the administration interface at http://localhost:8000/admin/.

## How Is BrainUploader Different than the Leitner Cardfile System?
The Leitner Cardfile System specifies that a series of boxes are to be used to hold flashcards and that flashcards are to be moved between boxes depending on whether they are answered correctly. One box is to be reviewed every day, one every other day, one every five days, and so on in increasing intervals. BrainUploader follows similar philosophy but doesn't use boxes. Instead, the statistics are tracked (virtually) on the cards themselves.

To facilitate learning, BrainUploader tracks a few key statistics for the user on each flashcard between review sessions. In particular, BrainUploader tracks the number of times the user has gotten the flashcard right in a row and the last time the flashcard was reviewed. Once the user has gotten the flashcard right once, the user will not see the flashcard again until the next day. If the user has gotten the flashcard right twice, the user will not see the flashcard for two days. If the user has gotten the flashcard right three times, they won't see it for four days, four times eight days, ... following the equation $$\text{Days to  Next Review} = 2^{\text{Times Right in a Row - 1}}$$. But if the user gets the flashcard wrong, the times-right-in-a-row counter will be reset to 0, so the card will be scheduled for review immediately, and when it is answered correctly, it will be scheduled again on the very next day.

In this way, the user will regularly review information that is not yet memorized, while flashcards containing information that is already known will be reviewed infrequently.

# License

Copyright (C) Geoffrey Humphreys 2024
All Rights Reserved

BrainUploader is made available to the community under the Gnu Affero General Public License, which is the strongest copyleft license available. Please see LICENSE for details.

