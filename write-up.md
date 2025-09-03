# patient-appointment-backend write up

## Overview
This is a document containing some of my thoughts and considerations about this technical exercise.

### My thoughts
I really enjoyed this task. I used it as an opportunity to learn more about using FastAPI and SQLModel together as they are from the same creator. They integrate very nicely and have some fantastic features leading to some very simple and clean code.

There is a lot of scope for improvement of various things but since the brief mentioned that the client wanted something working quickly, I am happy with where I've left the code.

For next steps, the first priority would be to add appointment funtionality and have a relation in the database between patients and appointments. Implementing thorough unit tests involving mocks would also be high on the list. Some refactoring would be nice, such as creating a repository service for interacting with the database as more functionality is required there. Finally, having an end-to-end test involving the frontend would be extremely valuable and necessary before deployment to production but this would obviously depend on the frontend being ready.

## Tech choices and considerations
### FastAPI & SQLModel
As mentioned, these integrate nicely with each other. There is also excellent documentation on both so future developers on the project would benefit from this. It also does cater for database migrations through [Alembic](https://alembic.sqlalchemy.org/en/latest/) which is good. From my understanding, if more complex database interactions were in scope for the future, one can use SQLAlchemy code with SQLModel since that's what SQLModel is based on.

### PostgreSQL
In PostgreSQL I chose a simple open source database that is widely used and I was familiar with. As mentioned, SQLModel caters for database migrations so if a change was needed, it would be possible.

### Other considerations
- I chose to go with a simple requirements.txt file for managing dependencies in order to keep things simple in this regard. I also looked into using [uv](https://github.com/astral-sh/uv) and [poetry](https://python-poetry.org/) which seem like great options.
- Docker and docker-compose were fantastic for developer experience. Having the backend containerised also gives the possibility of deploying anywhere down the line, for example in Kubernetes.
- I found a library for the NHS Number checksum validation called [nhs_number](https://uk-fci.github.io/nhs-number/). I went with this instead of hand-rolling my own checksum as I felt this would mimick a real production service by using a centrally maintained library.
- In a similar vein, I found some postcode validation libraries but wanted to use Test Driven Development (TDD) to create a simple util with some unit tests.
- The use of a .env file is not particularly ideal - especially for production deployments. However it works well in this setting due to it's simplicity. With a developed CI/CD pipeline, you could store secrets in GitHub secrets and inject them in during the pipeline. Or, if for example the application was running in Kubernetes or similar in the cloud, you could set the cluster/namespace to pull secrets from a cloud based secrets management service and have them directly available to the container.

### My development thought process
I wanted to write up some notes on how I went about building this project for future reference. This can also be inferred from the commit history.

I wanted to start off by getting everything connected and running properly so I could iterate and add features and functionality in a step-by-step manner - validating everything along the way.

Once I had a good base of a backend service talking to a database, all deployed via docker compose, I began implementing the api routes and CRUD functionality. Having a database set up early was fantastic for validating that the code was functioning as desired and drastically reduced errors along the way. 

Ideally I would have implemented these in a TDD manner but since this can take slightly longer, and the brief mentioned getting a working prototype up ASAP, I used the method of interacting with the db to check my work. I also incorporated some TDD by creating a simple postcode verifier and formatter to showcase this development style. 

Finally, the brief also mentioned that the client highly valued automated tests so even though there was no frontend available to run full end-to-end tests with, I created a simple script that starts everything up, and uses an /integration-test endpoint and does a full CRUD test. I wanted to make sure this endpoint wasn't available at all times so I included a simple check based on an ENVIRONMENT variable that only made it available if set to 'integration-test'. This was achieved with a secondary docker compose file specifically for integration tests. Something more sophisticated like a Makefile, docker compose overrides and a proper test harness would be an obvious improvement and something I would plan to implement sooner rather than later in the project lifecycle.