from flask import Flask
from simple_page.simple_page import simple_page
import os

app = Flask(__name__)
app.register_blueprint(simple_page)
# Blueprint can be registered many times
app.register_blueprint(simple_page, url_prefix='/pages')

if __name__=='__main__':
  port = int(os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
