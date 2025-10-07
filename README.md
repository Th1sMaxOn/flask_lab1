# Flask Lab 1 — Template, Docker, Compose, Deploy

Базовий Flask-проєкт з двома ендпоінтами:
- `GET /healthcheck` → `{"status":"ok","service":"flask-lab1","time":"..."}`
- `GET /hello?name=Max` → `{"message":"Hello, Max!"}`

## 1) Запуск локально (без Docker)

> Потрібен Python 3.11+

```bash
python -m venv env
# Linux/macOS:
source env/bin/activate
# Windows PowerShell:
# .\env\Scripts\Activate.ps1

pip install -r requirements.txt
# Варіант 1: запустити через Flask CLI
set FLASK_APP=app.py  # Windows PowerShell: $env:FLASK_APP="app.py"
flask run -h 0.0.0.0 -p 8080

# Варіант 2: gunicorn (Linux/macOS)
# gunicorn -b 0.0.0.0:8080 app:app
```

Перевірка:
- http://127.0.0.1:8080/healthcheck
- http://127.0.0.1:8080/hello?name=World

## 2) Запуск в Docker

```bash
docker build -t flask-lab1:latest .
docker run --rm -p 8080:8080 -e PORT=8080 flask-lab1:latest
```

## 3) Запуск через Docker Compose

```bash
docker-compose build
docker-compose up
# Далі перевірити ті самі URL що вище
```

## 4) Тестування (Insomnia/Postman/cURL)

- В директорії `insomnia/` є експорт для Insomnia.
- cURL приклади:
```bash
curl http://127.0.0.1:8080/healthcheck
curl "http://127.0.0.1:8080/hello?name=Anya"
```

## 5) Деплой на Render.com (Web Service)

1. Створіть порожній GitHub репозиторій і завантажте цей код (див. **Git інструкції** нижче).
2. На https://render.com → **New** → **Web Service** → підключіть свій репозиторій.
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `flask --app app run -h 0.0.0.0 -p $PORT`
5. Region/Branch — за замовчуванням або як потрібно. Натисніть **Create Web Service**.
6. Після деплою відкрийте ваш сервісний URL і перевірте `/healthcheck` та `/hello`.

> Render встановлює змінну оточення `PORT` автоматично.

## 6) Git інструкції (структуровані коміти)

```bash
git init
git branch -M main
git add .
git commit -m "feat: init Flask template with /healthcheck and /hello"
git remote add origin <your-github-repo-url>
git push -u origin main

# Далі робіть окремі коміти за логікою змін, наприклад:
# git commit -m "docs: add README with local, docker and render steps"
# git commit -m "chore: add docker-compose for local dev"
```

---

### Структура
```
flask_lab1/
  ├─ .gitignore
  ├─ Dockerfile
  ├─ docker-compose.yml
  ├─ requirements.txt
  ├─ README.md
  ├─ app.py
  ├─ myapp/
  │   ├─ __init__.py
  │   └─ views.py
  └─ insomnia/
      └─ flask_lab1-insomnia.json
```

> Лабораторна покриває всі вимоги: Flask шаблон, `healthcheck`, Docker, docker-compose, деплой на Render, інструкції та приклади тестування.