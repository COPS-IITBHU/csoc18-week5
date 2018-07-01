hello-django
============

The minimum "hello world" for Django 1.4. Views only, no code having anything
to do with model/database/etc.

Assumes Django 1.4+ is installed (`pip install django` or `easy_install django`).
See "Notes" section below.

## Running "Hello World"

From inside the repo root:

    cd mysite
    python manage.py runserver

Then open http://127.0.0.1:8000/ .

## How this repo was put together

These are the commands that were run to create this repo (once I was `cd`'d
into the root of this repo):

    django-admin.py startproject mysite
    cd mysite
    python manage.py startapp myapp

These steps basically define:

1. a `mysite` directory that contains a bunch of Django boilerplate which
   (essentially) defines the "website" you are starting to build.
2. a `myapp` directory inside `mysite`, containing (empty) boilerplate files
   that define a yet-to-be-worked-on Django app. Django projects are split up
   into "apps", that can all define their own database table models, URLs, and
   views. (i.e. on a news website, you could define different apps for `articles`,
   `staff`, and `photos` and work on those sections and features separately)

The result of these "boilerplate generation" steps comprised the [first code commit](https://github.com/mtigas/hello-django/commit/255d88661c025874d5e47c2e1bc5a5d8d624d265).

---

Then `mysite/myapp/views.py` was edited to contain [the little bit of code
you see inside that file now.](https://github.com/mtigas/hello-django/blob/master/mysite/myapp/views.py)

`mysite/mysite/urls.py` was edited to add the following line inside the
`patterns('', ...)`  bit.

    url(r'^$', 'myapp.views.hello'),

These steps comprised [the next commit](https://github.com/mtigas/hello-django/commit/07544b4f17f9bfc3c42874ea0b6b67f84c18e2c4). (See also [comment on that commit](https://github.com/mtigas/hello-django/commit/07544b4f17f9bfc3c42874ea0b6b67f84c18e2c4#commitcomment-1436281).)

That's it.

## Notes

This doesn't use [virtualenv](http://iamzed.com/2009/05/07/a-primer-on-virtualenv/)
or any other "best practices" things to contain the Django installation. This
doesn't explain anything other than how to get plain Python code spitting out
an `HttpResponse` that says "Hello, world" at the / URL.

---

# What now?

You should [read the official Django tutorial](https://docs.djangoproject.com/en/1.4/intro/tutorial01/)
to start learning more about the structure of a Django app and how to use
Django's ORM to work with a database.

The [Django Book](http://www.djangobook.com/en/2.0/) is technically outdated
(originally written for Django 1.0, in 2009), but the first handful of chapters
are a great resource for those learning the ropes.

Once you get your land legs, the [official Django documentation](https://docs.djangoproject.com/en/1.4/)
is a great reference to keep on-hand.

If you're new to Python (and even if you're not), the [Python documentation](http://docs.python.org/)
is equally useful and well-structured in terms of the API. (i.e.: Need to know about the
`datetime` module and see examples of it's functions in use? The [datetime documentation](http://docs.python.org/library/datetime.html)
has you covered.)
