# coding=utf-8

import os
import sys
import shutil
import subprocess

if '--full' in sys.argv:
    BUILD = NSI = COMPRESS = True
    CLEAR = False
else:
    BUILD = '--build' in sys.argv
    CLEAR = '--clear' in sys.argv
    NSI = '--nsi' in sys.argv
    COMPRESS = '--zip' in sys.argv
CONDA_FOLDER = r'conda'
OS_VERSION = '4.1.0'
BUILD_VERSION = '2'
MAKENSIS = r'..\nsis-3.05\makensis.exe'
ZIP = r'..\7zip\7za.exe'
ENV_TARGET = CONDA_FOLDER + r'\opensesame_{version}'
ZIP_TARGET = 'opensesame_{}.zip'
BAT_TMPL = r'bat-tmpl\py3.bat.tmpl'
NSI_TMPL = r'nsi\py3.nsi.tmpl'
ENV_YAML = r'env\py313.yaml'
ENV_FOLDER = CONDA_FOLDER + r'\opensesame-41\\'
PIP_REQS = r'pip_reqs\py313.txt'
VERSION = OS_VERSION + '-py313-win64-' + BUILD_VERSION
if CLEAR:
    print('Clearing environments')
    shutil.rmtree(CONDA_FOLDER)
    os.mkdir(CONDA_FOLDER)
    print('Done')
# First build the environment
print('Creating build.bat')
with open(BAT_TMPL) as fd:
    tmpl = fd.read()
with open('build.bat', 'w') as fd:
    fd.write(
        tmpl.format(
            env_folder=ENV_FOLDER,
            env_yaml=ENV_YAML,
            pip_reqs=PIP_REQS,
            version=VERSION
        )
    )
if BUILD:
    print('Running build.bat')
    subprocess.run(['build.bat'])
if NSI:
    # Now build the installer
    print('Creating build.nsi')
    with open(NSI_TMPL) as fd:
        tmpl = fd.read()
    with open('build.nsi', 'w') as fd:
        fd.write(tmpl.format(env_folder=ENV_FOLDER, version=VERSION))
    print('Compiling build.nsi')
    subprocess.run([MAKENSIS, '/V4', '/P3', 'build.nsi'])
if COMPRESS:
    # And then zip the environment
    print('Moving environment')
    os.rename(ENV_FOLDER, ENV_TARGET.format(version=VERSION))
    print('Zipping environment')
    subprocess.run([
        ZIP,
        'a',
        '-y',
        ZIP_TARGET.format(VERSION),
        os.path.abspath(ENV_TARGET.format(version=VERSION))
    ])
    print('Done!')
