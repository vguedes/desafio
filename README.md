**Processo seletivo Reclame Aqui**

## NoSQL

Django does not have a great NoSQL support, so I'll implement a mid-tier service that receives raw complains and a worker that consumes this database and inserts it's data to django models.
I would never do this on a real product, unless its a required integration due to some legacy systems.


### Models

## Locale
This models does not make much sense since the locale will have a city for its FK, So I can link the Complain directly to the city.
The City model has a Fk to State, that has a FK to Country, so, we can navigate through and filter objects easilly.