https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET

orBE2Js9tyI6DeU3hdotXUvbTS8xEPrHfbs56aXbjSqsa5HSkRmXqtczzrsKDsZ-Q16zglJSxkysdoC8e2oPw00TEJSDc-8-QhjzuJ-lLkELSAjAFAYFN

curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' -XPOST -d '{"button": [{"name": "加盟申请", "sub_button": [], "url": "http://coupon.ktvsky.com/ktv_bar", "type": "view"}, {"name": "录音列表", "sub_button": [], "url": "http://k.ktvsky.com/bar/userinfo/new", "type": "view"}, {"name": "用户反馈", "type": "view", "url": "http://static.ktvsky.com/wow/feedback.html"}]}' 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=S8KuNnxExNbwpFntw10j78mRn64ujfgw86mtOJYmhz1NBN4XuPltxpKEPjAEKqvvS4YscHSQnaJLy505cxpIVty-z-ff2mCip8srFQ4v1SL_DN1hvFFolophTXpfyM-_MSCeAEAZFP'
curl -i -H 'Accept: application/json' -H 'Content-Type: application/json' -XPOST -d '{"button": [{"name": "加盟申请", "sub_button": [], "url": "http://coupon.ktvsky.com/ktv_bar", "type": "view"}, {"name": "用户反馈", "type": "view", "url": "http://wx.handle.ktvdaren.com/song_new/nextpage/feedback.html?uid=9e9183fd41ee5663935b96fed2bf54d6"}]}' 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=orBE2Js9tyI6DeU3hdotXUvbTS8xEPrHfbs56aXbjSqsa5HSkRmXqtczzrsKDsZ-Q16zglJSxkysdoC8e2oPw00TEJSDc-8-QhjzuJ-lLkELSAjAFAYFN'

#调用common获取access_cotke(wow)
curl -s 'http://gm.ktvsky.3231266f50027675yg.custom.ucloud.cn/open/wx/token?secret=b649fa6fe892817e501c1e564dcd6b5b&appid=wx07e7e13d46a5c6fb'
