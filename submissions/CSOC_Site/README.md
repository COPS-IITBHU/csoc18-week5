# CSOC-Site
Django site to help guide freshers and college-aspirants in the amazing life of IIT-BHU!

### TeamName: 
Name: **Laplacian Demons**

Members:
* Shivansh Saini
* P. Shravan Nayak

Website: https://iitbhuguide.ml or https://www.iitbhuguide.ml

### Features
* Registration/Login with Email confirmation
* Forum
* Projects details
* Club details
* Alumni details
* Google Analytics

### How to Run it???
All the required packages are listed in the **requirements.txt** file. Install them all using **pip install -r requirements.txt** at the project root directory (submissions/CSOC_Site/).
Since the database is included, no need to migrate it. Also, collect all static files for WhiteNoise to use by using **python manage.py collectstatic** again at the project root directory.
Finally, use **python manage.py runserver** and test the site locally @ http://127.0.0.1:8000 or http://localhost:8000
For any queries, feel free to open an Issue.

### BROWNIE POINTS
* Team participation - Preferably in groups of two or three (Yep)
* A Logical Roadmap - Not just a website with bunch of features (Yep)
* Backend models(prefer SQL) with a simple database (Yep)
* UI/UX of the website (Yep)
* Django Forms (Yep)
* Google Analytics integration (Yep)
* User login/profile (Yep)
* Social Media integration (Nops)
* Using external API's (Yep)
* List/QuerySet iterators in python (Getting queryset of all objects, rather than filtering. Does it counts?)
* Misc - directory structure and neat code (Yep)

### Work path
We faced quite a lot of trouble in gathering projects details and even had to look in other colleges sites to gather some data. We hope that with this step, our respected seniors from other clubs will also come forward and provide the much-needed information.
And we hope that interested students and new entrants will find the forum interesting and use it well. Currently, due to lack of time, my personal IITBHU email address is used to send emails. I hope to fix that in future.