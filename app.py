from aiohttp import web
import pathlib
import argparse
from dotenv import load_dotenv
import os
import logging

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='Port to run on (default: 8087)')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    return parser.parse_args()

async def handle_favicon(request):
    return web.Response(status=204)

async def handle_index(request):
    return web.FileResponse('./public/index.html')

def init_app():
    app = web.Application()
    logging.debug('Initializing application...')
    public_path = pathlib.Path('./public')
    app.router.add_get('/', handle_index)
    app.router.add_static('/', public_path)
    app.router.add_get('/favicon.ico', handle_favicon)
    return app

if __name__ == '__main__':
    load_dotenv()
    args = parse_args()
    
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    app = init_app()
    port = args.port or int(os.getenv('PORT', 8087))
    logging.info(f'Starting server on port {port}')
    web.run_app(app, host='127.0.0.1', port=port)
