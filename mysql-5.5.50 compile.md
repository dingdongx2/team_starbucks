- 운영체제: ubuntu 16.04 64비트 Server
- 아이피: 192.168.0.250


`sudo apt-get install ssh

sudo apt-get install vim cmake libncurses5-dev bison build-essential libreadline6-dev

sudo groupadd mysql
sudo useradd -g mysql mysql
sudo usermod -a -G www-data mysql

cd /tmp
wget https://github.com/mysql/mysql-server/archive/mysql-5.5.50.tar.gz
tar xfz mysql-5.5.50.tar.gz
mv mysql-server-mysql-5.5.50 mysql-5.5.50
cd mysql-5.5.50/

sudo cmake \
-DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci \
-DMYSQL_UNIX_ADDR=/run/mysqld/mysql.sock \
-DMYSQL_TCP_PORT=3306 \
-DSYSConFDIR=/etc/mysql \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_ARCHIVE_STORAGE_ENGINE=1 \
.

sudo make
make test
sudo make install

cd /usr/local/mysql
sudo chown -R mysql:mysql /usr/local/mysql
sudo ./scripts/mysql_install_db

sudo mkdir /etc/mysql
sudo cp support-files/my-medium.cnf /etc/mysql/my.cnf
sudo chown -R mysql:mysql /etc/mysql/

sudo mkdir /run/mysqld
sudo chown mysql:mysql /run/mysqld
sudo chown -R mysql:mysql /usr/local/mysql/
sudo bin/mysqld_safe &

sudo bin/mysql_secure_installation

- 1번째로 묻는건 현제 루트비밀번호 (처음 성치하면 그냥 엔터)
- 2번째로 묻는건 루트비밀번호를 지정하나? (y 누름)
  - 새로 지정할 루트비밀번호 입력
  - 그리고 확인용으로 재입력
- 익명계정을 삭제하나? (y누름)
- 외부에서 접속을 허락하지 않을것인가 (y누름)
=> 아니면 외부에서 접속가능
- 'test' 라는 데이터베이스를 삭제할것인가? (y누름)
- 테이블권한을 새로고침(?) 할것인가? (y누름)
- 끝

sudo cp support-files/mysql.server /etc/init.d/mysqld
sudo update-rc.d mysqld defaults
sudo ln -s /usr/local/mysql/bin/* /usr/local/bin/

sudo pkill mysql
sudo service mysql start

참고 사이트
http://m.todayhumor.co.kr/view.php?table=total&no=7450281
