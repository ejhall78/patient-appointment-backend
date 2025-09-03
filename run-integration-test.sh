#!/bin/bash

docker compose -f docker-compose.integration-test.yml up --build -d

while [[ "$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/health)" != "200" ]]; do
  echo "Waiting for a 200 response from the health endpoint..."
  sleep 2
done

curl -X 'POST' \
  'http://localhost:8000/patients/intergration-test' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "nhs_number": "1953262716",
  "name": "Dr Ian Hall",
  "date_of_birth": "1963-08-27",
  "postcode": "WA55 8HE"
}'

echo

sleep 1

docker compose down