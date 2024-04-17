
# How to run examples

```
yum install -y podman
```

Build image.

```
podman build -t tomldemo .
```

Run command and check file cluster.toml before and after

```
 podman run --security-opt label=disable  -it --rm --name my-running-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp tomldemo  python read_write.py
```
