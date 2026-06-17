from flask import jsonify, Flask
from pydantic import ValidationError
from werkzeug.exceptions import BadRequest

from .logger import logger
from .exceptions import DatabaseError, InternalServerError, ResourceNotFoundError

def register_error_handlers(app: Flask) -> None:

    @app.errorhandler(InternalServerError)
    def handle_internal_server_error(e):
        logger.exception(f"{type(e)}: {e}")
        return jsonify({"error": "Internal Server Error"}), 500
        
    @app.errorhandler(DatabaseError)
    def handle_db_error(e):
        return handle_internal_server_error(e)
    
    @app.errorhandler(ResourceNotFoundError)
    def handle_resource_not_found(e):
        return jsonify({'error': str(e)}), 404
    
    @app.errorhandler(ValidationError)
    def handle_validation_error(e):
        return jsonify({"errors": str(e.errors())}), 400
        
    @app.errorhandler(BadRequest)
    def handle_bad_request(e):
        return jsonify({"error": str(e.description)}), e.code or 500
    
    @app.errorhandler(KeyError)
    def handle_key_error(e):
        return handle_resource_not_found(f"Resource not found: {e}")