
#!/bin/sh

mkdir /epics/ioc/config
cp -r /mnt/* /epics/ioc/config/
echo "=== configuration yaml ======="
cat /mnt/__docker__/mrf-evg/config.yaml
echo "=============================="
cd /epics/ioc/config
find . -name "*.j2" -exec sh -c 'jnjrender "$1" __docker__/mrf-evg/config.yaml --output "${1%.j2}"' _ {} \;
cp -r /epics/ioc/config /mnt/__docker__/mrf-evg/ ## copy the rendered files to the docker volume

mkdir -p /nfs/data/mrf-evg


mkdir -p /nfs/autosave/mrf-evg


mkdir -p /nfs/config/mrf-evg

cp -r /epics/ioc/config/* /nfs/config/mrf-evg/



/epics/ioc/start.sh
