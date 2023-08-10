from os import path

# СТРОКИ, КОТОРЫЕ ЛУЧШЕ НЕ ТРОГАТЬ

# Адресная книга
mskdev = 'stand1'
gpn = 'stand5'
generated_dev = "stand4"
genrestest = 'stand3'
demorospan = 'stand2'

# Функциональное
main_dir = path.dirname(__file__)

# СТРОКИ ЗАПОЛНЯЮТСЯ ПОЛЬЗОВАТЕЛЕМ

tester_name = "Ваня Пупкин"                                                             # Имя-фамилия тестировщика
ffmpeg_path = fr'{main_dir}\путь к ffmpeg.exe'                                          # Путь к ffmpeg.exe
downloads_dir = fr"ПУТЬ К ПАПКЕ ЗАГРУЗОК"                                               # Путь к папке загрузок
current_stand = genrestest                                                              # Выбор стенда для работы
