import os

if __name__ == '__main__':
    os.environ['__PACKAGE_NAME__'] = 'SyncView'
    os.environ['__SECRET_KEY__'] = 'Dr4N5fXz6P88LcYvcfnCtlCK3-qoaisD6gQmz-kQj2c='
    os.environ['release_version'] = '1.0.2'

    from core.app import App

    app = App('SyncView')
    app.run()
    app.MainLoop()
