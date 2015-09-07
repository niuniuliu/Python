#--encoding:utf-8--
import pycurl

url = "http://10.129.145.112:8081/jenkins/job/helloworld-freestyle/config.xml"

crl = pycurl.Curl()
crl.setopt(pycurl.VERBOSE,1)
crl.setopt(pycurl.FOLLOWLOCATION, 1)
crl.setopt(pycurl.MAXREDIRS, 5)
crl.setopt(pycurl.USERPWD, "peterguo:peterguo")
  
crl.setopt(pycurl.CONNECTTIMEOUT, 60)
crl.setopt(pycurl.TIMEOUT, 300)
crl.setopt(pycurl.HTTPPROXYTUNNEL,1)
crl.fp = StringIO.StringIO()
 
crl.setopt(pycurl.URL, url)
crl.setopt(crl.WRITEFUNCTION, crl.fp.write)
crl.perform()
ret = crl.fp.getvalue()
