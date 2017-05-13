# WordPress Plugin Vulnerability :: Like DiskLike Account
#### WordPress Plugin 중에서 게시글에 Like DisLike를 통한 게시물 선호도를 알아볼 수 있는 Plugin이다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-01.png)  

우선 Like 버튼을 누르고 서버에 전송되는 패킷을 잡는다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-02.png)  

패킷을 확인해보면 Like를 눌렀을 때 up_type=like, DisLike를 눌르면 up_type=dislike라고 표시된다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-03.png)  

[Intercept is on]을 눌러 off 상태로 만들고 [HTTP history] 탭으로 이동한다.  
HTTP history에서 서버에 전송했던 기록을 찾아 우 클릭 + Repeater를 눌러 이동한다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/0001.png)  
![](https://github.com/dingdongx2/team_starbucks/blob/master/img/0002.png)  

Repeater에서 여러 코드들을 수정해서 전송해본 결과, post_id에서 "and 1=1"과 "and 1=2"를 통해 Blind SQL Injection이 발생함을 알 수 있었다.  

![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-05.png)  
Repeater에 보냈던 기록을 Intruder로 보낸다. (우 클릭 + Intruder)  
Intruder 탭에서 하위 Positions 탭으로 이동하면 Request 코드가 들어가 있을 것이다. 옆에 Clear 버튼을 통해 변수 처리 된 모든 설정을 해제한다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-06.png)  
post_id=31 뒤에 "and substring(database(), §§, 1)=char(§§)"를 추가로 작성한다.  
Attack type은 Cluster bomb으로 설정해준다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-07.png)  
[Payloads]탭으로 이동하여 다음과 같이 설정해 준다.  
“첫 번째” 페이로드를 “숫자”의 형태로 1~13까지 1씩 증가시키며 대입한다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-08.png) 
“2 번째” 페이로드를 “숫자”의 형태로 32~126까지 1씩 증가시키며 대입한다.  


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-09.png)  
Option 탭에서 response 값이 1인 결과만 표시할 수 있도록 grep 옵션에 추가한다.  

substring(database(), §§, 1)=char(§§)에서 1번째 Payload는 앞의 §§에 들어갈 값이고, 2번째 Payload는 뒤의 §§에 들어갈 값이다.  
따라서, 1에서 13자리까지 중에 ASCII 코드로 32에서 126까지 값들을 하나하나 대입하는 Brute Force를 수행하는 과정이다.  

![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-10.png)  
Start Attack 버튼을 누르면 설정했던 값들에 의해 동작된다. 동작이 완료된 다음에 나타나는 화면에 각 Payload 값에 따른 표시들이 나타나도 거기에 Option에 넣어 줬던 1에 대한 결과도 함께 표시된다.  
대/소문자를 구별하지 않기 때문에 각 자리별로 일치하는 ASCII값이 2개가 되고, 각 값을 다시 문자로 치환하면 DB 이름인 wordpress를 추출할 수 있다.  
