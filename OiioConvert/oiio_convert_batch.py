import subprocess, os, sys, re
from datetime import datetime

startTime = datetime.now()

oiioTool = "/Applications/Houdini/Houdini19.5.435/Frameworks/Houdini.framework/Versions/19.5/Resources/bin/hoiiotool"

inputDir = ''

inputFiles = [f for f in os.listdir(inputDir) if f[-4:] == '.exr' ]

subprocesses = []

os.mkdir(os.path.join(inputDir,'jpg'))

for file in inputFiles:

    input = os.path.join(inputDir,file)
    outputFileName = file[:-3] + 'jpg'
    output = os.path.join(inputDir,'jpg',outputFileName)

    command = [oiioTool, '-i:subimages=\"RGBA\"', input, '--colorconvert', 'ACES - ACEScg', 'Output - Rec.709', '--ch', 'R,G,B', '-o', output]

    process = subprocess.Popen(command, env=dict(os.environ, OCIO="colour-science OpenColorIO-Configs master aces_1.2/config.ocio"), stdout=subprocess.PIPE)

    subprocesses.append(process)

    # process.wait()

    # print('Converted ' + outputFileName[:-4])

    # lines_iterator = iter(process.stdout.readline, b"")
    # for line in lines_iterator:
    #     print(line.decode("utf-8").strip())
    #     sys.stdout.flush()

exit_codes = [p.wait() for p in subprocesses]
print('Done!')
print(datetime.now() - startTime)
#my_env = {**os.environ, **dict_with_env_variables}
