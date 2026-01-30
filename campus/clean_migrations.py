import os
import shutil

apps = ['accounts', 'activities', 'participation', 'certificates', 'report', 'core', 'dashboard', 'notification']
base_dir = r'c:\cams\campus'

for app in apps:
    migrations_dir = os.path.join(base_dir, app, 'migrations')
    if os.path.exists(migrations_dir):
        for filename in os.listdir(migrations_dir):
            if filename != '__init__.py' and filename != '__pycache__':
                file_path = os.path.join(migrations_dir, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}. Reason: {e}")
    else:
        print(f"No migrations dir for {app}")
