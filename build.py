# coding=utf-8

import os
import sys
import subprocess

CONDA_FOLDER = r'C:\Users\P279200\.conda'

if '--py2' in sys.argv:
    BAT_TMPL = r'bat\build-env-py2.bat.tmpl'
    NSI_TMPL = r'nsi\py2.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\envs\rapunzel-py2\\'
    MAKENSIS = r'..\nsis-3.05\makensis.exe'
    ZIP = r'C:\Program Files\7-Zip\7z.exe'
    VERSION = '3.3.0a56-py2-win64-1'
    ENV_TARGET = CONDA_FOLDER + r'\envs\opensesame_{version}'
else:
    BAT_TMPL = r'bat\build-env.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_FOLDER = CONDA_FOLDER + r'\envs\rapunzel\\'
    MAKENSIS = r'..\nsis-3.05\makensis.exe'
    ZIP = r'C:\Program Files\7-Zip\7z.exe'
    VERSION = '3.3.0a56-py3-win64-1'
    ENV_TARGET = CONDA_FOLDER + r'\envs\opensesame_{version}'


# First build the environment
print('Creating build.bat')
with open(BAT_TMPL) as fd:
    tmpl = fd.read()
with open('build.bat', 'w') as fd:
    fd.write(tmpl.format(env_folder=ENV_FOLDER))
print('Running build.bat')
subprocess.run(['build.bat'])

# Now build the installer
print('Creating build.nsi')
with open(NSI_TMPL) as fd:
    tmpl = fd.read()
with open('build.nsi', 'w') as fd:
    fd.write(tmpl.format(env_folder=ENV_FOLDER, version=VERSION))
print('Compiling build.nsi')
subprocess.run([MAKENSIS, '/V4', '/P3', 'build.nsi'])

# And then zip the environment
print('Moving environment')
os.rename(ENV_FOLDER, ENV_TARGET.format(version=VERSION))
print('Zipping environment')
subprocess.run([
    ZIP,
    'a',
    '-y',
    'opensesame_{}.zip'.format(VERSION),
    ENV_TARGET.format(version=VERSION)
])
print('Done!')
