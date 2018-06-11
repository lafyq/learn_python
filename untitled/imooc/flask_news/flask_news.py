from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request
from imooc.flask_news.forms import NewsForm



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8'  # 这是Python3的
db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    news_type = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(300))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    is_valid = db.Column(db.Boolean)


    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.query.all()
    return render_template("index.html", news_list=news_list)


@app.route('/cat/<name>/')
def cat(name):
    """ 新闻类别页面 """
    news_list = News.query.filter(News.news_type == name)
    # print(name)
    # print(news_list)
    return render_template('cat.html', name=name, news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻详情页 """
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 后台管理首页 """
    if page is None:
        page = 1
    page_data = News.query.filter_by(is_valid=1).paginate(page=page, per_page=5)
    return render_template("admin/index.html", page_data=page_data)


@app.route('/admin/add/', methods=['GET', 'POST'])
def add():
    """ 新增新闻 """
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        new_obj = News(
            title=form.title.data,
            content=form.content.data,
            news_type=form.news_type.data,
            img_url=form.img_url.data,
            created_at=datetime.now()
        )
        db.session.add(new_obj)
        db.session.commit()
    return render_template("admin/add.html", form=form  )


@app.route('/admin/update/<int:pk>/', methods=['GET', 'POST'])
def update(pk):
    """ 修改新闻 """
    news_obj = News.query.get(pk)
    if not news_obj:
        # TODO 此处应该有提示之后再重定向转跳
        return redirect(url_for('admin'))
    form = NewsForm(obj=news_obj)
    if form.validate_on_submit():
        # 获取数据
        news_obj.title = form.title.data
        news_obj.content = form.content.data
        news_obj.news_type = form.news_type.data
        news_obj.img_url = form.img_url.data

        # 保存数据
        db.session.add(news_obj)
        db.session.commit()

        # 重定向
        return redirect(url_for('admin'))

    return render_template("admin/update.html", form=form)


@app.route('/admin/delete/<int:pk>/', methods=['POST'])
def delete(pk):
    news_obj = News.query.get(pk)
    if not news_obj:
        return 'no'
    news_obj.is_valid = False
    db.session.add(news_obj)
    db.session.commit()
    return 'yes'

app.config['SECRET_KEY'] = 'a random string'
if __name__ == '__main__':
    app.run(debug=True)
