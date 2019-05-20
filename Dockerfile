FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/html
ADD requirements.txt /var/www/html
RUN pip install mysqlclient

RUN apt-get update \
    && apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8\
    && apt-get install -y git\
    && apt-get install -y make\
    && apt-get install -y curl\
    && apt-get install -y build-essential\
    && apt-get install -y xz-utils\
    && apt-get install -y file\
    && apt-get install -y sudo\
    && apt-get install -y locales\
    && apt-get install -y locales-all\
    && apt-get install -y wget\
    && apt-get install -y swig\
    && apt-get install -y vim apache2 apache2-utils\
    && apt-get install -y libapache2-mod-wsgi-py3

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export LANG=ja_JP.UTF-8
ADD . /var/www/html
ADD ./my_site.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80 3500
CMD ["python", "/var/www/html/mysite/manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["apache2ctl", "-D", "FOREGROUND"]
#RUN cd /var/www/html/data
#RUN wget http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/data/20170201.tar.bz2
#RUN tar -xjvf 20170201.tar.bz2
#RUN rm -rf 20170201.tar.bz2