# coding=utf-8

import os
import sys
import shutil
import subprocess

if '--full' in sys.argv:
    CLEAR = NSI = COMPRESS = True
else:
    CLEAR = '--clear' in sys.argv
    NSI = '--nsi' in sys.argv
    COMPRESS = '--zip' in sys.argv
CONDA_FOLDER = r'conda'
OS_VERSION = '3.3.0a61'
BUILD_VERSION = '1'
MAKENSIS = r'..\nsis-3.05\makensis.exe'
ZIP = r'..\7zip\7za.exe'
ENV_TARGET = CONDA_FOLDER + r'\opensesame_{version}'
if '--py27' in sys.argv:
    BAT_TMPL = r'bat\build-env-py27.bat.tmpl'
    NSI_TMPL = r'nsi\py2.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py27\\'
    VERSION = OS_VERSION + '-py27-win64-' + BUILD_VERSION
elif '--py36' in sys.argv:
    BAT_TMPL = r'bat\build-env-py36.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py36\\'
    VERSION = OS_VERSION + '-py36-win64-' + BUILD_VERSION
elif '--py37' in sys.argv:
    BAT_TMPL = r'bat\build-env-py37.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py37\\'
    VERSION = OS_VERSION + '-py37-win64-' + BUILD_VERSION
else:
    raise ValueError('Please specify a target')

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
    fd.write(tmpl.format(env_folder=ENV_FOLDER))
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
        'opensesame_{}.zip'.format(VERSION),
        os.path.abspath(ENV_TARGET.format(version=VERSION))
    ])
    print('Done!')
