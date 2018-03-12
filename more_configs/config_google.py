# coding=utf-8
# 这是为Google和中文维基(无缝整合)镜像配置的示例配置文件
#
# 使用方法:
#   1. 复制本文件到 zmirror 根目录(wsgi.py所在目录), 并重命名为 config.py
#   2. 修改 my_host_name 为你自己的域名
#
# 各项设置选项的详细介绍请看 config_default.py 中对应的部分
# 本配置文件假定你的服务器本身在墙外
# 如果服务器本身在墙内(或者在本地环境下测试, 请修改`Proxy Settings`中的设置
#
# 由于google搜索结果经常会出现中文维基, 所以顺便把它也加入了.
# google跟中文维基之间使用了本程序的镜像隔离功能, 可以保证中文维基站的正常使用
#
# 本配置文件试图还原出一个功能完整的google.
#   但是由于程序本身所限, 还是不能[完整]镜像过来整个[google站群]
#   在后续版本会不断增加可用的网站
#
# 以下google服务完全可用:
#   google网页搜索/学术/图片/新闻/图书/视频(搜索)/财经/APP搜索/翻译/网页快照/...
#   google搜索与中文维基百科无缝结合
# 以下服务部分可用:
#     gg地图(地图可看, 左边栏显示不正常)/G+(不能登录)
# 以下服务暂不可用(因为目前无法解决登录的问题):
#     所有需要登录的东西, docs之类的
#

# Github: https://github.com/aploium/zmirror

# ############## Local Domain Settings ##############
my_host_name = '127.0.0.1'
my_host_scheme = 'http://'
my_host_port = None  # None表示使用默认端口, 可以设置成非标准端口, 比如 81

# ############## Target Domain Settings ##############
target_domain = 'www.google.com.hk'
target_scheme = 'https://'

# 这里面大部分域名都是通过 `enable_automatic_domains_whitelist` 自动采集的, 我只是把它们复制黏贴到了这里
# 实际镜像一个新的站时, 手动只需要添加很少的几个域名就可以了.
# 自动采集(如果开启的话)会不断告诉你新域名
external_domains = (
    'www.google.com',
    'webcache.googleusercontent.com',  # Google网页快照
    'images.google.com.hk',
    'images.google.com',
    'apis.google.com',

    # Google学术
    'scholar.google.com.hk',
    'scholar.google.com',

    # 中文维基百科
    'zh.wikipedia.org',
    'zh.m.wikipedia.org',
    'upload.wikipedia.org',
    'meta.wikimedia.org',
    'login.wikimedia.org',

    # Google静态资源域名
    'ssl.gstatic.com',
    'www.gstatic.com',
    'encrypted-tbn0.gstatic.com',
    'encrypted-tbn1.gstatic.com',
    'encrypted-tbn2.gstatic.com',
    'encrypted-tbn3.gstatic.com',
    'csi.gstatic.com',
    'fonts.googleapis.com',

    # Google登陆支持
    'accounts.google.com',
    'accounts.youtube.com',
    'accounts.google.com.hk',
    'myaccount.google.com',
    'myaccount.google.com.hk',

    'ajax.googleapis.com',
    'translate.google.com',
    'translate.google.com.hk',
    'video.google.com.hk',
    'books.google.com',
    'cloud.google.com',
    'analytics.google.com',
    'security.google.com',
    'investor.google.com',
    'families.google.com',
    'clients1.google.com',
    'clients2.google.com',
    'clients3.google.com',
    'clients4.google.com',
    'clients5.google.com',
    'talkgadget.google.com',
    'news.google.com.hk',
    'news.google.com',
    'support.google.com',
    'docs.google.com',
    'books.google.com.hk',
    'chrome.google.com',
    'profiles.google.com',
    'feedburner.google.com',
    'cse.google.com',
    'sites.google.com',
    'productforums.google.com',
    'encrypted.google.com',
    'm.google.com',
    'research.google.com',
    'maps.google.com.hk',
    'hangouts.google.com',
    'developers.google.com',
    'get.google.com',
    'afp.google.com',
    'groups.google.com',
    'payments.google.com',
    'photos.google.com',
    'play.google.com',
    'mail.google.com',
    'code.google.com',
    'tools.google.com',
    'drive.google.com',
    'script.google.com',
    'goto.google.com',
    'calendar.google.com',
    'wallet.google.com',
    'privacy.google.com',
    'ipv4.google.com',
    'video.google.com',
    'store.google.com',
    'fi.google.com',
    'apps.google.com',
    'events.google.com',
    'notifications.google.com',
    'plus.google.com',
    'dl.google.com',
    'manifest.googlevideo.com',
    'storage.googleapis.com',

    'gg.google.com',

    'scholar.googleusercontent.com',
    'translate.googleusercontent.com',
    't0.gstatic.com',
    't1.gstatic.com',
    't2.gstatic.com',
    't3.gstatic.com',
    's-v6exp1-ds.metric.gstatic.com',
    'ci4.googleusercontent.com',
    'gp3.googleusercontent.com',
    'accounts.gstatic.com',

    # For Google Map (optional)
    'maps-api-ssl.google.com',
    'maps.gstatic.com',
    'maps.google.com',
    'fonts.gstatic.com',
    'lh1.googleusercontent.com',
    'lh2.googleusercontent.com',
    'lh3.googleusercontent.com',
    'lh4.googleusercontent.com',
    'lh5.googleusercontent.com',
    'lh6.googleusercontent.com',

    # 'upload.wikimedia.org',
    'id.google.com.hk',
    'id.google.com',

    # misc
    'inputtools.google.com',
    'inbox.google.com',
    '-v6exp3-v4.metric.gstatic.com',
    '-v6exp3-ds.metric.gstatic.com',
    'if-v6exp3-v4.metric.gstatic.com',
    'public.talk.google.com',
    'ie.talkgadget.google.com',
    'client-channel.google.com',
    'maps.googleapis.com',
    'people-pa.clients6.google.com',
    'myphonenumbers-pa.googleapis.com',
    'clients6.google.com',
    'staging.talkgadget.google.com',
    'preprod.hangouts.sandbox.google.com',
    'dev-hangoutssearch-pa-googleapis.sandbox.google.com',
    'picasaweb.google.com',
    'schemas.google.com',
    'contact.talk.google.com',
    'groupchat.google.com',
    'friendconnectchat.google.com',
    'muvc.google.com',
    'bot.talk.google.com',
    'prom.corp.google.com',
    'stun.l.google.com',
    'stun1.l.google.com',
    'stun2.l.google.com',
    'stun3.l.google.com',
    'stun4.l.google.com',
    'onetoday.google.com',
    'plus.googleapis.com',
    'youtube.googleapis.com',
    'picasa.google.com',
    "www-onepick-opensocial.googleusercontent.com",

    'plus.sandbox.google.com',

    # gmail misc
    'gmail.com',
    'www.gmail.com',
    'chatenabled.mail.google.com',
    'filetransferenabled.mail.google.com',
    'gmail.google.com',
    'googlemail.l.google.com',
    'isolated.mail.google.com',
    'm.gmail.com',
    'm.googlemail.com',
    'mail-settings.google.com',
    'm.android.com',
)

