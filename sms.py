[
  {
    "product": "netease",
    "desc": "网易短信验证码",
    "source": "https://github.com/isu5/xinghuiapp/commit/d599bcd1e90c4ad4b286ee8eddae18eb01d1c868",
    "auth": {
      "app_key": "d5275854a775369121a2e80536a5884b",
      "app_secret": "a3a5477f8b97"
    },
    "payloads": {
      "templateid": "3992639"
    },
    "weight": 10
  },
  {
    "product": "ucp",
    "desc": "云之讯",
    "source": "https://github.com/isu5/xinghuiapp/commit/d599bcd1e90c4ad4b286ee8eddae18eb01d1c868",
    "auth": {
      "app_id": "e540b654b48145249b36cd5cf715e6de",
      "sid": "f105a32dcd8bc368fffb4b2501c9c4ac",
      "token": "102ad7bc0b93cc89963ad5ff0c87077a"
    },
    "payloads": {
      "templateid": "310246",
      "params": "123456"
    }
  },
  {
    "product": "aliyun",
    "desc": "阿里云",
    "source": "https://github.com/reatent/che/blob/e47e73f4a8c23e0235bb5255942750791851c0fa/Application/Common/Conf/config.php",
    "auth": {
      "app_key": "LTAINwieuECXDOdk",
      "app_secret": "ye16iLTfcN5bxGDBBRd8lhydhTaBVF"
    },
    "payloads": {
      "template_code": "SMS_114035014",
      "sign_name": "哈弗养车",
      "template_params": {
        "code": "123456"
      }
    }
  },
  {
    "product": "ucp",
    "desc": "云之讯",
    "source": "https://github.com/mali1711/xianMaidang/blob/ac8847d68d1c14670ab8a92fdf2b23cc9cd848ba/application/config.php",
    "auth": {
      "app_id": "2c021c71e4a04741842f836df509b957",
      "sid": "594c1c503e4539df437ba99c235eb0ec",
      "token": "eb78c6b89891c71f8769ce7909c39a25"
    },
    "payloads": {
      "templateid": "277877",
      "params": "123456"
    }
  },
  {
    "product": "ucp",
    "desc": "云之讯",
    "source": "https://github.com/SavorGit/savor_api/blob/25d7ea62fc4487f7c7a655270e298de99e549c60/Application/Common/Conf/config.php#L178-L183",
    "auth": {
      "app_id": "a982fdb55a2441899f2eaa64640477c0",
      "sid": "6a929755afeded257916ca68518ec1c3",
      "token": "66edd50a46c882a7f4231186c44416d8"
    },
    "payloads": {
      "templateid": "178978",
      "params": "123456"
    }
  },
  {
    "product": "aliyun",
    "desc": "阿里云",
    "source": "https://github.com/Magic-Bing/xk/blob/15cea7bc83f89a14698516c916fc49d31732131c/Application/Common/Conf/config.php#L91-L95",
    "auth": {
      "app_key": "LTAIm5O6hgHs2Jdh",
      "app_secret": "rW0AsJlM8N9E7StxjyZAx4cg9k9piV"
    },
    "payloads": {
      "template_code": "SMS_115750019",
      "sign_name": "云销控",
      "template_params": {
        "code": "123456"
      }
    }
  },
  {
    "product": "aliyun",
    "desc": "阿里云",
    "source": "https://github.com/suiyiyou-rour/syy/blob/07964ed6c9cfb19a015bfe3b85401f1f9bc0b388/application/config.php",
    "auth": {
      "app_key": "LTAI4tfw5qzG499J",
      "app_secret": "F3zIzdabHuUpVGH6XVBLg8EvUyWB89"
    },
    "payloads": {
      "template_code": "SMS_109705432",
      "sign_name": "随意游网络",
      "template_params": {
        "code": "123456"
      }
    }
  },
  {
    "product": "smsbao",
    "desc": "短信宝,支持自定义消息体",
    "source": "https://github.com/SuperNodeLibs/wallet/blob/70257645d4758e5950842a9de8a59fd80a881776/application/config.php",
    "api": "http://api.smsbao.com/sms",
    "auth": {
      "username": "ukengame",
      "password": "youtui2017"
    },
    "enable_custom_msg": true
  },
  {
    "product": "yunpian",
    "desc": "云片短信",
    "source": "https://github.com/xinyuanmmx/hpshop/blob/5f298d1ac9b29cdb5fb02bf988f1578dc99f4a5c/application/libraries/yunpian-sdk-php/config.php",
    "api": "https://sms.yunpian.com/v2/sms/single_send.json",
    "auth": {
      "api_key": "cdfc9e5bf8d05c5ea8cc940b38a75961",
      "api_secret": "1c2d8640"
    }
  },
  {
    "product": "normal",
    "desc": "不知名的短信",
    "api": "https://dx.ipyy.net/smsJson.aspx?action=send&userid=&account=AA00344&password=AA0034452&content=%E3%80%90%E4%BB%80%E4%B9%88%E3%80%91123",
    "source": "https://github.com/hou1202/zhe/blob/dfc059bdb11a993657b4b0393a32ca4c738bc4e4/application/index/controller/Convert.php#L24",
    "method": "GET",
    "payloads": {
      "text": "【折金券】您的验证码为：123456，请在10分钟内完成验证",
      "mobile": "{{mobile}}",
      "sign_name": ""
    }
  },
  {
    "product": "normal",
    "desc": "不知名的短信",
    "api": "http://pi.noc.cn/SendSMS.aspx",
    "source": "https://github.com/gywl/bms/blob/2d0b3c82959b897f46b499c0f10eb6424fee99b8/application/common/config.php#L18-L21",
    "method": "POST",
    "auth": {
      "ececcid": "101003005",
      "password": "yuanmeng2013"
    },
    "payloads": {
      "msisdn": "{{mobile}}",
      "smscontent": "{{content}}",
      "msgtype": 5,
      "longcode": ""
    }
  },
  {
    "product": "tencent",
    "desc": "腾讯云短信不支持自定义消息,必须有模版tpl_content和模版参数tpl_params才可以发送消息",
    "api": "https://yun.tim.qq.com/v5/tlssmssvr/sendsms",
    "source": "https://github.com/snowonbridge/cms/blob/880e8151e8fff2efae2f8d9e3cdf4c78d1d183b5/application/config.php#L368-L371",
    "method": "POST",
    "tpl_content": "尊敬的灵游测试玩家，{1}为您的短信验证码，请于{2}秒内填写。如非本人操作，请忽略本短信。",
    "tpl_params": [
      "123456",
      "30"
    ],
    "auth": {
      "app_id": "1400013341",
      "app_secret": "92fc8ef260d2699e4b52a79057282a22"
    }
  },
  {
    "product": "netease",
    "desc": "网易短信验证码",
    "source": "https://github.com/diaoyudao/mrkshop/blob/8ccddec42a2bbfdd3ac7562ea396988492693005/Application/Common/Conf/config.php#L74-L78",
    "auth": {
      "app_key": "0c6ab52108e0596417f596f05e7ae013",
      "app_secret": "02184da78572"
    }
  },
  {
    "product": "cl253",
    "desc": "创蓝253",
    "api": "http://smssh1.253.com/msg/send/json",
    "source": "https://github.com/aichesong/aice/blob/4f8c8dec29ed56cbf0610f050444df351642709b/application/api/config.php#L13-L17",
    "method": "POST",
    "auth": {
      "account": "N3300103",
      "password": "JWi7jpcZ3"
    },
    "enable_custom_msg": true
  },
  {
    "product": "cl253",
    "desc": "创蓝253",
    "api": "http://smssh1.253.com/msg/send/json",
    "source": "https://github.com/doushen11/luntan/blob/e420cb1226b4f67134b4ce8f6a71883c1d45d242/application/config/config.php#L542-L544",
    "method": "POST",
    "auth": {
      "account": "N4625148",
      "password": "ySBCfmMDjXbdeb"
    },
    "enable_custom_msg": true
  },
  {
    "product": "yunpian",
    "desc": "云片短信",
    "source": "https://github.com/xinyuanmmx/ci_base/blob/810b419d336108338fc1634bede647d1b9c3e4b3/application/libraries/yunpian-sdk-php/config.php",
    "api": "https://sms.yunpian.com/v2/sms/single_send.json",
    "auth": {
      "api_key": "cdfc9e5bf8d05c5ea8cc940b38a75961",
      "api_secret": "1c2d8640"
    }
  },
  {
    "product": "miaodi",
    "desc": "秒滴云",
    "source": "https://github.com/gaoshusen/gaoshusen/blob/6221f850f9af0f55f971c38134e1c1f9569a8575/Application/Conf/Api/config.php#L9-L11",
    "api": "https://api.miaodiyun.com/20150822/industrySMS/sendSMS",
    "auth": {
      "sid": "6ce883ce6eb044ce873775c9be8d805b",
      "token": "17abc178cc6b41949dbfb4e66d22734a"
    }
  },
  {
    "product": "juhe",
    "desc": "聚合服务",
    "source": "https://github.com/baobeiboboda/efan_admin/blob/4a2c6018e0dfce4de4c52ca72fc9acb96a23f4ab/Application/Common/Conf/config.php",
    "api": "http://v.juhe.cn/sms/send",
    "auth": {
      "key": "f755c0e9e5862251e09ec9d5555328eb"
    },
    "payloads": {
      "key": "f755c0e9e5862251e09ec9d5555328eb",
      "tpl_id": "9642",
      "tpl_value": "#code#=1234&#name#=&#operate#="
    }
  },
  {
    "product": "normal",
    "desc": "助通科技",
    "source": "https://github.com/XiangYu0777/.io.zfjd.com/blob/3f33af99eb7188185eb0926b34c1c382d215b033/Application/Common/Conf/config.php",
    "api": "http://www.ztsms.cn:8800/sendSms.do",
    "method": "GET",
    "auth": {
      "username": "zysd",
      "password": "VomAacEl",
      "productid": "887362"
    },
    "payloads": {
      "mobile": "{{mobile}}",
      "content": "{{content}}"
    }
  },
  {
    "product": "luosimao",
    "desc": "螺丝帽",
    "source": "https://github.com/zjuandroid/aquarium/blob/daa96f66fea58cf810e4ef9e4f2ac829319ef956/Application/Common/Conf/config.php#L20-L21",
    "api": "http://sms-api.luosimao.com/v1/send.json",
    "method": "POST",
    "auth": {
      "key": "eb2323adc7bb33eab35a4d4f9843f425"
    },
    "payloads": {
      "message": "验证码：123456，三分钟内有效。【吉印水族科技】"
    }
  }
]
 
