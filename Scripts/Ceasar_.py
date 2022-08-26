import datetime
import string
import pyfiglet


class CC:
    def __new__(cls, *args, **kwargs):
        global full_date
        info = 'Encrypter_V01'
        full_date = datetime.datetime.now().strftime("%Y/%m/%d")
        print(pyfiglet.figlet_format(info))
        print('_' * 80)
        print(f'[+] Date: {full_date}')
        print('-' * 80)
        return object.__new__(cls)

    def __str__(self):
        info = f'[+] {self.__class__.__name__}'
        return info

    def __repr__(self):
        return self.__str__()

    def __init__(self, phrase: str, n: int) -> None:
        self.Phrase: str = phrase
        self.Constant: int = n
        self.Code: str = ''
        self.Old_Position: int = 0
        self.New_Position: int = 0
        self.Encrypted: str = ''
        self.Decrypted: str = ''
        self.Unencrypted: str = ''
        self.File_Path: str = r'../Encrypted/Encrypted.txt'
        self.Full_Date = full_date
        self.Verification: bool = False
        return

    def encrypt(self) -> str:
        try:
            if len(self.Phrase) > 0 and self.Constant > 0:
                for letter in self.Phrase:
                    letter = letter.lower()
                    if letter == ' ':
                        self.Encrypted += letter
                    else:
                        if letter in string.ascii_letters:
                            self.Old_Position = string.ascii_letters.find(letter)
                            self.New_Position = self.Old_Position + self.Constant
                            self.Encrypted += string.ascii_letters[self.New_Position]
                self.Verification = True
                print('[+] Encrypted Successfully!')
            else:
                raise Exception("[!!] Sorry, Invalid Parameter!")
        except Exception as Error:
            print(f"[!!] {Error}")
        return self.Encrypted

    def decrypt(self) -> str:
        try:
            if len(self.Phrase) and self.Constant > 0:
                for letter in self.Phrase:
                    letter = letter.lower()
                    if letter == ' ':
                        self.Decrypted += letter
                    else:
                        if letter in string.ascii_letters:
                            self.Old_Position = string.ascii_letters.find(letter)
                            self.New_Position = self.Old_Position - self.Constant
                            self.Decrypted += string.ascii_letters[self.New_Position]
                print('[+] Decrypted Successfully!')
            else:
                raise Exception('[!!] Sorry, Invalid Parameter!')
        except Exception as Error:
            print(f'{Error}')
        return self.Decrypted

    def upload(self):
        with open(self.File_Path, 'a') as doc:
            doc.write(f'[+] Date {full_date} : {self.Phrase} = {self.Encrypted}\n')
            doc.write('_' * 80)
            doc.write('\n')
            doc.close()
        print('[+] Save Process Complete!')
        return

    def update(self):
        print('[+] [1] Encrypt: ')
        print('[+] [2] Decrypt: ')
        print('_' * 80)
        while True:
            selection = input('[+] Select a option:')
            while selection == '':
                selection = input('[+] Select a option:')
            if int(selection) == 1:
                self.encrypt()
                self.upload()
                print(f'[+] Encrypted Word : {self.Encrypted}.')
            elif int(selection) == 2:
                if selection == 2:
                    self.decrypt()
            else:
                print('[!!]Option not Found!')
            return


if __name__ == '__main__':
    CC('Bruno', 13).update()
