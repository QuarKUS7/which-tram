# which-tram

Simple web app that returns information to which tram stop one should go when leaving Florentinum in order to get to Letenske namesti. That is either Bila Labut or Masarykovo nadrazi.

 - **Technology stack**: The app is in Flask framewokr. Scrapping is done in Selenium. Everything is containizered via Dokcer. Testing and deploynment is done by Travis-CI. The app is hoste on Heroku free-tier.
 
 It takes some 30 seconds to wake up the app due to Heroku policy.

[![Build Status](https://travis-ci.org/QuarKUS7/which-tram.svg?branch=master)](https://travis-ci.org/QuarKUS7/which-tram)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
