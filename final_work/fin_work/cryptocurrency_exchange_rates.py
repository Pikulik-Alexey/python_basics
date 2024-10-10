from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_basic_label(event):
    # Получаем полное название базовой валюты из словаря и обновляем метку
    code = basic_combobox.get()
    name = cur[code]
    basic_label.config(text=name)


def update_target_label(event):
    # Получаем  название целевой валюты из словаря и обновляем метку
    code = target_combobox.get()
    name = cur_2[code]
    target_label.config(text=name)


def receive():
    # Получаем из поля ввода
    target_code = target_combobox.get()
    basic_code = basic_combobox.get()
    if basic_code and target_code:
        try:
            response = requests.get(
                f'https://api.coinlayer.com/api/live?access_key=79f105c6a5be1c9b8168f21b57eaf2f1')
            # Проверяем статус
            response.raise_for_status()
            # Преобразуем ответ в JSON
            data = response.json()
            # Ищем курс для введенной валюты
            if basic_code in data['rates']:
                exchange_rate = data['rates'][basic_code]
                basic_name = cur[basic_code]
                target_name = cur_2[target_code]
                # Выводим курс
                mb.showinfo(
                    'Биткоин', f'Курс: за 1 {basic_name} придется заплатить {exchange_rate:.2f} {target_name}')
            else:
                mb.showerror('Ошибка', f'Валюта {basic_name} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Ошибка: {e}')
    else:
        mb.showinfo('Ошибка', 'Выберите код валюты')


# Словарь кодов валют и их полных названий
cur = {
    '611': 'SixEleven',
    'ABC': 'AB-Chain',
    'ACP': 'Anarchists Prime',
    'ACT': 'ACT',
    'ACT*': 'Achain',
    'ADA': 'Cardano',
    'ADCN': 'Asiadigicoin',
    'ADL': 'Adelphoi',
    'ADX': 'AdEx',
    'ADZ': 'Adzcoin',
    'AE': 'Aeternity',
    'AGI': 'SingularityNET',
    'AIB': 'AdvancedInternetBlock',
    'AIDOC': 'AI Doctor',
    'AION': 'Aion',
    'AIR': 'AirToken',
    'ALT': 'ALTcoin',
    'AMB': 'Ambrosus',
    'AMM': 'MicroMoney',
    'ANT': 'Aragon',
    'APC': 'AlpaCoin',
    'APPC': 'AppCoins',
    'ARC': 'ArcticCoin',
    'ARCT': 'ArbitrageCT',
    'ARDR': 'Ardor',
    'ARK': 'ARK',
    'ARN': 'Aeron',
    'ASAFE2': 'Allsafe',
    'AST': 'AirSwap',
    'ATB': 'ATB coin',
    'ATM': 'ATMChain',
    'AURS': 'Aureus',
    'AVT': 'AventCoin',
    'BAR': 'TBIS token',
    'BASH': 'LuckChain',
    'BAT': 'Basic Attention Token',
    'BAY': 'BitBay',
    'BBP': 'BiblePay',
    'BCD': 'Bitcoin Diamond',
    'BCH': 'Bitcoin Cash / BCC',
    'BCN': 'ByteCoin',
    'BCPT': 'BlockMason Credit Protocol',
    'BEE': 'Bee Token',
    'BIO': 'Biocoin',
    'BLC': 'BlakeCoin',
    'BLOCK': 'BlockNet',
    'BLU': 'BlueCoin',
    'BLZ': 'Bluzelle',
    'BMC': 'Blackmoon Crypto',
    'BNB': 'Binance Coin',
    'BNT': 'Bancor Network Token',
    'BOST': 'BoostCoin',
    'BQ': 'Bitqy',
    'BQX': 'Ethos',
    'BRD': 'Bread token',
    'BRIT': 'BritCoin',
    'BT1': 'Bitfinex Bitcoin Future',
    'BT2': 'Bitcoin SegWit2X',
    'BTC': 'Bitcoin',
    'BTCA': 'Bitair',
    'BTCS': 'Bitcoin Scrypt',
    'BTCZ': 'BitcoinZ',
    'BTG': 'Bitcoin Gold',
    'BTLC': 'BitLuckCoin',
    'BTM': 'BitMark',
    'BTM *': 'Bytom',
    'BTQ': 'BitQuark',
    'BTS': 'Bitshares',
    'BTX': 'Bitcore',
    'BURST': 'BurstCoin',
    'CALC': 'CaliphCoin',
    'CAS': 'Cashaa',
    'CAT': 'BlockCAT',
    'CCRB': 'CryptoCarbon',
    'CDT': 'CoinDash',
    'CESC': 'Crypto Escudo',
    'CHAT': 'ChatCoin',
    'CJ': 'CryptoJacks',
    'CL': 'CoinLancer',
    'CLD': 'Cloud',
    'CLOAK': 'CloakCoin',
    'CMT *': 'CyberMiles',
    'CND': 'Cindicator',
    'CNX': 'Cryptonex',
    'CPC': 'CapriCoin',
    'CRAVE': 'CraveCoin',
    'CRC': 'CrowdCoin',
    'CRE': 'Credits',
    'CRW': 'Crown Coin',
    'CTO': 'Crypto',
    'CTR': 'Centra',
    'CVC': 'Civic',
    'DAS': 'DAS',
    'DASH': 'DigitalCash',
    'DAT': 'Datum',
    'DATA': 'Streamr DATAcoin',
    'DBC': 'DeepBrain Chain',
    'DBET': 'Decent.bet',
    'DCN': 'Dentacoin',
    'DCR': 'Decred',
    'DCT': 'Decent',
    'DEEP': 'Deep Gold',
    'DENT': 'Dent',
    'DGB': 'DigiByte',
    'DGD': 'Digix DAO',
}
# Словарь для целевой валюты
cur_2 = {
    'USD': 'американских долларов'
}

# Создание главного окна и компонентов
win = Tk()
win.title('Курсы криптовалют')
win.geometry('350x300')

Label(text='Базовая валюта').pack(padx=10, pady=10)
# Создаем выпадающий список валют
basic_combobox = ttk.Combobox(values=list(cur.keys()))
basic_combobox.pack(padx=10, pady=10)
basic_combobox.bind('<<ComboboxSelected>>', update_basic_label)
basic_label = ttk.Label()
basic_label.pack(padx=10, pady=10)


Label(text='Целевая валюта').pack(padx=10, pady=10)
# Создаем выпадающий список валют
target_combobox = ttk.Combobox(values=list(cur_2.keys()))
target_combobox.pack(padx=10, pady=10)
target_combobox.bind('<<ComboboxSelected>>', update_target_label)
target_label = ttk.Label()
target_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена', command=receive).pack(padx=10, pady=10)

win.mainloop()
