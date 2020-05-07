# -*- mode: python ; coding: utf-8 -*-

block_cipher = None
import platform

def get_resources():
    data_files = []
    for file_name in os.listdir('resources'):
        data_files.append((os.path.join('resources', file_name), 'resources'))
    for file_name in os.listdir('resources\img'):
        data_files.append((os.path.join('resources\img', file_name), 'resources\img'))
    return data_files

def get_binaries():
    os_name = platform.system()
    lib_name = 'bar.so'
    if os_name == 'Windows':
        lib_name = 'bar.dll'
    elif os_name == 'Darwin':
        lib_name = 'bar.dylib'
    return [(os.path.join('bin', lib_name), '')]

a = Analysis(['app.py'],
             pathex=['C:\\Projetos\\Python\\SyncView'],
             binaries=[],
             datas=get_resources(),
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SyncView',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Projetos\\Python\\SyncView\\resources\\Icon.ico')

if platform.system() == 'Darwin':
    info_plist = {'addition_prop': 'additional_value'}
    app = BUNDLE(exe,
                 name='Foobar.app',
                 bundle_identifier=None,
                 info_plist=info_plist
                )
