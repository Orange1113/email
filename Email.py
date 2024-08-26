from flask import Flask, request
import resend
from datetime import datetime

from gevent import pywsgi

app = Flask(__name__)

resend.api_key = "re_d1E6682s_AhrQwGtkwcLusi3JrscRLmZQ"


@app.route('/', methods=['POST'])
def send_email():
    # 获取要发送的邮箱地址
    to_email = request.json.get('to')
    if not to_email:
        return "Missing 'to' parameter", 400

    # 构建 HTML 内容（这里使用一个简单的默认内容示例，实际应用中你可能需要根据需求动态生成）
    date = datetime.now().strftime('%Y 年 %m 月 %d 日')
    html = """
    <style>
    .success-message {
        font-family: sans-serif;
        text-align: center;
        padding: 50px;
    }

    h1 {
        color: #4CAF50;
    }

    p {
        color: #666;
        font-size: 18px;
    }

    .icon {
        font-size: 48px;
        color: #4CAF50;
    }

    .credit {
          text-align: right;
    }
    </style>

    <!-- 成功图标 -->
    <div class="success-message">
    <span class="icon">&#10004;</span>
    <h1>感谢您的建议！</h1>
    <p>您的建议已成功提交，我们会尽快进行处理。</p>
    <p>如果有进一步的需要，我们可能会与您联系。</p>
    <!-- 署名和日期 -->
    <div class="credit">有想法的橙子<br>%s</div>
    </div>
    """ % date

    params: resend.Emails.SendParams = {
        "from": "有想法的橙子 <report@ooorange.top>",
        "to": to_email,
        "subject": "建议提交成功",
        "html": html
    }

    email = resend.Emails.send(params)
    return "Email sent successfully", 200


@app.route('/demo')
def demo():
    return "Hello, World!"
