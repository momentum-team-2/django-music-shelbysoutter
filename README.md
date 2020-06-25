# Django Music Collection

Create an application to keep track of all the music albums you own. You can choose what fields each album should have, but it should have at least these three:

- title
- artist
- year released

Your Django app should allow you to do the following:

- See a list of all albums (this should be your homepage)
- Create a new album
- See a detail page for one existing album
- Edit an existing album
- Delete an existing album

Your app should have at least minimal styling using a CSS library like Tachyons or Bootstrap.

A good place to start is planning out your model and making sure you can make an Album object in the console. Make some simple wireframes to sketch out the different functions of the app on the list above, and the urls (and corresponding view functions) you will need to make each page show up. Start with the home page.

## Spicy options 🌶️🌶️🌶️

- Add an Artist model and create a foreign key on the Album model to associate the two.
  - Show the Artist and their other albums on the album detail page, with links to those album detail pages.
- Create an way to mark an album with a star rating.
- Add an option to sort all albums on the list page by title, year, or artist.

## Getting up and running

In your project directory, run the following to install the project dependencies, set up your virtual environment, and run the existing database migrations. After you do these steps you can run your server.

```
> poetry install
> cp django_music/.env.sample django_music/.env
> poetry shell
> ./manage.py migrate
```

### Django Project Template

This project was generated from the Momentum Django project template. This template sets up some minimal changes:

- [django-extensions](https://django-extensions.readthedocs.io/en/latest/) and [django-debug-toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/) are both installed and set up.
- [django-environ](https://django-environ.readthedocs.io/en/latest/) is set up and the `DEBUG`, `SECRET_KEY`, and `DATABASES` settings are set by this package.
- There is a custom user model defined in `users.models.User`.
- There is a `templates/` and a `static/` directory at the top level, both of which are set up to be used.
- A `.gitignore` file is provided.
- [Poetry](https://python-poetry.org/) is used to manage dependencies.

