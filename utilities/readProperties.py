import configparser

config = configparser.RawConfigParser()
# config.read(".\\Configuration\\config.ini")
config.read("/home/mohit/SDET/Hybrid_Pytest_Framework/LearnHybridFrameworkDesign/Configuration/config.ini")



class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
