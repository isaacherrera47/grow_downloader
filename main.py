import subprocess
from sys import argv


def print_help():
    print("""Download and unzip grow version into bin folder. By default is downloaded last version before 1.0
Use -b or --build to specify a version. i.e. -b 0.8.0
List of available versions:
{0}""".format("\n".join(GROW_BUILDS)))


def get_builds():
    version = '0.{}.{}'
    result = []
    for x in GROW_NUM_BUILDS.keys():
        for i in range(GROW_NUM_BUILDS[x], -1, -1):
            result.append(version.format(x, i))
    return result


def run_process():
    version = argv[2] if len(argv) >= 3 else GROW_BUILDS[0]
    print(f'Trying to fetch {version} from github :)...')
    subprocess.call(f'./run.sh {version} {version.split(".")[1]}', shell=True)


GROW_NUM_BUILDS = {
    8: 25,
    7: 6,
    5: 5
}
GROW_BUILDS = get_builds()
commands = {
    '--help': print_help,
    '-h': print_help,
    '--build': run_process,
    '-b': run_process
}


def main():
    if len(argv) == 1:
        print('No parameters were used. Downloading the last version...')
        return run_process()
    command = commands.get(argv[1])
    if command is None:
        return print('Invalid parameter :( Use --help or -h for more information.')

    return command()


if __name__ == '__main__':
    main()
