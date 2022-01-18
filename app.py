from flask import Flask

@app.route('/')
def hell():
    return "<h1>진리야 안녕, <br> 나랑 눈사람 만들래?<h1> \
    <br> <form action='login_page.php'> \
    <input type='button' value='나 웹 사이트 첨으로 띄워봤어!'/> </form>"


@app.route('/test')
def test():
    # 수행해야할 로직이 여기에 들어온다.
    return "<form action='login_page.php'> <input type='button' value='정다은 최고, 파이썬 꿀잼!! '/> </form>"

app = Flask(__name__)

if __name__ == '__main__':
    app.run("0.0.0.0",port =8080)

