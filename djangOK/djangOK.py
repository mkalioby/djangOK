import sys
import os

def setup_django(manage_folder='.'):
    try:
        subprocess.check_call(['python', 'manage.py', 'check'])
        exit(0)
    except Exception:
        import traceback
        print(traceback.format_exc())
        exit(-1)


if __name__=='__main__':
    setup_django(sys.argv[1])
