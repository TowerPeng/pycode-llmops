from sqlalchemy.engine import make_url

url_string = "postgresql://postgres:postgre@127.0.0.1:5432/llmops?client_encoding=utf8"
try:
    url = make_url(url_string)
    print("解析成功:", url)
except Exception as e:
    print("解析失败:", e)