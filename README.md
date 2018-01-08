**Processo seletivo Reclame Aqui**

## NoSQL

Django does not have a great NoSQL support, so I'll implement a mid-tier service that receives raw complains and a worker that consumes this database and inserts it's data to django models.
I would never do this on a real product, unless its a required integration due to some legacy systems.