from flask import jsonify
import logging

class AuthController:
    def register(self):
        logging.info("----Auth_controller.register----")
        ## TODO:實現註冊邏輯
         
        return jsonify({"message": "User registered successfully"})
    
    def login(self):
        logging.info("----Auth_controller.login----")
        ## TODO: 實現登入邏輯
         
        return jsonify({"message": "User logged in successfully"})
    
    def logout(self):
        logging.info("----Auth_controller.logout----")
        ## TODO: 實現登出邏輯
         
        return jsonify({"message": "User logged out successfully"})
    

auth_controller = AuthController()