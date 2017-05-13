# WordPress Plugin Vulnerability :: Like DiskLike Account
#### WordPress Plugin 중에서 게시글에 Like DisLike를 통한 게시물 선호도를 알아볼 수 있는 Plugin이다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-01.png)

우선 Like 버튼을 누르고 서버에 전송되는 패킷을 잡는다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-02.png)

패킷을 확인해보면 Like를 눌렀을 때 up_type=like, DisLike를 눌르면 up_type=dislike라고 표시된다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-03.png)

[Intercept is on]을 눌러 off 상태로 만들고 [HTTP history] 탭으로 이동한다.
HTTP history에서 서버에 전송했던 기록을 찾아 우 클릭 + Repeater를 눌러 이동한다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/likedislikeaccount-04.png)

HTTP history에서 서버에 전송했던 기록을 찾아 우 클릭 + Repeater를 눌러 이동한다.


![](https://github.com/dingdongx2/team_starbucks/blob/master/img/0001.png)
![](https://github.com/dingdongx2/team_starbucks/blob/master/img/0002.png)

Repeater에서 여러 코드들을 수정해서 전송해본 결과, post_id에서 "and 1=1"과 "and 1=2"를 통해 Blind SQL Injection이 발생함을 알 수 있었다.




