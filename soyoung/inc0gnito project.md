# inc0gnito project



## 개요

1. 구성
   - __member__ : 박소영, 박여정, 조운삼
     __mento__ : 최우석
   - __project name__ : wordpress를 통한 chain attack 분석





## 진행

### 1주차. 환경설정

1. vmware 소프트웨어 설치
2. 가상머신 구성(우분투 데스크톱 버전)

###  ![Screen Shot 2017-04-09 at 5.21.40 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%205.21.40%20PM.png)

###  ![Screen Shot 2017-04-09 at 5.22.05 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%205.22.05%20PM.png)

3. 우분투 설치 ISO파일 구하기

4. 가상머신에 우분투 설치
   ![Screen Shot 2017-04-09 at 5.22.37 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%205.22.37%20PM.png)

   ![Screen Shot 2017-04-09 at 6.20.50 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%206.20.50%20PM.png)

   ![Screen Shot 2017-04-09 at 5.23.24 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%205.23.24%20PM.png) 

   ![Screen Shot 2017-04-09 at 5.24.15 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%205.24.15%20PM.png)

   ![Screen Shot 2017-04-09 at 7.10.02 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-09%20at%207.10.02%20PM.png)

   ![Screen Shot 2017-04-09 at 10.57.24 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen Shot 2017-04-09 at 10.57.24 PM.png)

   1차당황

   대처 : 일단 껐다 킨다

   ![Screen Shot 2017-04-09 at 11.13.46 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen Shot 2017-04-09 at 11.13.46 PM.png)

   ??

   아무튼 성공!

5. ping test

   ```sudo apt-get update && sudo apt-get install traceroute```

6. terminal launcher에 등록하기

   `ctrl+alt+t` : 터미널 실행

   ![Screen Shot 2017-04-10 at 4.59.54 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%204.59.54%20PM.png)

   Lock to Launcher 클릭

### 2주차. WORDPRESS 설치

1.  LAMP : Linux, Apache, MySQL, PHP 첫 글자를 가지고 와서 만들어진 용어이다. 설정된 리눅스 저장소 (repository)와 동기화한다.
    ```sudo apt-get update```
    AMP설치 : (LAMP 중 L 제외)
    ```sudo apt-get install -y apache2 php5 mysql-server mysql-client php5-mysql phpmyadmin vsftpd```

*  -y : 설치할 때 '설치하시겠습니까? yes/no'에서 미리 yes해준다.
*  설치할 list 중 하나라도 오타가 있다면 진행X
   * 혹시 이미 설치된 것이 있다면 그것 제외하고 설치가 된다
   * sudo 안쓰면 니가 수도냐고 물어본다 -.- 흥 

   ![Screen Shot 2017-04-10 at 7.36.19 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%207.36.19%20PM.png)

   <TUI(Terminal User Interface) 입력. 비밀번호 : soyoung 설정>

2. wordpress.org 접속
   ![Screen Shot 2017-04-10 at 7.40.47 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%207.40.47%20PM.png)

   <wordpress.com되면 주옥됩니다>

   ![Screen Shot 2017-04-10 at 7.41.48 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%207.41.48%20PM.png)

   <tar.gz 다운. 리눅스에서 사용할 것이기 때문이다. 큰 상관은 없다.>

   ![Screen Shot 2017-04-10 at 7.49.23 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%207.49.23%20PM.png)

   <다운 완료!>

   다운을 완료했으니, 압축을 해제하고 wordpress directory를 /var/www로 옮긴다.

   ```sudo mv wordpress/ /var/www/```

3. 아파치 설정
   아파치의 기본 directory는 ```/var/www/html```

   기본 경로를 해제한다

   ```sudo a2dissite 000-defaut.conf```

   available directory에 wordpress.conf 파일로 생성한다

   ```sudo vi /etc/apache2/sites-available/wordpress.conf```

   ```print
   <VirtualHost *:80>
   	ServerAdmin wordpress@localhost
   	ServerName wordpress.local
   	DocumentRoot /var/www/wordpress
   	<Directory /var/www/wordpress>
   		Options -Indexes
   		AllowOverride all
   		Order allow,deny
   		allow from all
   	</Directory>

   	LogLevel warn
   	ErrorLog /var/log/apache2/wordpress.local_error.log 
   	CustomLog /var/log/apache2/wordpress.local_access.log combined
   	ServerSignature Off
   </VirtualHost>
   ```

   wordpress.conf 설정을 활성화한다.

   ```sudo a2ensite wordpress.conf```

   아파치 서비스를 재시작하여 변동사항 저장한다.

   ```sudo service apache2 reload```

   이제 웹 서버에 접근하면.. (localhost에 접속)

   ![Screen Shot 2017-04-10 at 8.17.04 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%208.17.04%20PM.png)

   <web sevice main page changed>

4. 권한 설정
   아파치 전용 사용자 권한 설정

   ```sudo chown -R www-data:www-data /var/www/wordpress```

   디렉터리와 파일에 대해 서로 다른 권한 부여

   ```
   > sudo find /var/www/wordpress -type d -exec chmod 755 {} \;
   > sudo find /var/www/wordpress -type f -exec chmod 644 {} \;
   ```

