#Simple implementation of 128-bit AES Algorithm
from Crypto.Cipher import AES
import hashlib
import random

mode = AES.MODE_CBC

#Make the string multiple of 16 bit

def pad_message(file):
    while len(file) % 16 != 0:
        file = file + b'0'
    return file

#Encrypt

def encryp_aes(pwd, file, iv, file_e):
    key = hashlib.sha256(pwd.encode('utf-8')).digest()
    chiper = AES.new(key, mode, iv)

    try:
        with open(file, 'rb') as f:
            message = f.read()
        f.close()
    except:
        print("Erro: O ficheiro não existe")

    encrypted = chiper.encrypt(pad_message(message))

    with open(file_e, 'wb') as f:
        f.write(encrypted)
    f.close()

#Decrypt

def decryp_aes(pwd, file, iv, file_d):
    key = hashlib.sha256(pwd.encode('utf-8')).digest()
    chiper = AES.new(key, mode, iv)

    try:
        with open(file, 'rb') as f:
            message = f.read()
        f.close()
    except:
        print("Erro: O ficheiro não existe")

    message = chiper.decrypt(message)

    with open(file_d, 'wb') as f:
        f.write(message)
    f.close()

#Load IV -- 256 diferent iv's

def loadIV(iv_n):
    iv = ['HcI8JdZVIOIswmUl',
            'tk9WbonGQkqE9LEL',
            '4Scc9IDle9nkKHdS',
            'd1HuIL41NYh6FotU',
            '3RMDbJSacZyosGPF',
            'MBzKWvLEpoRNuiLj',
            'KSWPKD1wozAs4qMx',
            'TipwSbF0rvtP5Anp',
            'Qd8tWVMp2dLLIScl',
            'U1UJqnM1E2H2pdYr',
            '0ew8Z60ZBr98PBgf',
            'sshAdOs08Wg891IG',
            'tm7yap8KlEsR8DOd',
            'Pv3QRqDuRWQpZKJK',
            'LtC2CnVCN0kSx5c2',
            '9yNhPaDvchFPP4pu',
            'ET4TTf4GK74nJKri',
            '7pK4BfDhWo9jw8gt',
            'rLbrnbQzkxCSrFrU',
            '5dxun1qRxWgkgnt5',
            'RHAsv1zsB4NPuEa8',
            'STSsasZ5ewcSjEmz',
            'Gx0xkp2ibWrZAdU7',
            '7Yrbm0HojogvM7JD',
            'xkDpDcbFVLpumR99',
            'phitDcPHVTjHaWb8',
            '1p2bnb9Iqv2tUNqY',
            'r3MTwutXXzTd3OAY',
            'fKt9YtI6rTAPopae',
            'zFH5axKYSS6o4lf2',
            'CLcKCDIId2FPaYdb',
            'R5WjjUvqkRASWI4s',
            'AivWbVwkGEfMEKMu',
            'WFOln5gkcHLBwEhz',
            '7m1CSTDj4NrFd4PF',
            'Q0RKq2lK1G78urxd',
            'lCh6uDpAH3Jnfn1V',
            'ZgJ0AsGDmqjCECMw',
            '8ljeBrPjl80TznXX',
            'QpTG1ZM1ILp1qnDK',
            'f9SYu8JKBR0H85Lt',
            'rVELK8JT8nhLW2vs',
            'bLSJC86XUMypHv9W',
            '9imJWOAhpnc8kw3f',
            'IbEsvxtDw2xUpCLC',
            'DzdRfb0Kx8LxvXR3',
            'CYlBHrDAOWuuB5dA',
            '6oiYc7VMBLHGXKSN',
            'sFO0qTObtOEQHahp',
            'fiP4gpJCm34pq9k1',
            'EdUgDQKl9XSIMdOc',
            'u1hs46nry1UHCDoK',
            'myR25svS0Bte0ekN',
            'YLZ7FcoaJgqyIRyN',
            'jg34vCU8XFUWBhXj',
            'pvJu49MOxQl56FSK',
            'jInMDucwEdEsP2KC',
            'OnMZUkVO87ZB4pRQ',
            'kc3IhydeFxUdINO4',
            'HpW72wH1wKWfjRyx',
            'HSKHzvtNeSK1CsWk',
            'NpsxxAEgUHL0aVV3',
            'MpwX749VXn1QksqO',
            'TDlxDy4BuSxAvtwl',
            'ACjB7160f1PHr3NZ',
            'iMWfOr5zmgUT7roS',
            'BDWTemvvTUMaEHkx',
            'BXQK1Rrl8FinB0az',
            'ZSO5FnEHrb5xlDea',
            'caTVm7Gj2NvwnWs7',
            'NN4ZrLftymzq4p5D',
            '0Q8QG2ieATX7913b',
            'VTwklWgZLapcbKfR',
            'NC9diKyL83vltnVq',
            'DzBlisUVlTyXQv4L',
            'WkdBibFaUIHIOiph',
            '1KQokc6fDLHBNNxd',
            'GTeMY5RAEHx4T3lU',
            'rdm8j9s8Ymtkwdnj',
            'BA4OH0hpQ1OgIymj',
            '7d5pcoH81TfyyGHF',
            'FVUDhSDxflLgGjoY',
            '6hYRExc6EN6bJMP5',
            '9yQMGiSgkarDFcfr',
            'ipI4unG84rrHYAVt',
            'qkiB34g5HHACXi7s',
            'GZDpWAtxbCZz5A8v',
            'db1qCjJmurs3u1kw',
            'EogKG7O4oVMOZ82x',
            'TUUNascl9bJLzbaM',
            'jmsuz6YCTasvUgh8',
            'N0eO00aOz7gKnlKj',
            'DiOUE9nGjkDPsGtD',
            'kuBNV00zlUbWH4Jw',
            'VrQZYEcLjyHAY9Ve',
            '48aXaWACd3unByLj',
            'NDIUjJqVMIvmWi3N',
            '42HhBpOndGdZ9Qu2',
            'NXhe7uJN9bGMZqLj',
            'WtevF5JxoCEKzQBN',
            'xpwXUwxyXSEGUrPG',
            'k9XoH5fM3VXmXil5',
            'uSCOB6lsh1k8m3U3',
            'mxLMkt8tXatKFV08',
            'BUA3VAdVzi57uKng',
            'VBBUZ2MPujP9POQL',
            'DBZ58entj7qdGm0k',
            'Fe0VyAn2dRojYJhv',
            'aWDjrpgH5QuuCzB9',
            '65LpaHEYjYAOfOlR',
            'pOzcVa5A1BMPOPtC',
            'Joh4iudcyJUkP0Lp',
            'rWJHPszp2eIfaigo',
            'HLrDusJTRb1AigOE',
            'OtYf2ltTDbl1b2nj',
            'PWIrsli1xpjXfNuC',
            '9WverOg3db1HaURn',
            'LABsXae2hCqTiIqS',
            'qpx6RQkELAQoykhW',
            'WEMI6uKesvYo5Co3',
            'UeER0MWMXRtUZFkj',
            'i9wAgQYpWDPPvIuP',
            'nLn4LC4cb0AXIEyt',
            'cHtHPltnAcHG6rQg',
            'vIKpsTxqdCwCH1jN',
            'tWaYHmJ2m3Wv91Ch',
            '24t13SIDIBl8EbkJ',
            'A1WnH6lziZGjnrhX',
            'cYiLrAwxxW067vGt',
            'I0nxzaHe9nWReDur',
            'ZvnoKd4vfAYLuHHI',
            'JrQ77lHVNbilSiWO',
            'WDK6QsJtDUD9Xgs9',
            'av2Q0qdfD7TRNEp4',
            '81oHFgTbKNCQ63d2',
            'KHIdwcjofIqE7frS',
            '8Oee9Syt5HjW3bTP',
            'SQQq3lTx27YT6lZd',
            '1SXLBsqBj6Y5cvO1',
            'xHpq6LiOVjS4nZlx',
            'cxFoqpQJu7c5skSA',
            'eVh25P2JjzOdB8cU',
            '8tw16I57YUIxhfWZ',
            'NAVgBXkTBBkxUKzU',
            'S0FsR1mHswIQys9f',
            'i8GXRgdbI1h5vJS2',
            'AHMCLnlVQJZYDq3W',
            'eV8HBXLTf6K1fPZC',
            'uvitcAmMIPz8VgPu',
            'jDEzQA61BRdUJvI1',
            '6N4JoRtvvnLzK3cJ',
            'KaLde1WcDTtRNTwE',
            '8Jgdv8uZkNt2Y1FY',
            'y3pJBv344dH4fj0h',
            '3eXdKUKqysXhclpO',
            'E0M4gaqLGPrsvJPk',
            'kvFkMJzV40GGl8bB',
            'iOSZboaiNxmPAYUm',
            'ZW0KAhTLZ8SGvclf',
            'DOZMzj9ZWNNrEkT0',
            'Eqeezql0LCc314Sg',
            'FmPORtHxRLu2bgww',
            'q2JLcNQWj6K7OXkP',
            '86rS5VXolfcRFvui',
            'u9UVG0nKiqcBJK3V',
            '3yzfXz0RJ0RvLkfx',
            'tAb4sGuvjcgbf2vI',
            'mN9sifm1EITN10NR',
            'x8eW7sdYpYzaWj8U',
            'pZfZXsm3P7MAvNIw',
            'GNvDcCv6RQW7eTXT',
            '9ud7LTuS8wt6Vevq',
            'PSD8A8zS1CO5E6Ew',
            'fWgxxzB70Z4OG713',
            'KwQ9rKFkQMa54zct',
            'gkpEJtrRvkIeP9h7',
            'Bzi35GqANEAm8qgL',
            'Q64xMb344QtlAqO0',
            '19tYL459GrxntwZD',
            'iQjwwsVYwuJotfmE',
            'st9tWYXcLcTjIkcm',
            '2jMwMasK9buUznHs',
            'qbA8AHVXzGCKK5cv',
            'HWaIZVy8CeGMv97l',
            'aXJDMcgVgLX25wzo',
            'njzqzoeI2cCvAbkT',
            'su1PWIbxjOwYnvWB',
            'l4IqNq33VFdiNAt1',
            'vUdKViIK07D7hAEt',
            'xJnS7zxTKSLMI10k',
            'G1cFdCy5ZpdklcUs',
            'tecPawCMTBpTH9OK',
            'zQeFbI3iWHBhLuOJ',
            'BNyjiaObTd3C8yDj',
            'aq33tcEa7NmvkI0W',
            'PVedxAH04uPOAI7K',
            '4wpwRWEMO7Ikhn3l',
            'MfI8k6SDhpAoq178',
            'Ve0qDdkqlnte3Cy5',
            'MdNi98Bxrz4v2JCO',
            '7EASi9OresdJWagd',
            'C5Tl6s6sYMylsSgx',
            'ozwQPaSv8BgThCTD',
            'jJRR5iJ5RgxsXyJL',
            'tjH7vy16tjLbaeYz',
            '39NVIyfBHyX5vABU',
            'IA7EnQuSmu6i9fmj',
            'czpGK28GWXAARy0v',
            'XR0zWDOyXjdFwzcc',
            'tyepizP6ZmD1PVlU',
            'LEYw2aQ2jUWQbOtA',
            'bvcatz6gVdTSB4VC',
            'j32z9GZiWnQ7ijj0',
            'hcX2IwOuhuJW5nUq',
            'BmWYOaXBOFFCfUxE',
            'kQ7v8O0VoD8CWTd5',
            'KexdEl8yjSjtuv4L',
            'Q3klv82TgGT6zRTm',
            'e0wX5J9uwqqYm3ah',
            'TjW3W6hqOR6Irk5E',
            'uO56ORimaUicNKWW',
            'howiocEUFcoiyjia',
            'vYXnp3geU6yzqIo6',
            '52vSGE1ydPTSelw3',
            'Hbn6382do3LUmM1Y',
            'Xxi3IWoojGZHqMXC',
            '7echNJzYmEcBxMjE',
            'G0gthSTGEGlmBoTT',
            'ugbOFjvbGKnkEEyK',
            'vuEPVF08UbboiC2a',
            'fa324sFU8UCfKIcw',
            '6brrJl3MDNeWjvys',
            'V6wp38KTPDrZFZ3b',
            'po7xKKr9djFaQKw9',
            'BGIFGCgRQGvgdcON',
            'qbIIrJhSkKS1HN9Z',
            's5wXkVBx8mPGZkIA',
            'hKcMVA0qOIEZsI1d',
            'KaRLBNWoYuzuTdqT',
            'DJuabP8LBwnw73ZD',
            'WST5fPmcoOJMkQpj',
            'k7FzZxTPdRUCrHUp',
            'hXbMJhssbdQCqQsO',
            'ops6ii2ThNl1RxBq',
            'lXNFl93aVxq1N5T6',
            'iICo9qjImWuMXYcW',
            'ZtqPbyrTwdXD5Ibp',
            'hrozhv76rw9j98gB',
            'bf4vAuqr66C5Dr62',
            '1Dk7dphGZLyLaMDZ',
            'zwLRHvFzoja55xAg',
            'BVD8CbHvVnyxVIwJ',
            'HCXgYxnK7g1PROkx',
            'OruAQN8amqZ3N30u',
            'vtwjHt6sKVISsqC',
            '7XW93FXTDLcR9IiO']
    return iv[iv_n]

#Main part
opt = int(input("Prima 1 para encriptar o ficheiro\nPrima 2 para desencriptar o ficheiro: "))
if opt == 1:
    #Input values
    f_p_e = input("Insira o nome do ficheiro: ")
    password = input("Insira a password: ")
    f_e = input("Insira o nome do ficheiro encriptado: ")
    #Load a random iv string
    iv_n = random.randint(0,255)
    print("IV = " + str(iv_n))
    #Encrypt
    encryp_aes(password, f_p_e, loadIV(iv_n), f_e)
elif opt == 2:
    #Input values
    f_p_d = input("Insira o nome do ficheiro encriptado: ")
    password = input("Insira a password: ")
    f_d = input("Insira o nome do ficheiro desencriptado: ")
    #Load the iv string
    iv_n = int(input("Insira o número de IV: ").encode('utf-8'))
    #Decrypt
    decryp_aes(password, f_p_d, loadIV(iv_n), f_d)
else:
    print("Erro, adios")