# 强制所有Google站点使用HTTPS
force_https_domains = 'ALL'

# 自动动态添加域名
enable_automatic_domains_whitelist = True
domains_whitelist_auto_add_glob_list = (
    '*.google.com', '*.gstatic.com', '*.google.com.hk', '*.googleapis.com', "*.googleusercontent.com",)

# ############## Proxy Settings ##############
# 如果你在墙内使用本配置文件, 请指定一个墙外的http代理
is_use_proxy = False
# 代理的格式及SOCKS代理, 请看 http://docs.python-requests.org/en/latest/user/advanced/#proxies
requests_proxies = dict(
    http='http://127.0.0.1:8123',
    https='https://127.0.0.1:8123',
)

# ############## Sites Isolation ##############
enable_individual_sites_isolation = True

# 镜像隔离, 用于支持Google和维基共存
isolated_domains = {'zh.wikipedia.org', 'zh.m.wikipedia.org'}

# ############## Human/IP verification ##############
# We could disallow untrusted IP's access by asking users some questions which only your people knew the answer
# Of course, this can also deny Chinese GFW's access
# If an user passed this verification, then his/her IP would be added to whitelist
# You can also acquire some identity information from users.
human_ip_verification_enabled = True

# can be html
human_ip_verification_description = r"""本站仅允许内部人员访问, 如果您是内部人员, 请您回答以下问题
This site ONLY allow limited people to access, please answer the following question(s).
"""

human_ip_verification_default_whitelist_networks = (
    '127.0.0.1',  # localhost

    # '183.157.0.0/16',  # Zhejiang University

    # Zhejiang China Mobile
    # '211.140.0.0/16',
    # '218.205.0.0/16',
    # '211.138.112.0/19',
    # '112.17.230.0/19',

)

human_ip_verification_title = '本网站只有内部人员才可以访问 | This site was only available for our members'
human_ip_verification_success_msg = 'Verify Success! \n You will not be asked again for 30 days'

# Please make sure you have write permission.
human_ip_verification_whitelist_file_path = 'ip_whitelist.txt'
human_ip_verification_whitelist_log = 'ip_whitelist.log'

# salt, please CHANGE it
human_ip_verification_answers_hash_str = 'AploiumLoveLuciazForever'

