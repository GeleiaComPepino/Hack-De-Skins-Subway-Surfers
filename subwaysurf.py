import subprocess, pathlib, shutil
import time
path = f'{pathlib.Path(__file__).parent.absolute()}'.replace("\\","/") + "/" + "bin"
path2 = path + "/" + "ADB"
escolha1 = input('''
1 - Personagem
2 - Skate (Custom)
3 - Moeda (Custom) (Limite: 999999999)
Qual a sua escolha? ''')
if escolha1 == '1':

    escolha2 = input('''
    1 - Yutani
    2 - Super Runner Jake
    3 - Bob The Blob
    4 - Koral
    5 - Trym
    6 - Lana
    7 - Tankbot
    8 - Lauren
    9 - Kareem
    10 - Freya
    11 - Dino
    12 - Miss Maia
    13 - Prince K
    14 - Brody
    15 - Ella
    16 - Zoe
    17 - King
    18 - Frank
    19 - Tasha
    20 - Ninja
    21 - Tagbot
    22 - Lucy
    23 - Spike
    24 - Fresh
    25 - Tricky
    26 - Boombot
    27 - Customizado
    Qual a sua escolha? ''')
    if escolha2 == '1':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Yutani/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '2':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Super Runner Jake/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '3':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Bob The Blob/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '4':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Koral/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '5':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Trym/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '6':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Lana/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '7':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Tankbot/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '8':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Lauren/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '9':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Kareem/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '10':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Freya/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '11':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Dino/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '12':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Miss Maia/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '13':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Prince K/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '14':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Brody/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '15':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Ella/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '16':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Zoe/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '17':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/King/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '18':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Frank/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '19':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Tasha/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '20':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Ninja/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '21':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Tagbot/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '22':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Lucy/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '23':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Spike/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '24':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Fresh/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '25':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Tricky/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '26':
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{path}/Boombot/characters_inventory.json" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
    if escolha2 == '27':
        pergunta = input('Digite o nome do personagem: ')
        file_path = "C:/Users/DESKTOP_BRY/OneDrive/Área de Trabalho/Python/SubwaySurfers/bin/Custom/characters_inventory.json"
        arquivo = open(file_path, 'r')
        for line in arquivo:
            arquivo = open(file_path, 'w')
            arquivo.write(line.replace('bobTheBlob',f'{pergunta}'))
            subprocess.Popen(f'{path2}/adb.exe devices')
            subprocess.Popen(f'{path2}/adb.exe push "{file_path}" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
            subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
            subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
            arquivo.close()
            time.sleep(20)
            source=f'{path}/Bob The Blob/characters_inventory.json'
            shutil.copyfile(source, file_path)
            print('Personagem customizado com sucesso!')
            break
elif escolha1 == '2':
    escolha2 = input('Digite o nome do skate: ')
    file_path = "C:/Users/DESKTOP_BRY/OneDrive/Área de Trabalho/Python/SubwaySurfers/bin/Custom/boards_inventory.json"
    arquivo2 = open(file_path, 'r')
    for line in arquivo2:
        arquivo = open(file_path, 'w')
        arquivo.write(line.replace('birthday2022',f'{escolha2}'))
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{file_path}" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
        arquivo.close()
        time.sleep(20)
        source=f'{path}/Bob The Blob/boards_inventory.json'
        shutil.copyfile(source, file_path)
        print('Skate customizado com sucesso!')
        break
elif escolha1 == '3':
    escolha2 = input('Digite quantas moedas você quer: ')
    file_path = "C:/Users/DESKTOP_BRY/OneDrive/Área de Trabalho/Python/SubwaySurfers/bin/Custom/wallet.json"
    arquivo2 = open(file_path, 'r')
    for line in arquivo2:
        arquivo = open(file_path, 'w')
        arquivo.write(line.replace('167234',f'{escolha2}'))
        subprocess.Popen(f'{path2}/adb.exe devices')
        subprocess.Popen(f'{path2}/adb.exe push "{file_path}" /storage/emulated/0/Android/data/com.kiloo.subwaysurf/files/profile')
        subprocess.Popen(f'{path2}/adb.exe shell am force-stop com.kiloo.subwaysurf')
        subprocess.Popen(f'{path2}/adb.exe shell monkey -p com.kiloo.subwaysurf 1')
        arquivo.close()
        time.sleep(20)
        source=f'{path}/Bob The Blob/wallet.json'
        shutil.copyfile(source, file_path)
        print('Moedas customizadas com sucesso!')
        break