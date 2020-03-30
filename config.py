TOKEN = '1127861580:AAGV7ixtdHovL47iPmVhwQmwp0mmvaamBdc' 
PLAYERS_COUNT_TO_START = 4 
PLAYERS_COUNT_LIMIT = 10  
REQUEST_OVERDUE_TIME = 10 * 60  
SSL_CERT = '/root/cert/PUBLIC.pem'  # File path of public SSL certificate 
SSL_PRIV = '/root/cert/PRIVATE.key'  # File path of private key of SSL certificate

import logging
LOGGER_LEVEL = logging.DEBUG
bot = telebot.TeleBot("1127861580:AAGV7ixtdHovL47iPmVhwQmwp0mmvaamBdc")
