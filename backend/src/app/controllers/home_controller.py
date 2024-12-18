from flask import jsonify
import logging

class HomeController:
    def index(self):
        logging.info("----HomeController.index----")
        return jsonify({"message": "Welcome!"})
    
home_controller = HomeController()