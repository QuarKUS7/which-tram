# which-tram

A simple web app that returns information to which tram stop one should go when leaving Florentinum in order to get to Letenske namesti. One can got to Bila Labut or Masarykovo nadrazi. Incidentally I have to make this choice every day and this app helps me.

 - **Technology stack**: The app is in Flask framework. Scrapping is done in Selenium. Everything is containizered via Dokcer. Testing and deploynment is done by Travis-CI. The app is hoste on Heroku free-tier.
 
 Please note that it takes some 30 seconds to wake up the app due to Heroku policy.

[![Build Status](https://travis-ci.org/QuarKUS7/which-tram.svg?branch=master)](https://travis-ci.org/QuarKUS7/which-tram)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
