# -*- coding: utf-8 -*-
from LianJiaSpider import *


def do_xiaoqu_spider1(region=u"昌平"):
    """
    爬取大区域中的所有小区信息
    """
    url = u"http://bj.lianjia.com/xiaoqu/rs" + region + "/"
    try:
        req = urllib2.Request(url, headers=hds[random.randint(0, len(hds) - 1)])
        source_code = urllib2.urlopen(req, timeout=5).read()
        plain_text = unicode(source_code)  # ,errors='ignore')
        soup = BeautifulSoup(plain_text, "html.parser")
    except (urllib2.HTTPError, urllib2.URLError), e:
        print e
        return
    except Exception, e:
        print e
        return
    d = "d=" + soup.find('div', {'class': 'page-box house-lst-page-box'}).get('page-data')
    exec (d)
    print d
    total_pages = d['totalPage']

    threads = []
    print u"爬下了 %s 区全部的小区信息" % region


get_region_link()