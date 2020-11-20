# CTR Static Nonce Lab

The hacking lab for static nonce in CTR mode

## Let Play

Please hack this lab on your own environment. And then, get a real flag [HERE!](https://ctr-static-nonce-lab.herokuapp.com/).

## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org). To push to Heroku, you'll need to install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).

```sh
$ git clone https://github.com/suam-team/ctr-static-nonce-lab.git
$ cd ctr-static-nonce-lab
$ pip install -r requirements.txt
$ echo "FLAG=flag{ILoveYou}" > .env
$ heroku local
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Deploying to Heroku

```sh
$ heroku create
$ git push heroku main
$ heroku open
```
or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)