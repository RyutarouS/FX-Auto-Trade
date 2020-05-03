from oandapyV20 import API


class ApiUtils:
    accountID: str = None
    access_token: str = None
    environment: str = None
    
    def __init__(self, id: str, token:str, env: str):
        self.accountID = id
        self.access_token = token
        self.environment = env
    
    def create_api(self) -> API:
        if self.access_token is None or self.environment is None:
            # Error 処理
            return None
        return API(access_token= self.access_token, environment= self.environment)
