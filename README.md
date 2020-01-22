# Flask Helm Chart

This is meant to be a standard helm chart for a simple Flask based application

SET these values on install, either directly or with a `values.yaml`, and example override file is `example_override.yaml`

configs:
    HOST:
    USER:
    PASSWORD:

    helm install ... --set configs.HOST=192.168.1.1 --set configs.USER=user ...

