Vendor dependencies until they are availble on the public Internet.

mkdir -p vendor
pip install --download vendor -r requirements.txt --no-binary :all:

