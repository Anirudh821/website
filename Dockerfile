FROM  python:3.12-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install --no-cache-dir -r requirments.tcxt 
COPY . .
EXPOSE 8501
CMD [ "streamlit" ,"run", "index.py", "--server.port=8501", "--server.address=0.0.0.0" ]