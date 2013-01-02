# -*- coding: utf-8 -*-
from flask import Markup

#: The title of this site
SITE_TITLE = 'Lastuser'

#: Support contact email
SITE_SUPPORT_EMAIL = 'test@example.com'

#: TypeKit code for fonts
TYPEKIT_CODE = ''

#: Google Analytics code UA-XXXXXX-X
GA_CODE = ''

#: Database backend
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

#: Secret key
SECRET_KEY = 'make this something random'

#: Timezone
TIMEZONE = 'Asia/Calcutta'

#: Mail settings
#: MAIL_FAIL_SILENTLY : default True
#: MAIL_SERVER : default 'localhost'
#: MAIL_PORT : default 25
#: MAIL_USE_TLS : default False
#: MAIL_USE_SSL : default False
#: MAIL_USERNAME : default None
#: MAIL_PASSWORD : default None
#: DEFAULT_MAIL_SENDER : default None
MAIL_FAIL_SILENTLY = False
MAIL_SERVER = 'localhost'
DEFAULT_MAIL_SENDER = ('Lastuser', 'test@example.com')

#: Logging: recipients of error emails
ADMINS = []

#: Log file
LOGFILE = 'error.log'

#: Use SSL for some URLs
USE_SSL = False

#: Twitter integration
OAUTH_TWITTER_KEY = ''
OAUTH_TWITTER_SECRET = ''

#: GitHub integration
OAUTH_GITHUB_KEY = ''
OAUTH_GITHUB_SECRET = ''

#: Recaptcha for the registration form
RECAPTCHA_USE_SSL = USE_SSL
RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''
RECAPTCHA_OPTIONS = ''

#: SMS gateways
SMS_SMSGUPSHUP_MASK = ''
SMS_SMSGUPSHUP_USER = ''
SMS_SMSGUPSHUP_PASS = ''

#: Messages (text or HTML)
MESSAGE_FOOTER = Markup('Copyright &copy; <a href="http://hasgeek.com/">HasGeek</a>. Powered by <a href="https://github.com/hasgeek/lastuser" title="GitHub project page">Lastuser</a>, open source software from <a href="https://github.com/hasgeek">HasGeek</a>.')
USERNAME_REASON = ''
EMAIL_REASON = 'Please provide an email address to complete your profile'
BIO_REASON = ''
TIMEZONE_REASON = 'Dates and times will be shown in your preferred timezone'
ORG_NAME_REASON = u"Your company’s name as it will appear in the URL. Letters, numbers and dashes only"
ORG_TITLE_REASON = u"Your organization’s given name, preferably without legal suffixes"
ORG_DESCRIPTION_REASON = u"A few words about your organization (optional). Plain text only"

#: RETASK_SETTINGS
RETASK_HOST = "localhost"
RETASK_PORT = 6379
RETASK_DB = 0
RETASK_PASSWORD = ""
RETASK_QUEUE_NAME = ""
