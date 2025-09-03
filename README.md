# patient-appointment-backend
Repository for the Patient Appointment Network Data Application (PANDA) backend service.

## Overview
The PANDA service is currently in MVP stage and offers Create, Read, Update and Delete (CRUD) functionality for NHS patients.

In the near future, CRUD functionality for patient appointments will be added.

## Tech Stack
- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) for the Python backend API.
- 🧰 [SQLModel](https://sqlmodel.tiangolo.com) for the Python SQL database interactions.
- 🔍 [Pydantic](https://docs.pydantic.dev), used by FastAPI, for data validation.
- 💾 [PostgreSQL](https://www.postgresql.org) as the SQL database.
- 🐋 [Docker Compose](https://www.docker.com) for automated deployment.

## Deployment Instructions
### Preparation
- Make sure you have installed the following:
  - At least **v28.3.3** Docker
  - At least **v2.34.0** docker-compose
- The integration test script is a shell script so this will only work in linux environments.

### Step-by-step
- Create your own .env file in the root directory based off of .env.example
- Update the docker-compose files to refer to your .env file. (lines 10 & 23)
- Run the following command in your terminal:
```
docker compose up --build
```
- ⚠️Note: If you have PostgreSQL installed on your machine already, you may see and error relating to the port 5432 being already in use. You can find which process is using this port and kill it with the following commands. You will then need to run the above command again.

```
sudo lsof -i :5432
```

```
sudo kill **PID**
```

You should now see docker compose logging the build and creation process for the database and the backend containers.

You can now head to http://localhost:8000/docs to interact with the backend service via a handy UI.

**Tip**: checkout the *example-patients.json* file for some valid data.

As you interact, you should see the relevant database and backend logs in your terminal.

You can shutdown the service with the following command:
```
**Ctrl+C**
docker compose down
```

## Integration Test
There is a rudimentary Integration Test script in the root directory that tests the CRUD functionality for the /patients end-points. This will be improved in the future to handle more cases as they are implemented. It could also be refactored to use a Makefile instead of a shell script.

To run the Integration Test, simply run the following command:
```
bash run-integration-test.sh
```