# EnglishService

Microservice for English exam questions for Grade 9-12 students. Part of the **ExamPlatform** suite.

## Tech Stack

- **Language**: Python 3.9
- **Framework**: Django 3.2.12 + Django REST Framework
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Container**: Docker

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/english/health/` | Health check |
| GET | `/api/english/questions/grade/{grade}/top/{n}/` | Top N questions for a grade |
| GET | `/api/english/questions/topic/{topic}/count/{n}/` | N questions by topic |
| GET | `/api/english/questions/complexity/{complexity}/count/{n}/` | N questions by complexity |
| GET | `/api/english/questions/grade/{grade}/topic/{topic}/count/{n}/` | N questions by grade + topic |
| GET | `/api/english/topics/` | List all available topics |
| GET | `/api/english/stats/` | Question bank statistics |

## Supported Topics

- Grammar
- Literature
- Writing
- Poetry
- Vocabulary
- Reading Comprehension
- Rhetoric

## Complexity Levels

- `easy` — 1 mark
- `medium` — 2 marks
- `hard` — 3 marks

## Running Locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8084
```

Service starts on port **8084**.

### Example Requests

```bash
# Top 5 questions for Grade 11
curl http://localhost:8084/api/english/questions/grade/11/top/5/

# 3 Grammar questions
curl http://localhost:8084/api/english/questions/topic/Grammar/count/3/

# 4 hard questions
curl http://localhost:8084/api/english/questions/complexity/hard/count/4/
```

## Docker

```bash
docker build -t english-service:1.0.0 .
docker run -p 8084:8084 english-service:1.0.0
```
