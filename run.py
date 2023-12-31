
# Internal imports
from app import create_app
from decl import MODE
from utl.logger import Logger

# Third party library
from waitress import serve

logger = Logger()


if __name__ == '__main__':
    app = create_app()

    if MODE == "PRODUCTION":
        serve(app, host='0.0.0.0', port=5000)
    elif MODE == "DEBUG":
        app.run(ssl_context="adhoc")
    else:
        logger.critical("Invalid Mode")
        exit(134)

