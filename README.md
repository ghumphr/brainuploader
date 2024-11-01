# BrainUploader
BrainUploader implements a structured learning program to let you memorize large amounts of information quickly.  Upload information to your brain!

(note: this revision contains copy-paste code from the assignment description that must be edited; please disregard any obviously incorrect or apparently plagiarized text below until this notice is removed)

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
To run my awesome app simply,
```bash
python manage.py runserver
```
See in-app menus for help with using specific features.

# License

Copyright (C) Geoffrey Humphreys 2024
All Rights Reserved

BrainUploader is made available to the community under the Gnu Affero General Public License, which is the strongest copyleft license available. Please see LICENSE for details.

