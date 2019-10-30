from app import register_app

server = register_app('development')

if __name__ == '__main__':
    server.run()
