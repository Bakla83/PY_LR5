import re
import random


def generate_ipv4():
    if random.randint(1, 10) <= 3:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(3)) + ".abc"
    else:
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip


def is_valid_ipv4(ip):
    ipv4_regex = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return re.match(ipv4_regex, ip) is not None


def validate_ipv4(ip):
    if not is_valid_ipv4(ip):
        raise ValueError("Некорректный формат IP-адреса IPv4")
    return ip


random_ip = generate_ipv4()
print(f"Сгенерированный IP-адрес: {random_ip}")

try:
    valid_ip = validate_ipv4(random_ip)
    print(f"Введенный IP-адрес {valid_ip} корректен.")
except ValueError as e:
    print(e)
