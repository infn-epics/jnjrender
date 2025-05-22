
#!/bin/sh

mkdir /epics/ioc/config
cp -r /mnt/* /epics/ioc/config/
echo "=== configuration yaml ======="
cat /mnt/__docker__/mrf-rf-delay/config.yaml
echo "=============================="
cd /epics/ioc/config
find . -name "*.j2" -exec sh -c 'jnjrender "$1" __docker__/mrf-rf-delay/config.yaml --output "${1%.j2}"' _ {} \;
cp -r /epics/ioc/config /mnt/__docker__/mrf-rf-delay/ ## copy the rendered files to the docker volume

mkdir -p /nfs/data/mrf-rf-delay


mkdir -p /nfs/autosave/mrf-rf-delay


mkdir -p /nfs/config/mrf-rf-delay

cp -r /epics/ioc/config/* /nfs/config/mrf-rf-delay/



/epics/ioc/start.sh
