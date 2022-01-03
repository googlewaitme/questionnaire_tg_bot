from environs import Env
import json

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
CHANNEL_TO_REPORTS = env.str('CHANNEL_TO_REPORTS')

with open('questions.json') as inp_file:
    raw_text = ''.join(inp_file.readlines())
    messages = json.loads(raw_text)