5. 데이터베이스 생성

   ```mysql -u root -p```

   ```
   mysql -u root -p
   Enter password: (비밀번호 입력)
   mysql > create database wordpress;
   mysql > show databases;
   mysql > CREATE USER wordpress@localhost IDENTIFIED BY 'password';
   mysql > GRANT ALL PRIVILEGES ON wordpress.* TO wordpress@localhost;
   mysql > FLUSH PRIVILEGES;
   mysql > exit
   ```

6. 워드프레스 설치

   ![Screen Shot 2017-04-10 at 8.25.33 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%208.25.33%20PM.png)

   <OH한글등판OH>

   ![Screen Shot 2017-04-10 at 8.30.33 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%208.30.33%20PM.png)

   <설정값! 나중에 까먹을까봐.. 여기서 사용자명은 root로 변경>

   ![Screen Shot 2017-04-10 at 8.33.04 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-04-10%20at%208.33.04%20PM.png)

   <비밀번호는 박소영23!>

   ​

### 4주차. SQL injection이란?

URL요청, 웹 요청에 포함되는 파라미터 값에 SQL구문이나 시스템 명령을 삽입하는 형태의 공격.

웹 어플리케이션 뒤의 database에 query를 보내는 과정 사이에, 다른 구문을 삽입하여 공격자가 원하는 SQL 쿼리문을 실행하는 기법이다.

세가지 유형

/***

1) 인증 우회 (AB : Auth Bypass)

아이디와 패스워드를 입력하는 login 페이지를 타켓으로 하는 공격. SQL쿼리문의 True/False의 논리적 연산 오류를 이용, 로그인 인증 쿼리문이 무조건 True 결과값이 나오게 해서 인증을 무력화 시키는 방법이다.

ex) ID, password에 'or 1=1--'

2) 데이터 노출 (DD : Data Disclosure)



3) 원격명령 실행 (RCE : Remote Command Excute)

***/



SQL injection 공격의 종류

- Boolean-Based blind SQL injection
- Time-Based blind SQL injection
- Error-Based SQL injecion
- UNION query-based SQL injection
- Stacked queries SQL injection





1. Blind SQL injection

정의

- 서버에 악의적 쿼리를 날려서 참인 경우와 거짓인 경우의 반응 차이를 이용해 정보를 빼내는 기법

응용

- 아이디 찾기 할 때 아이디 존재 여부 확인
- 게시글을 검색할 때 검색 결과의 유무

방법

- 얻고 싶은 값의 n번째 byte code를 하나씩 찾는다 ![Screen Shot 2017-05-11 at 3.18.59 PM](https://github.com/dingdongx2/team_starbucks/blob/master/img/Screen%20Shot%202017-05-11%20at%203.18.59%20PM.png)

  <원리 : 이진탐색>


- N번째 글자를 비교하는 구문 작성
  ex) ascii (substr((<원하는 쿼리>), n,1)) < 64
  원하는 쿼리는 결과를 하나만 반환해야 한다
- 기존 구문과 결합
  ex) select * FROM users WHERE id = ‘(a’ and ascii(substr((<원하는 쿼리>), n, 1)) < 64#) and pw = ( );
  앞에서 배운 기초 SQL 인젝션 구문 응용
  뒷부분 필요 없는 것은 주석처리 해서 버림
- 이 과정을 계속 반복해서 글자들을 찾아 나간다





2. UNION based SQL injection

- UNION

  - 여러 쿼리의 결과값을 하나로 합치는 구문
  - Column 개수가 동일해야 한다
  - ex) 

  ```
  SELECT user, grade FROM student_01 UNION SELECT user, grade FROM student_02
  ```

- 정의
  UNION 구문을 이용해서 원래 나오는 값과 원하는 값을 합쳐서 출력하게 하는 공격 기법

- 가능한 시나리오
  게시판 검색에 SQL Injection 취약점이 있어서 게시물 목록 뒤에다가 원하는 값을 덧붙여서 나오도록 할 수 있다

- 특징
  원하는 문자열이 한꺼번에 나오기 때문에 속도가 빠르다
  Column 개수가 같아야 함 (SELECT 뒤에 아무 문자열이나 NULL 삽입)

- 예시

  ```
  SELECT title, name, date, username FROM board WHERE id
  < ( ) AND id >= ( );
  ```

  Student table에 있는 이름과 성적을 털고 싶다면

  ```
  ... id < (0 UNION SELECT name, grade, NULL, ‘1’ FROM student #) AND id >= (0);
  ```

  Column 개수를 맞추기 위해 임의의 문자열이나 NULL을 넣어 준다





3. Stacked queries SQL injection

- 정의
  세미클론(;)으로 구분된 여러 SQL쿼리를 실행시키는 기법

- 예시

  ```
  SELECT * FROM user WHERE id = (1, <원하는 쿼리>;)
  ```


​	
