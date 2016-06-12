from DES.Key import Key
class Run:
    def __init__(self):
        self.choice = ''
        self.key_text = ''
        self.plaintext = ''
        self.cipher = ''
        self.key = None

    def enter_key(self):
        while 1:
            self.key_text = str(input('Enter the key -- 8 characters string and input "quit" back to\n>>'))

            if self.key_text.lower() == 'quit':
                return False
            elif len(self.key_text) == 8:
                break
            print('Key must be 8 characters in length. Exiting...')
        return True

    def if_continue(self):
        print("*********************")
        flag = input("do you want to continue[Y/N]\n>>")
        if flag.lower() == 'n':
            print("See You!")
            exit()
        print("\n")

    def run(self):
        self.key = Key(1)
        while 1:
            print('Enter the choice')
            print('A. ENCRYPT A MESSAGE')
            print('B. DECRYPT A MESSAGE')
            print("C. EXIT")
            self.choice = input('>>')

            if self.choice.lower() == 'a':
                if not self.enter_key():
                    continue
                self.plaintext = str(input('Enter the message(in Text-form)\n>>'))
                self.cipher = self.key.encrypt(self.plaintext, self.key_text)
                print('the cipher is(in hex-decimal form)\n[+] %s' % self.cipher)
                #print(self.cipher)
                self.if_continue()
                continue

            elif self.choice.lower() == 'b':
                print("please wait\n")
                continue
                if not self.enter_key():
                    continue
                self.cipher = str(input('Enter the message(in hex-decimal form)\n>>'))
                self.plaintext = self.key.decrypt(self.cipher, self.key_text)
                print('the original text is\n[+]')
                print(self.plaintext)
                self.if_continue()
                continue

            elif self.choice.lower() == 'c':
                exit()

            else:
                print("Please enter again\n")