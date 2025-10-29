import uuid

from flask import request, Blueprint
from core.logger import init_logger
from core.settings import get_settings
import os, requests
from core.response.response_schema import response_base


settings = get_settings()
bp = Blueprint('http_api', __name__)
logger = init_logger("funasr_api")

@bp.route('/api/say_hello', methods=['GET'])
def hello_world():
    print('hello world')
    return 'hello world'

@bp.route('/api/sync/file', methods=['POST'])
def sync_file():
    try:
        if 'file' not in request.files:
            logger.error('No file provided')
            return response_base.fail(data='No file provided')
        file = request.files['file']
        if file.filename == '':
            logger.error('No selected file')
            return response_base.fail(data='No selected file')

        os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
        filename = f"{uuid.uuid4().hex}_{file.filename}"
        save_path = os.path.join(settings.UPLOAD_DIR, filename)
        file.save(save_path)
        logger.info(f"File saved: {save_path}")

        return response_base.fast_success()

    except requests.exceptions.RequestException as e:
        logger.error(f"sync file failed: {str(e)}")
        return response_base.fail(data=f"sync file failed: {str(e)}")
    except Exception as e:
        logger.exception(f"Internal server error: {str(e)}")
        return response_base.fail(data=f"Internal server error: {str(e)}")