from typing import Dict

FileName = str
user_info = dict()                                                           # type: Dict[str, str]

def passwd_to_dict(filename:FileName)->None:
    with open(filename) as passwd_file:
        for line in passwd_file:
            if not line.startswith(('#', '\n')):
                info = line.split(':')
                username, password = info[0], info[2]
                user_info[username] = password

if __name__ == "__main__":
    passwd_to_dict('passwd.txt')
    print(user_info)