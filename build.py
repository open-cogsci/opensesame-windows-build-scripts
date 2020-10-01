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
FROZEN = '--frozen' in sys.argv
CONDA_FOLDER = r'conda'
OS_VERSION = '3.3.4a13'
RAPUNZEL_VERSION = '0.4.11'
BUILD_VERSION = '1'
MAKENSIS = r'..\nsis-3.05\makensis.exe'
ZIP = r'..\7zip\7za.exe'
ENV_TARGET = CONDA_FOLDER + r'\opensesame_{version}'
ZIP_TARGET = 'opensesame_{}.zip'
if '--py27' in sys.argv:
    BAT_TMPL = r'bat-tmpl\py2.bat.tmpl'
    NSI_TMPL = r'nsi\py2.nsi.tmpl'
    ENV_YAML = r'env\py27.yaml'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py27\\'
    PIP_REQS = r'pip_reqs\py27.txt'
    VERSION = OS_VERSION + '-py27-win64-' + BUILD_VERSION
elif '--py37' in sys.argv:
    BAT_TMPL = r'bat-tmpl\py3.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_YAML = r'env\py37.yaml'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py37\\'
    PIP_REQS = r'pip_reqs\py37.txt'
    VERSION = OS_VERSION + '-py37-win64-' + BUILD_VERSION
elif '--py37-megapack' in sys.argv:
    BAT_TMPL = r'bat-tmpl\py3.bat.tmpl'
    NSI_TMPL = r'nsi\py3.nsi.tmpl'
    ENV_YAML = r'env\py37-megapack.yaml'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py37-megapack\\'
    PIP_REQS = r'pip_reqs\py37-megapack.txt'
    VERSION = OS_VERSION + '-py37-megapack-win64-' + BUILD_VERSION
elif '--py38-rapunzel' in sys.argv:
    BAT_TMPL = r'bat-tmpl\rapunzel.bat.tmpl'
    NSI_TMPL = r'nsi\rapunzel.nsi.tmpl'
    ENV_YAML = r'env\py38-rapunzel.yaml'
    ENV_FOLDER = CONDA_FOLDER + r'\rapunzel-py38-rapunzel\\'
    PIP_REQS = r'pip_reqs\py38-rapunzel.txt'
    VERSION = RAPUNZEL_VERSION + '-py38-win64-' + BUILD_VERSION
    ENV_TARGET = CONDA_FOLDER + r'\rapunzel_{version}'
    ZIP_TARGET = 'rapunzel_{}.zip'
else:
    raise ValueError('Please specify a target')
if FROZEN:
    BAT_TMPL = BAT_TMPL.replace('\\', r'\frozen-')
    ENV_YAML = ENV_YAML.replace('\\', r'\frozen-')

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
