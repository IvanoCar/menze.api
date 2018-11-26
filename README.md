# MenzeRi API

Web API devoloped for **MenzeRi project** - complete solution which enables students from the University of Rijeka, Croatia to view student restaurant menus in real-time.

It includes:

- **Desktop application** - Windows desktop application made with Electron and JS for restaurant management adopted completely to their business process - [Github repo](https://github.com/riverDeer12/menzeRi)

- **WebAPI**

- **Mobile application MenzeRi** - Android application for showing menus, among other functionality. 

  [zubi96](https://github.com/zubi96)

## API

API is built with Python and Flask microframework, MongoDB (mLab) is used for storage. Some additional work is required before deployment.

It also has some other functionalies which are not used in the MenzeRi mobile app, but will be used in **UniriApp**, another project under devolopment.

It is split into several modules:

- **dataport** module which contains routes for accepting weather data and notification data which will be sent as push notifications to mobile app users
- **get** module which contains routes for serving GET requests from the mobile apps
- **update** module which contains routes for serving POST requests from the desktop app
- **show** module which serves campus maps to mobile app users
- **utils** module

## TODO

- Limiting number of requests
- Improve auth
- Code optimization
- Implement news and job data
- (....)

