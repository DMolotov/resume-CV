import os


class CalculationConstructorFilesList:
    current_dir = os.path.abspath(__file__)
    current_dir = current_dir[:-13]

    # Макропараметры
    macro_dir = os.path.join(current_dir, '3 Orenburg macro 22.6Б 06.10.las')

    # ФЭМ НДПИ
    FEM_NDPI_dir = os.path.join(current_dir, 'Gazprom-Neft_Upstream_v22.6Б.xml')

    # ФЭМ НДД
    FEM_NDD_dir = os.path.join(current_dir, 'Gazprom-Neft_Upstream_v22.6Б_NDD.xml')

    # Оренбуржский формат - МК ЮУНГ Бурение
    # 1 консолидация 6 кейсов
    MB_YUUNG_BUR_filename = 'МК_Upstream_v22.6Б_6+6_ЮУНГ_Бурение_3_51'
    MB_YUUNG_BUR_dir = os.path.join(current_dir, (MB_YUUNG_BUR_filename + '.xlsx'))
    MB_YUUNG_BUR_consolidations = ('2021_2023_Бур_3_скв_зав51_ЮУНГ_ф', ) # не опечатка, запятая нужна потому что тип
    # данных - tuple
    MB_YUUNG_BUR_cases = ([
        '2021_2023_Бур_3_скв_зав51_ЮУН_51Р_БУР_БУР_2022_ф',
        '2021_2023_Бур_3_скв_зав51_ЮУ_ГПЭС_БУР_БУР_2022_ф',
        '2021_2023_Бур_3_скв_зав51_ЮУН_510_БУР_БУР_2022_ф',
        '2021_2023_Бур_3_скв_зав51_Ю_Инфра_БУР_БУР_2022_ф',
        '2021_2023_Бур_3_скв_зав51_ЮУН_513_БУР_БУР_2022_ф',
        '2021_2023_Бур_3_скв_зав51_ЮУН_512_БУР_БУР_2022_ф'
    ], )    # аналогично комментарию выше

    # Оренбуржский формат - МК ЮУНГ
    # 20 консолидаций 59 кейсов
    MB_YUUNG_filename = 'МК_Upstream_v22.6Б_6+6_ЮУНГ'
    MB_YUUNG_dir = os.path.join(current_dir, (MB_YUUNG_filename + '.xlsx'))
    MB_YUUNG_consolidations = (
        '2020_2021_Каркас_ЮУНГ_ф',
        '2022_2023_ЗБС_4_скв_ЮУНГ_ф',
        '2021_Формирование_стоимости_ГРА_ЮУНГ_п',
        '2022_Неинвестиционные_ревексы_ЮУНГ_ф',
        '2022_Каркас_ЮУНГ_ф',
        '2021_2023_Инфра+ОНВСС_поддержание_ЮУНГ_ф',
        '2019_Инфра+ОНВСС_поддерж_ЮУНГ_ф',
        '2022_ТРС_27_скв_ЮУНГ_ф',
        '2018-2019_Тех_Перевооружение_УППНГ_ЮУНГ_ф',
        '2022_КГРП_5_скв_ЮУНГ_ф',
        '2022_КРС_ЮУНГ_ф',
        '2021_ПП_скв_№5326_ЮУНГ_ф',
        '2022_Инфра+ОНВСС_поддержание_ЮУНГ_ф',
        '2022_Формирование_стоимости_ГРА_ЮУНГ_ф',
        '2022_Программа_ЦиН_трубопроводов_НПО_ЮУНГ_ф',
        '2020_Инфра+ОНВСС_поддержание_ЮУНГ_ф',
        '2020_СКП_ГПН_НТЦ_ЮУНГ_ф',
        '2022_ПВЛГ_3_скв_ЮУНГ_ф',
        '2020_2023_УПКГ_2_3 ступеней_ЮУНГ_ф',
        '2021_РВП_1_скв_ЮУНГ_доп'
    )
    MB_YUUNG_cases = (
        [
            '2020_2021_Карк_Охр_здоровья_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_Эл_безопас_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_ОНВСС_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_здравпункт_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУН_ВЫСОТА_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_СБУ_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_ГНВП_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_каб_линии_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУНГ_Негабарит_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЮУН_Взрывы_ЮУНГ_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2022_2023_ЗБС_4_скв_ЮУНГ_5352_ЗВС_ЗВС_2023_ф',
            '2022_2023_ЗБС_4_скв_ЮУНГ_5340_ЗВС_ЗВС_2023_ф',
            '2022_2023_ЗБС_4_скв_ЮУНГ_5330_ЗВС_ЗВС_2023_ф',
            '2022_2023_ЗБС_4_скв_ЮУНГ_5317_ЗВС_ЗВС_2023_ф'
        ],
        ['2021_Формирование_стоимости_ГР_ГРА_ГРР_КАП_ГРР_п'],
        ['2022_Неинвестицион_Капитоновское_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_Каркас_ЮУНГ_Эл_безопас_БАЗ_БАЗ_Нефть_ф',
            '2022_Каркас_ЮУНГ_ОНВСС_БАЗ_БАЗ_Нефть_ф',
            '2022_Каркас_ЮУНГ_Инфра_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2021_2023_Инфра+ОНВСС_по_ОНВСС_Ю_БАЗ_БАЗ_Нефть_ф',
            '2021_2023_Инфра+ОН_Реконстр_Вл_Ю_БАЗ_БАЗ_Нефть_ф',
            '2021_2023_Инфра+ОНВСС_подд_Инф_Ю_БАЗ_БАЗ_Нефть_ф',
            '2021_2023_Инфра+ОН_Капитоновское_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2019_Инфра+ОНВСС_поддерж_Ю_ПИР_Ю_БАЗ_БАЗ_Нефть_ф',
            '2019_Инфра+ОНВСС_подд_Кап_ремонт_БАЗ_БАЗ_Нефть_ф',
            '2019_Инфра+ОНВСС_поддерж_Ю_Инф_Ю_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2022_ТРС_27_скв_ЮУ_Капитоновское_БАЗ_БАЗ_Нефть_ф'],
        ['2018-2019_Модуль_охлаждения_ГАР_ГАР_ИП_ГП_УПКГ_ф'],
        [
            '2022_КГРП_5_скв_ЮУНГ_5355_ГРП_ГРП_2022_ф',
            '2022_КГРП_5_скв_ЮУНГ_5307_ГРП_ГРП_2022_ф',
            '2022_КГРП_5_скв_ЮУНГ_5301_ГРП_ГРП_2022_ф',
            '2022_КГРП_5_скв_ЮУНГ_5324_ГРП_ГРП_2022_ф',
            '2022_КГРП_5_скв_ЮУНГ_5320_ГРП_ГРП_2022_ф'
        ],
        [
            '2022_КРС_ЮУНГ_КРС_ПРОЧ_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_КРС_ПРОЧ_ЛНЭК_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_БОПЗП_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_КРС_ЛАПЛ_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_Ремонты_ППД_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_КРС_ЛТА_ЮУНГ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЮУНГ_РИР_база_ЮУНГ_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2021_ПП_скв_№5326_ЮУНГ_5326_ПиП_ПП_2021_ф'],
        [
            '2022_Инфра+ОНВСС_поддерж_ОНВСС_Ю_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_п_Реконстр_Вл_Ю_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС__УМАСИТ_ОНВСС_Ю_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_п_Капитоновское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддержан_Инф_Ю_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2022_Формирование_стоимости_ГР_ГРА_ГРР_КАП_ГРР_ф'],
        [
            '2022_Программа_ЦиН_тру_ПИР_ЦиН_Ю_БАЗ_БАЗ_Нефть_ф',
            '2022_Программа_ЦиН_т_ОНВСС_ЦиН_Ю_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2020_Инфра+ОНВСС_поддержан_ПИР_Ю_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_п_Капитоновское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддерж_ОНВСС_Ю_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддержан_Инф_Ю_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2020_СКП_ГПН_НТЦ_ЮУНГ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_ПВЛГ_3_скв_ЮУНГ_232_ПиП_ПП_2022_ф',
            '2022_ПВЛГ_3_скв_ЮУНГ_471_ПиП_ПП_2022_ф',
            '2022_ПВЛГ_3_скв_ЮУНГ_5337_ПиП_ПП_2022_ф'
        ],
        ['2020_2023_УПКГ_2_3 ст_Инфра_ГАР_ГАР_ИП_ГП_УПКГ_ф'],
        ['2021_РВП_1_скв_ЮУНГ_доп._5334_ЗВС_РВП_2021_ф']
    )

    # Оренбуржский формат - МК Ягодный
    # 21 консолидаций 62 кейсов
    MB_YAG_filename = 'МК_Upstream_v22.6Б_6+6_Ягодный'
    MB_YAG_dir = os.path.join(current_dir, (MB_YAG_filename + '.xlsx'))
    MB_YAG_consolidations = (
        '2022_КРС_Ягодный_ф',
        '2018_2020_ГРР_1_скв_Ягодный_ф',
        '2022_Иссл_скв_62Р_Ягодный_ф',
        '2022_ТРС_Ягодный_ф',
        '2023_Бур_3_скв_зав62р_Земл_ф',
        '2022_ОПЗ_скв_62Р_Землянское_ф',
        '2022_Формирование_стоимости_ГРА_Ягодный_ф',
        '2022_Программа_ЦиН_трубопроводов_НПО_Ягодный_ф',
        '2019_ВДК_скв_№69_Ягодный_ф',
        '2022_Неинвестиционные_Ревексы_Ягодный_ф',
        '2020_РБП_Ягодный_п',
        '2020_ГРР_скв_№48_Ягодный_ф',
        '2019_2020_Труба_ВЛ_Ягодного_ЛУ_доп_ф',
        '2020_Инфра+ОНВСС_поддержание_Ягодный_ф',
        '2021_Формирование_стоимости_ГРА_Ягодный_п',
        '2019_2021_Бур_4_скв_зав_47ПО+ПИР_ф',
        '2022_Инфра+ОНВСС_поддержание_Ягодный_ф',
        '2021_ГРР_СРР_Ягодный_ф',
        '2019_2021_ГРР_50_скв_Ягодный_ф',
        '2021_Инфра+ОНВСС_поддержание_Ягодный_ф',
        '2022_Создание_ПГД_Ягодный_п'
    )
    MB_YAG_cases = (
        [
            '2022_КРС_Ягодны_КРС_ПРОЧ_Ягодный_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_Яго_КРС_ПРОЧ_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_Яго_Консервация_Ягодный_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС__Консервация_Землянское_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2018_2020_ГРР_1_скв_Ягодный_41_НИР_ГРР_ЯГД_ГРР_ф',
            '2018_2020_ГРР_1_скв_Ягодный_41р_ГРР_ЯГД_ГРР_ф'
        ],
        ['2022_Иссл_скв_62Р_Ягодный_62Р_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_ТРС_Ягодный_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2022_ТРС_Ягодный_Ягодный_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2023_Бур_3_скв_зав62р_Земл_621_ГРР_ЗЕМ_Н_P50_ф',
            '2023_Бур_3_скв_зав62р_Земл_Инфра_ГРР_ЗЕМ_Н_P50_ф',
            '2023_Бур_3_скв_зав62р_Земл_620_ГРР_ЗЕМ_Н_P50_ф',
            '2023_Бур_3_скв_зав62р_Земл_622_ГРР_ЗЕМ_Н_P50_ф'
        ],
        ['2022_ОПЗ_скв_62Р_Землянское_62Р_ОПЗ_ОПЗ_Н_2022_ф'],
        [
            '2022_Формирование_стоимости_ГР_ГРА_ГРР_ЗЕМ_ГРР_ф',
            '2022_Формирование_стоимости_ГР_ГРА_ГРР_ЯГД_ГРР_ф'
        ],
        [
            '2022_П_Замена_камер_СОД_Я_Эффект_БАЗ_БАЗ_Нефть_ф',
            '2022_Программа_ЦиН_тр_Кам_СОД_Яг_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2019_ВДК_скв_№69_Яго_Инфра_ГТМ_ПРОЧИЕ_ГТМ_2021_ф',
            '2019_ВДК_скв_№69_Ягодн_69р_ГТМ_ПРОЧИЕ_ГТМ_2021_ф'
        ],
        [
            '2022_Неинвестиционные_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2022_Неинвестиционные_Ре_Ягодный_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2020_РБП_Ягодный_РБП_БАЗ_БАЗ_Нефть_п'],
        [
            '2020_ГРР_скв_№48_Ягодный_48_ГРР_ЯГД_ГРР_ф',
            '2020_ГРР_скв_№48_Ягодный_48_НИР_ГРР_ЯГД_ГРР_ф'
        ],
        ['2019_2020_Труба_ВЛ_Ягодног_Инфра_БАЗ_БАЗ_Нефть_ф'],
        [
            '2020_Инфра+ОНВСС_подд_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВС_Система связи_Яг_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддерж_Ягодный_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВ_Маркшейдер_работы_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддержан_Инф_Я_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддержа_УМЗР_Я_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддерж_ОНВСС_Я_БАЗ_БАЗ_Нефть_ф',
            '2020_Стро-во пункта слива НСЖ_Яг_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2021_Формирование_стоимости_ГР_ГРА_ГРР_ЯГД_ГРР_п',
            '2021_Формирование_стоимости_ГР_ГРА_ГРР_ЗЕМ_ГРР_п'
        ],
        [
            '2019_2021_Бур_4_скв_зав_47ПО+_5344_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+П_474_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО_Инфра_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав__УППНГ_фин_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+_ГПЭС_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО_УППНГ_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+_5343_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+П_УПН_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+П_ПНН_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+П_473_БУР_БУР_КАП_ф',
            '2019_2021_Бур_4_скв_зав_47ПО+П_472_БУР_БУР_КАП_ф'
        ],
        [
            '2022_Инфра+ОНВСС_поддержан_Инфра_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддерж_ОНВСС_Я_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_подд_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддержани_ГПЭС_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддержан_Труба_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддерж_Ягодный_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2021_ГРР_СРР_Ягодный_НИР_ГРР_ЯГД_ГРР_ф'],
        [
            '2019_2021_ГРР_50_скв_Ягодны_50_НИР_ГРР_ЯГД_ГРР_ф',
            '2019_2021_ГРР_50_скв_Ягодный_50_ГРР_ЯГД_ГРР_ф'
        ],
        [
            '2021_Инфра+ОНВСС_подд_Землянское_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_поддерж_ОНВСС_Я_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_поддерж_Ягодный_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_поддержан_Инф_Я_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВ_Маркшейдер_работы_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2022_Создание_ПГД_Ягодный_НИР_ГРР_ЯГД_ГРР_п']
    )

    # Оренбуржский формат - МК ЦНТ
    # 28 консолидаций 134 кейсов
    MB_CNT_filename = 'МК_Upstream_v22.6Б_6+6_ЦНТ'
    MB_CNT_dir = os.path.join(current_dir, (MB_CNT_filename + '.xlsx'))
    MB_CNT_consolidations = (
        '2022_Неинвестиционные_ревексы_ЦНТ_ф',
        '2022_ТРС_ЦНТ_ф',
        '2022_Формирование_стоимости_ГРА_ЦНТ_ф',
        '2020_2021_Каркас_ЦНТ_ф',
        '2016_2017_КИТСО_ЦНТ_ф',
        '2022_ОПЗ_3_скв_чистый_горизонт_ЦФНМ_п',
        '2021_Инфра+ОНВСС_поддержание_ЦГМ_ф',
        '2019_2022_Стр-во_блока_отбензинивания_газа_ЦНТ_ф',
        '2022_КРС_ЦНТ_ф',
        '2019_2022_Газовая_программа_ЦНТ_ф',
        '2022_Инфра+ОНВСС_поддержание_ЦФНМ_ф',
        '2021_Оптимизация_добычи_ЦНТ_ф',
        '2016_РБП_База_ЦНТ_ф',
        '2021_Формирование_стоимости_ГРА_ЦНТ_п',
        '2021_2023_Пер_ППД_6_скв_ЦФНМ_ф',
        '2018_2020_Бур_17_скв_ЦНТ_ф',
        '2020_Инфра+ОНВСС_поддержание_ЦНТ_ф',
        '2022_ОПЗ_10_скв_ЦФНМ_ф',
        '2022_Каркас_ЦНТ_ф',
        '2020_ВДК_скв_№21Р_ЦФНМ_ф',
        '2018_Перевод_в_ППД_7_скв_ЦНТ_ф',
        '2019_Инфра+ОНВСС_поддержание_ЦФНМ_ф',
        '2022_Программа_ЦиН_трубопроводов_НПО_ЦФНМ_ф',
        '2013_УПНГ_1_этап_ПИР_ЦНТ_ф',
        '2022_ПП_скв_7_ЦФНМ_ф',
        '2022_Бур_2_скв_ЦФНМ_ф',
        '2022_ВДК_скв_106_ЦФНМ_ф',
        '2020_2022_Пер_ППД_Доп_2020_2022_ЦНТ_ф'
    )
    MB_CNT_cases = (
        ['2022_Неинвестиционны_Царичанское_БАЗ_БАЗ_Нефть_ф'],
        ['2022_ТРС_ЦНТ_Царичанское_БАЗ_БАЗ_Нефть_ф'],
        ['2022_Формирование_стоимости_ГР_ГРА_ГРР_АХМ_ГРР_ф'],
        [
            '2020_2021_Карка_Охр_здоровья_ЦНТ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_Инфра_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_ГАЗ_ЦНТ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_ОНВСС_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_СБУ_ЦНТ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_ВЫСОТА_ЦНТ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_ГНВП_ЦНТ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЦНТ_Негабарит_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2016_2017_КИТСО_ЦНТ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_ОПЗ_3_скв_чистый_горизо_Х2_ОПЗ_ОПЗ_Л_2022_п',
            '2022_ОПЗ_3_скв_чистый_горизо_Х3_ОПЗ_ОПЗ_Л_2022_п',
            '2022_ОПЗ_3_скв_чистый_горизо_Х1_ОПЗ_ОПЗ_Л_2022_п'
        ],
        [
            '2021_Инфра+ОНВСС_поддерж_ОНВСС_Ц_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_под_Филатовское_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_под_Царичанское_БАЗ_БАЗ_Нефть_ф',
            '2021_Инфра+ОНВСС_поддержан_Инф_Ц_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2019_2022_Стр-во_б_2_этап_ДГиЭ_ГАР_ГАР_ИП_БЛОГ_ф',
            '2019_2022_Стр-во_бл_1_этап_ДНТ_ГАР_ГАР_ИП_БЛОГ_ф',
            '2019_2022_Стр-во_б_1_этап_ДГиЭ_ГАР_ГАР_ИП_БЛОГ_ф',
            '2019_2022_Стр-во_блока_от_БЛОГ_ГАР_ГАР_ИП_БЛОГ_ф',
            '2019_2022_Стр-во_блока__Эффект_ГАР_ГАР_ИП_БЛОГ_ф'
        ],
        [
            '2022_КРС_ЦНТ_Водозаборные_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_ОПЗ_ППД_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_Консервация_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_КРС_ЛТА_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_КРС_РИР_ППД_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_Рем_ППД_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_КРС_ПРОЧ_ЦФНМ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_ЦНТ_КРС_ЛАПЛ_ЦФНМ_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2019_2022_Газовая_программ_Инфра_ГАР_ГАР_ИП_ГП_ф'],
        [
            '2022_Инфра+ОНВСС__УМАСИТ_ОНВСС_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_под_Царичанское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддержан_Инф_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддерж_ОНВСС_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_под_Филатовское_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2021_Оптимизация_доб_559_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_170_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_723_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_718_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_517_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_621_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_160_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_д_597_ГТМ_ПРОЧИЕ_Л_Ф_ГТМ_2021_ф',
            '2021_Оптимизация_доб_717_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_518_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_522_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_510_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_715_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_138_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_526_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_501_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_198_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_161_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_168_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_146_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_д_556-1_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_527_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_177_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_521_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_597_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_д_501-1_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_703_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_552_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_536_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_134_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_188_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_707_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_710_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_доб_511_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф',
            '2021_Оптимизация_д_530-1_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф'
        ],
        ['2016_РБП_База_ЦНТ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        ['2021_Формирование_стоимости_ГР_ГРА_ГРР_АХМ_ГРР_п'],
        ['2021_2023_Пер_ППД_6__Царичанское_БАЗ_БАЗ_Нефть_ф', '2021_2023_Пер_ППД_6_скв_ЦФ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        [
            '2018_2020_Бур_17_скв_ЦНТ_Инфра_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_701_БУР_БУР_Л_Ф_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_599_БУР_БУР_Л_Ф_2020_ф',
            '2018_2020_Бур_17_скв_ЦН_307-1_БУР_БУР_Л_Ф_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_618_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_620_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_623_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_717_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_719_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_615_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_720_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_597_БУР_БУР_Л_Ф_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_516_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_600_БУР_БУР_Л_Ф_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_515_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_714_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_716_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_718_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв_ЦНТ_БКНС_БУР_БУР_2020_ф',
            '2018_2020_Бур_17_скв__Энергоцентр_БУР_БУР_2020_ф'
        ],
        [
            '2020_Инфра+ОНВСС_поддержан_Инф_Ц_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_под_Царичанское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_под_Филатовское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддерж_ОНВСС_Ц_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2022_ОПЗ_10_скв_ЦФНМ_X7_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_3_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_503_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_X10_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_222_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_X9_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_X8_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_X6_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_X5_ОПЗ_ОПЗ_Л_2022_ф',
            '2022_ОПЗ_10_скв_ЦФНМ_416_ОПЗ_ОПЗ_Н_2022_ф'
        ],
        ['2022_Каркас_ЦНТ_ОНВСС_БАЗ_БАЗ_Нефть_ф', '2022_Каркас_ЦНТ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        ['2020_ВДК_скв_№21Р_ЦФ_21Р_ГТМ_ПРОЧИЕ_ГТМ_Н_2021_ф'],
        ['2018_Перевод_в_ППД_7_скв_Ц_Инфра_БАЗ_БАЗ_Нефть_ф', '2018_Перевод_в_ППД_7_Царичанское_БАЗ_БАЗ_Нефть_ф'],
        ['2019_Инфра+ОНВСС_поддержан_Инф_Ц_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_Программа_ЦиН_т_ОНВСС_ЦиН_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Программа_ЦиН_трубопр_Инф_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Програ_Дренаж_емкость_СОД_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Программа_ЦиН_Система_ППД_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Программа_ЦиН_тру_ПИР_ЦиН_Ц_БАЗ_БАЗ_Нефть_ф',
            '2022_Програ_Система_ППД_Ц_Эффект_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2013_УПНГ_1_этап_ПИР_ЦНТ_МТР_РИН_РИН_ИП_УПНГ_ф',
            '2013_УПНГ_1_этап_ПИР_ЦНТ_Пир_РИН_РИН_ИП_УПНГ_ф',
            '2013_УПНГ_1_этап_ПИР_ЦНТ_Инфра_РИН_РИН_ИП_УПНГ_ф'
        ],
        ['2022_ПП_скв_7_ЦФНМ_7_ПиП_ПП_ФИЛ_Н_2022_ф'],
        [
            '2022_Бур_2_скв_ЦФНМ_591-1_БУР_БУР_Н_2022_ф',
            '2022_Бур_2_скв_ЦФНМ_597-1_БУР_БУР_Н_2022_ф',
            '2022_Бур_2_скв_ЦФНМ_ПИР_БУР_БУР_Н_2022_ф'
        ],
        ['2022_ВДК_скв_106_ЦФН_106_ГТМ_ПРОЧИЕ_ГТМ_Н_2022_ф'],
        [
            '2020_2022_Пер_ППД_До_Энергоцентр_БАЗ_БАЗ_Нефть_ф',
            '2020_2022_Пер_ППД_Доп_2020_Инфра_БАЗ_БАЗ_Нефть_ф',
            '2020_2022_Пер_ППД_До_Царичанское_БАЗ_БАЗ_Нефть_ф'
        ]
    )

    # Оренбуржский формат - МК Кувайский
    # 2 консолидации 2 кейса
    MB_KUV_filename = 'МК_Upstream_v22.6Б_6+6_Кувайский'
    MB_KUV_dir = os.path.join(current_dir, (MB_KUV_filename + '.xlsx'))
    MB_KUV_consolidations = ('2019_ГРР_Создание_ПГД_Кувайский_ф', '2019_2020_Создание_концепта_ГМ_Кув_ЛУ_ф')
    MB_KUV_cases = [['2019_ГРР_Создание_ПГД_Кувайски_ПГД_ГРР_КУВ_ГРР_ф'],
                    ['2019_2020_Создание_концепт_Концепт_ГРР_КУВ_ГРР_ф']]

    # Оренбуржский формат - МК ЖИ
    # 31 консолидация 123 кейса
    MB_GEE_filename = 'МК_Upstream_v22.6Б_6+6_ЖИ_корр_штрафы_Бур_23_ЖИ'
    MB_GEE_dir = os.path.join(current_dir, (MB_GEE_filename + '.xlsx'))
    MB_GEE_consolidations = (
        '2020_ВЭР_скв_80р_ЖИ_ф',
        '2022_ГРР_НИР_Бенчмарк_Уранский_ф',
        '2018_2020_ГРР_5скв_ЖИ_ф',
        '2020_Инфра+ОНВСС_поддержание_ЖИ_ф',
        '2022_Инфра+ОНВСС_поддержание_ЖИ_ф',
        '2022_ГРР_Создание_ПГД_Краснореченский_ф',
        '2022_Формирование_стоимости_ГРА_ЖИ_ф',
        '2022_Пер_ППД_ЖИ_ф',
        '2022_Неинвестиционные_Ревексы_ЖИ_ф',
        '2019_2020_ГРР_скв_7_ЖИ_ф',
        '2021_Оптимизация_добычи_ЖИ_ф',
        '2019_Инфра+ОНВСС_поддержание_ЖИ_ф',
        '2016_РБП_ГРР_ЖИ_ф',
        '2022_КРС_прочие_ЖИ_ф',
        '2022_Каркас_ЖИ_ф',
        '2016_Формирование_стоимости_ГРА_ЖИ_ф',
        '2022_ГРР_скв_№60_ЖИ_ф',
        '2022_ТРС_ЖИ_ф',
        '2020_2021_Каркас_ЖИ_ф',
        '2021_Формирование_стоимости_ГРА_ЖИ_п',
        '2019_2020_ГРР_скв_81_ЖИ_ф',
        '2022_ОПЗ_2_скв_ЖИ_2022_ф',
        '2021_ВЭР_скв_82р_ЖИ_ф',
        '2019_2020_ГРР_скв_32_ЖИ_ф',
        '2022_ГРР_СРР_Уранский_ф',
        '2022_ПП_скв_№101_114_82_ЖИ_ф',
        '2021_Инфра+ОНВСС_поддержание_ЖИ_п',
        '2016_РБП_ГРР_ЖИ_ф',
        '2021_2022_РР_Регион_стратегии_ЖИ_ф',
        '2019_ВЭР_скв_№4_5_6_2019_ЖИ_ф',
        '2017_2023_БУР+УПНГ+УПСВ_ЖИ_ф'
    )
    MB_GEE_cases = (
        ['2020_ВЭР_скв_80р_ЖИ_Инфра_ГРР_ЗАР_Л_P50_ф', '2020_ВЭР_скв_80р_ЖИ_80р_ГРР_ЗАР_Л_P50_ф'],
        ['2022_ГРР_НИР_Бенчмарк_Уранский_НИР_ГРР_БАЛ_ГРР_ф'],
        ['2018_2020_ГРР_5скв_ЖИ_НИР_ГРР_ЦУР_ГРР_ф', '2018_2020_ГРР_5скв_ЖИ_5_ГРР_ЦУР_ГРР_ф'],
        [
            '2020_Инфра+ОНВСС_по_Балейкинское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВС_Западно-Уранский_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддерж_ОНВСС_Ж_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_поддержан_Инф_Ж_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_п_Новосамарское_БАЗ_БАЗ_Нефть_ф',
            '2020_Инфра+ОНВСС_п_Новозаринское_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2022_Инфра+ОНВСС_по_Геополигон_Ж_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_по_Балейкинское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС__УМАСИТ_ОНВСС_Ж_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_п_Новозаринское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_п_Новосамарское_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддерж_КИТСО_Ж_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддерж_ОНВСС_Ж_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВС_Западно-Уранский_БАЗ_БАЗ_Нефть_ф',
            '2022_Инфра+ОНВСС_поддержан_Инф_Ж_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2022_ГРР_Создание_ПГД_Красноре_НИР_ГРР_БАЛ_ГРР_ф'],
        [
            '2022_Формирование_стоимости_ГР_ГРА_ГРР_ЦУР_ГРР_ф',
            '2022_Формирование_стоимости_ГР_ГРА_ГРР_ЗАР_ГРР_ф',
            '2022_Формирование_стоимости_ГР_ГРА_ГРР_РОЩ_ГРР_ф'
        ],
        ['2022_Пер_ППД_ЖИ_Балейкинское_БАЗ_БАЗ_Нефть_ф', '2022_Пер_ППД_ЖИ_Инфра_БАЗ_БАЗ_Нефть_ф'],
        [
            '2022_Неинвестицион_Новозаринское_БАЗ_БАЗ_Нефть_ф',
            '2022_Неинвестицион_Новосамарское_БАЗ_БАЗ_Нефть_ф',
            '2022_Неинвестиционные_Р_Уранский_БАЗ_БАЗ_Нефть_ф',
            '2022_Неинвестиционн_Балейкинское_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2019_2020_ГРР_скв_7_ЖИ_НИР_ГРР_ВУР_ГРР_ф', '2019_2020_ГРР_скв_7_ЖИ_7_ГРР_ВУР_ГРР_ф'],
        ['2021_Оптимизаци_2104_ГТМ_ПРОЧИЕ_ГТМ_БАЛ_Л_2021_ф', '2021_Оптимизация__82_ГТМ_ПРОЧИЕ_ГТМ_БАЛ_Л_2021_ф'],
        [
            '2019_Инфра+ОНВСС_поддержа_БШПД_Ж_БАЗ_БАЗ_Нефть_ф',
            '2019_Инфра+ОНВСС_поддержа_БАДП_Ж_БАЗ_БАЗ_Нефть_ф',
            '2019_Инфра+ОНВСС_поддержан_Инф_Ж_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2016_РБП_ГРР_ЖИ_РБП_ГРР_БАЛ_ГРР_ф'],
        [
            '2022_КРС_прочие_ЖИ_РИР_ППД_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_прочие_ЖИ_Рем_ППД_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_прочие_ЖИ_КРС_ПРОЧ_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_прочие__Конервация_2_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2022_КРС_прочие_ЖИ_ОПЗ_ППД_ЖИ_БАЗ_БАЗ_Нефть_ф'
        ],
        ['2022_Каркас_ЖИ_Инфра_БАЗ_БАЗ_Нефть_ф', '2022_Каркас_ЖИ_ОНВСС_БАЗ_БАЗ_Нефть_ф'],
        ['2016_Формирование_стоимости_ГР_ГРА_ГРР_БАЛ_ГРР_ф', '2016_Формирование_стоимости_ГР_ГРА_ГРР_НОВ_ГРР_ф'],
        [
            '2022_ГРР_скв_№60_ЖИ_60_ПИР_ГРР_РОЩ_ГРР_ф',
            '2022_ГРР_скв_№60_ЖИ_НИР_ГРР_РОЩ_ГРР_ф',
            '2022_ГРР_скв_№60_ЖИ_60_ГРР_РОЩ_ГРР_ф'
        ],
        [
            '2022_ТРС_ЖИ_Уранский_БАЗ_БАЗ_Нефть_ф',
            '2022_ТРС_ЖИ_Новосамарское_БАЗ_БАЗ_Нефть_ф',
            '2022_ТРС_ЖИ_Балейкинское_БАЗ_БАЗ_Нефть_ф',
            '2022_ТРС_ЖИ_Рощинское_БАЗ_БАЗ_Нефть_ф',
            '2022_ТРС_ЖИ_Новозаринское_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2020_2021_Каркас_ЖИ_ОНВСС_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_Инфра_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_СБУ_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_БАДП_Ж_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_Негабарит_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_ВЫСОТА_ЖИ_БАЗ_БАЗ_Нефть_ф',
            '2020_2021_Каркас_ЖИ_ГНВП_ЖИ_БАЗ_БАЗ_Нефть_ф'
        ],
        [
            '2021_Формирование_стоимости_ГР_ГРА_ГРР_РОЩ_ГРР_п',
            '2021_Формирование_стоимости_ГР_ГРА_ГРР_ЗАР_ГРР_п',
            '2021_Формирование_стоимости_ГР_ГРА_ГРР_ЦУР_ГРР_п'
        ],
        ['2019_2020_ГРР_скв_81_ЖИ_НИР_ГРР_ЗАР_ГРР_ф', '2019_2020_ГРР_скв_81_ЖИ_81р_ГРР_ЗАР_ГРР_ф'],
        ['2022_ОПЗ_2_скв_ЖИ_2022_20_ОПЗ_ОПЗ_Н_БАЛ_2022_ф', '2022_ОПЗ_2_скв_ЖИ_2022_80_ОПЗ_ЗАР_Л_P50_ф'],
        ['2021_ВЭР_скв_82р_ЖИ_Инфра_ГРР_ЗАР_Л_P50_ф', '2021_ВЭР_скв_82р_ЖИ_82р_ГРР_ЗАР_Л_P50_ф'],
        ['2019_2020_ГРР_скв_32_ЖИ_НИР_ГРР_КАМ_ГРР_ф', '2019_2020_ГРР_скв_32_ЖИ_32_ГРР_КАМ_ГРР_ф'],
        ['2022_ГРР_СРР_Уранский_НИР_ГРР_ЦУР_ГРР_ф'],
        [
            '2022_ПП_скв_№101_114_82_Ж_82_ПиП_ПП_ЗАР_Л_2022_ф',
            '2022_ПП_скв_№101_114_82__101_ПиП_ПП_НОВ_Н_2022_ф',
            '2022_ПП_скв_№101_114_82__114_ПиП_ПП_НОВ_Н_2022_ф'
        ],
        [
            '2021_Инфра+ОНВС_Западно-Уранский_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_по_Геополигон_Ж_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_поддерж_Эл_снаб_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_по_Балейкинское_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_поддерж_ОНВСС_Ж_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_п_Новозаринское_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_поддержан_Инф_Ж_БАЗ_БАЗ_Нефть_п',
            '2021_Инфра+ОНВСС_п_Новосамарское_БАЗ_БАЗ_Нефть_п'
        ],
        ['2016_РБП_ГРР_ЖИ_РБП_ГРР_БАЛ_ГРР_ф'],
        ['2021_2022_РР_Регион_стра_Стратегия_ГРР_БАЛ_ГРР_ф'],
        [
            '2019_ВЭР_скв_№4_5_6_2019_ЖИ_5ПО_ГРР_ЦУР_Л_P50_ф',
            '2019_ВЭР_скв_№4_5_6_2019_ЖИ_6ПО_ГРР_РОЩ_Н_P50_ф',
            '2019_ВЭР_скв_№4_5_6_2019_ЖИ_4ПО_ГРР_ЦУР_Н_P50_ф',
            '2019_ВЭР_скв_№4_5_6_2019_ЖИ_Инфра_ГРР_ЦУР_Н_ф'
        ],
        [
            '2017_2023_БУР+УПНГ+УПС_8000_БУР_БУР_ЗАР_Л_2022_ф',
            '2017_2023_БУР+УПНГ+УПС_8020_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+УПС_8017_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+УПС_8004_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8007_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8202_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+У_6003_ПП_БУР_ПП_РОЩ_Л_2025_ф',
            '2017_2023_БУР+УПНГ+УПС_8019_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+УПС_6014_БУР_БУР_РОЩ_Н_2023_ф',
            '2017_2023_БУР+УПНГ+У_6000_ПП_БУР_ПП_РОЩ_Л_2025_ф',
            '2017_2023_БУР+УПНГ+УПС_8009_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8003_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПСВ_Ж_ПИР_УПНГ_БУР_БУР_РИН_ф',
            '2017_2023_БУР+УПНГ+УПС_Энергоцентр_БУР_БУР_РИН_ф',
            '2017_2023_БУР+УПНГ+УПС_6001_БУР_БУР_РОЩ_Н_2022_ф',
            '2017_2023_БУР+УПНГ+УПСВ_Ж_ПИР_УПСВ_БУР_БУР_РИН_ф',
            '2017_2023_БУР+УПНГ+УПСВ_ЖИ_Инфра_БУР_БУР_РИН_ф',
            '2017_2023_БУР+УПНГ+УПС_8006_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_6003_БУР_БУР_РОЩ_Н_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8100_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+УПС_8013_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8005_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8010_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8201_БУР_БУР_ЗАР_Л_2024_ф',
            '2017_2023_БУР+УПНГ+УПС_6000_БУР_БУР_РОЩ_Н_2022_ф',
            '2017_2023_БУР+УПНГ+УПС_8002_БУР_БУР_ЗАР_Л_2023_ф',
            '2017_2023_БУР+УПНГ+УПС_8001_БУР_БУР_ЗАР_Л_2022_ф',
            '2017_2023_БУР+УПНГ+УПС_6004_БУР_БУР_РОЩ_Н_2023_ф',
            '2017_2023_БУР+УПНГ+УПСВ_ЖИ_ДНС_БУР_БУР_РИН_ф',
            '2017_2023_БУР+УПНГ+У_6004_ПП_БУР_ПП_РОЩ_Л_2025_ф',
            '2017_2023_БУР+УПНГ+У_6014_ПП_БУР_ПП_РОЩ_Л_2025_ф',
            '2017_2023_БУР+УПНГ+УПС_8008_БУР_БУР_ЗАР_Л_2024_ф'
        ]
    )

    consolidations_black_list = ()
    cases_black_list = ()