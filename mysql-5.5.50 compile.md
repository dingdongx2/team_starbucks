- 운영체제: ubuntu 16.04 64비트 Server
- 아이피: 192.168.0.250

서버 버전은 복사 붙여넣기가 어려워 ssh를 설치하고, putty와 같은 원격 접속을 이용하여 이 문제를 해결
```
sudo apt-get install ssh
```
MySQL을 컴파일할 때 필요한 도구들
```
sudo apt-get install vim cmake libncurses5-dev bison build-essential libreadline6-dev
```
mysql 사용자와 그룹을 생성
```
sudo groupadd mysql
sudo useradd -g mysql mysql
sudo usermod -a -G www-data mysql
```
mysql 5.5.50 버전을 다운로드
```
cd /tmp
wget https://github.com/mysql/mysql-server/archive/mysql-5.5.50.tar.gz
tar xfz mysql-5.5.50.tar.gz
mv mysql-server-mysql-5.5.50 mysql-5.5.50
cd mysql-5.5.50/
```
마지막의 . 까지 포함하여 한번에 복사 붙여넣기하여 다운로드한 mysql 5.5.50을 설치
```
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
```
컴파일 시작
```
sudo make
make test
sudo make install
```
각 디렉터리를 mysql 사용자로 권한 설정 및 데이터베이스 설정
```
cd /usr/local/mysql
sudo chown -R mysql:mysql /usr/local/mysql
sudo ./scripts/mysql_install_db
sudo mkdir /etc/mysql
sudo cp support-files/my-medium.cnf /etc/mysql/my.cnf
sudo chown -R mysql:mysql /etc/mysql/
sudo mkdir /run/mysqld
sudo chown mysql:mysql /run/mysqld
sudo chown -R mysql:mysql /usr/local/mysql/
```
mysql 서비스 시작, 시작되면 엔터를 누르고 쉘로 복귀
```
sudo bin/mysqld_safe &
```
mysql 데이터베이스 기본 설정
```
sudo bin/mysql_secure_installation
```
위 설정의 질문 요약
- 1. 설정된 MySQL 루트 비밀번호? (처음 성치하면 그냥 엔터)
- 2. 루트 비밀번호 지정? (y 누름)
  - 새로 지정할 루트 비밀번호 입력
  - 비밀번호 재입력
- 3. 익명계정을 삭제? (y누름)
- 4. 외부에서 접속 허가 여부 (y누름) => n 이면 외부에서 접속가능
- 5. 'test' 데이터베이스 삭제? (y누름)
- 6. 테이블권한을 새로고침? (y누름)

mysql 도구들을 언제든지 사용할 수 있게 설정
```
sudo cp support-files/mysql.server /etc/init.d/mysqld
sudo update-rc.d mysqld defaults
sudo ln -s /usr/local/mysql/bin/* /usr/local/bin/
```
기존에 실행한 mysql 서비스 종료 후 일반적인 방법으로 재시작
```
sudo pkill mysql
sudo service mysql start
```
참고 사이트
- http://m.todayhumor.co.kr/view.php?table=total&no=7450281
