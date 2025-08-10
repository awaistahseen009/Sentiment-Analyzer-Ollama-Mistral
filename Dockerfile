FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY frontend ./frontend
COPY start.sh ./start.sh
RUN chmod +x start.sh

EXPOSE 8000 8501

CMD ["./start.sh"] 