#-*-coding:UTF-8-*-
# 导入模块 urllib2
import urllib2

# 随便查询一篇文章，比如On random graph。对每一个查询google 
# scholar都有一个url，这个url形成的规则是要自己分析的。
query = 'On+random+graph'
url = 'http://scholar.google.com/scholar?hl=en&q=' + query + '&btnG=&as_sdt=1%2C5&as_sdtp='
# 设置头文件。抓取有些的网页不需要专门设置头文件，但是这里如果不设置的话，
# google会认为是机器人不允许访问。另外访问有些网站还有设置Cookie，这个会相对复杂一些，
# 这里暂时不提。关于怎么知道头文件该怎么写，一些插件可以看到你用的浏览器和网站交互的
# 头文件（这种工具很多浏览器是自带的），我用的是firefox的firebug插件。
header = {'Host': 'scholar.google.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:26.0) Gecko/20100101 Firefox/26.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate',
'Connection': 'keep-alive'}
# 建立连接请求，这时google的服务器返回页面信息给con这个变量，con是一个对象
req = urllib2.Request(url, headers = header) 
con = urllib2.urlopen( req )
# 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本
doc = con.read()
# 关闭连接。就像读完文件要关闭文件一样，如果不关闭有时可以、但有时会有问题，
# 所以作为一个守法的好公民，还是关闭连接好了。
con.close()