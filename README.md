# BrainUploader
BrainUploader implements a structured learning program to let you memorize large amounts of information quickly.  Upload information to your brain!

## Executive Summary
BrainUploader implements a streamlined and simplified adaptation of the [Leitner Cardfile System](https://mindedge.com/learning-science/the-leitner-system-how-does-it-work/). Essentially, BrainUploader allows users to create and review a stack of flashcards and tracks a few key statistics on each flashcard, in particular, the number of times the user has gotten the flashcard right in a row and the last time the flashcard was reviewed. Once the user has gotten the flashcard right once, the user will not see the flashcard again until the next day. If the user has gotten the flashcard right twice, the user will not see the flashcard for two days. Three times, four days, four times eight days, following the equation $$\text{Days to  Next Review} = 2^{\text{Times Right}}$$. In this way, the user will regularly review information that is not yet memorized, while flashcards containing information that is already known will be reviewed infrequently.

## Installation
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

# License

Copyright (C) Geoffrey Humphreys 2024
All Rights Reserved

BrainUploader is made available to the community under the Gnu Affero General Public License, which is the strongest copyleft license available. Please see LICENSE for details.

