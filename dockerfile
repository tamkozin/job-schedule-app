# Dockerfile
FROM python:3.9-slim-buster

# 環境変数
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# WORKDIRディレクトリ
WORKDIR /app

# 必要なライブラリを先にコピーしてインストール
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt 

# アプリのソースをコピー
COPY . /app/

# ポート公開
EXPOSE 8000

# 開発用コマンド:runserver
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]