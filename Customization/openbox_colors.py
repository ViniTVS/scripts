#!/usr/bin/python3
import os


def main():
    # Get environment variables
    home = os.getenv('HOME')
    themes_path = f"{home}/.themes/CustomPixels/openbox-3"
    wal_path = f"{home}/.cache/wal/colors"
    # verifica se a pasta para o tema e arquivos do pywal existem 
    if not (os.path.isdir(themes_path) and os.path.isfile(wal_path)):
        print("Arquivos principais do tema não encontrados")
        return -1
    
    colors = []
    colors_file = open(wal_path, "r")
    for line in colors_file:
        colors.append(line.replace("\n", "").upper())
    colors_file.close()
    
    theme_file = open("themerc", "r")
    theme_data = theme_file.read()
    for i, cor in enumerate(colors):
        # print("{color" + str(i) + "}")
        theme_data = theme_data.replace("{color" + str(i) + "}", cor)
    theme_file.close()

    theme_file = open(f"{themes_path}/themerc", "w")
    theme_file.write(theme_data)
    theme_file.close()

    os.system("openbox --reconfigure")



if __name__ == "__main__":
    main()