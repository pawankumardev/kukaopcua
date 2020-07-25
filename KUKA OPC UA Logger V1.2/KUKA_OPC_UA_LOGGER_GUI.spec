# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['KUKA_OPC_UA_LOGGER_GUI.py'],
             pathex=['C:\\Users\\PawankumarGurav\\Desktop\\IIT Khargapur-RealTime OPC\\KUKA OPC UA Logger V1.2'],
             binaries=[],
             datas=[],
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
          name='KUKA_OPC_UA_LOGGER_GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