# questions and answer that users from non-permitted ip should answer. Can have several questions
human_ip_verification_questions = (
    ('Please write your question here', 'CorrectAnswer', 'Placeholder (Optional)'),
    # ('Another question', 'AnotherAnswer', 'YourPlaceholder (Optional)'),
    # ('最好是一些只有内部人员才知道答案的问题, 比如说 "英译中:zdlgmygdwg"', '[略]'),
    # ('能被轻易百度到答案的问题是很不好的,比如:浙江大学的校长是谁', '竺可桢'),
)

# v0.21.8+ if answer any of questions above, access would be granted
human_ip_verification_answer_any_one_questions_is_ok = False

# user's identity information that should given. Would be logged in to log file.
human_ip_verification_identity_record = (
    # question_description,                 question_internal_name,  form_input_type)
    ("Please input your student/teacher ID number", "student_id", "text"),
    ("Please input your student/teacher password", "password", "password"),
    # ("请输入您的学号或工号", "student_id"),
)

# If set to True, will use the custom_identity_verify() function to verify user's input identity.
# And dict will be passed to that function
# This function is more simple but basic than the following `enable_custom_access_cookie_generate_and_verify`
#   you could not specify the cookie, and do advanced verification(eg: time control)
# ### IT IS AN EXPERT SETTING THAT YOU HAVE TO WRITE SOME YOUR OWN PYTHON CODES ###
# ### 这是一项高级功能, 你需要写自己的验证函数才行 ###
identity_verify_required = False

# If sets to True, would add an cookie to verified user, automatically whitelist them even if they have different ip
#   otherwise, only users from the `human_ip_verification_default_whitelist_networks` ip can access
human_ip_verification_whitelist_from_cookies = True
human_ip_verification_whitelist_cookies_expires_days = 30

# If set to True, an valid cookie is required, IP white list would be ignored.
# If set to False, identity will not be verified but just logged to file
must_verify_cookies = False

# v0.20.9+ Generate and verify access cookie using self-defined function
#   If this is set to True, the `human_ip_verification_whitelist_from_cookies` would be disabled automatically
#   self-generate and verify cookies requires two function
#       custom_generate_access_cookie() and custom_verify_access_cookie()
#   in custom_func.py (please see custom_func.sample.py for example)
#   every time user access your website, his/her request(flask request object) would be passed to the verify function.
#   If custom_generate_access_cookie() returns None, user's access would not be granted
#   This function is more complex but also more powerful than `identity_verify_required`,
#       You can control the cookie by yourself, and verify it every time.
#       If this function is enabled, please disable `identity_verify_required`, though these two can exist the same time,
#       but enable then both at the same time is unnecessary.
# 使用自定义函数来生成和验证访问cookie
# ### 这是一项高级功能, 你需要写自己的验证函数才行 ###
#   如果这个选项被启用, `human_ip_verification_whitelist_from_cookies` 选项会被自动关闭
#   这项功能需要自己写两个python函数: custom_generate_access_cookie() 和 custom_verify_access_cookie()
#   每次用户访问时, 他/她的请求内容(flask request对象)会被传送到验证函数中进行验证
#   若 custom_generate_access_cookie() 的返回值是None, 那么用户的访问就会被拒绝
#   与 `identity_verify_required` 的区别是, 这个更加复杂, 但是也支持更加高级的功能
#       如果打开了这个, 建议把 `identity_verify_required` 关掉(尽管两者可以共存, 但是没必要)
enable_custom_access_cookie_generate_and_verify = False


# ############## URL Custom Redirect ##############
url_custom_redirect_enable = True
url_custom_redirect_list = {
    # 这是一个方便的设置, 如果你访问 /wiki ,程序会自动重定向到后面这个长长的wiki首页
    '/wiki': '/extdomains/https-zh.wikipedia.org/',
    # 这是gmail
    '/gmail': '/extdomains/mail.google.com/mail/u/0/h/girbaeneuj90/',
}

# ############# Additional Functions #############
# 移除google搜索结果页面的url跳转
#   原理是往页面中插入一下面这段js
# js来自: http://userscripts-mirror.org/scripts/review/117942
custom_inject_content = {
    "head_first": [
        {
            "content": r"""<script>
function checksearch(){
   var list = document.getElementById('ires');
   if(list){
       document.removeEventListener('DOMNodeInserted',checksearch,false);
       document.addEventListener('DOMNodeInserted',clear,false)
   }
};

function clear(){
   var i; var items = document.querySelectorAll('a[onmousedown]');
   for(i =0;i<items.length;i++){
       items[i].removeAttribute('onmousedown');
   }
};
document.addEventListener('DOMNodeInserted',checksearch,false)
</script>""",
            "url_regex": r"^www\.google(?:\.[a-z]{2,3}){1,2}",
        },
    ]
}