# BrainUploader
BrainUploader implements a structured learning program to let you memorize large amounts of information quickly.  Upload information to your brain!

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

