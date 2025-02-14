# NERV
import bio
import brut
def display_banner():
    print('''
  _   _ ______ _______      ___                _   
 | \ | |  ____|  __ \ \    / / |              | |  
 |  \| | |__  | |__) \ \  / /| |__  _ __ _   _| |_ 
 | . ` |  __| |  _  / \ \/ / | '_ \| '__| | | | __|
 | |\  | |____| | \ \  \  /  | |_) | |  | |_| | |_ 
 |_| \_|______|_|  \_\  \/   |_.__/|_|   \__,_|\__|
                                                                                                                  
    ''')
    print("===================================")
    print("       Brute force NERVbrut        ")
    print("===================================")
    print("1.-Запустить Brut-атаку")
    print("2.-О туле")

def main():
    while True:
        display_banner()
        choice = input("Выберите дейстиве: ")

        if choice == '1':
            brut.run()
        elif choice == "2":
            bio.run()

            break
        else:
            print("Неверный ввод. Пожалуйста, выберите номер от 0 до 5.")

if __name__ == "__main__":
    main()

