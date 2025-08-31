# As of time of writing, the below image contains vulnerabilities.
# In production, there would be an approved version available.

FROM python:3.12


WORKDIR /app


COPY /app /app


RUN pip install -r /app/requirements.txt


CMD ["fastapi", "run", "./main.py", "--port", "8000"]