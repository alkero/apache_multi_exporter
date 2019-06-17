# apache_multi_exporter
Python Prometheus exporter for multiple Apache instances.

It uses Python Bottle framework.


server-status should be configured on the Apache instances.


Installation

```
wget http://bottlepy.org/bottle.py
wget https://raw.githubusercontent.com/alkero/apache_multi_exporter/master/apache_multi_exporter.py
nohup python ./app.py &
```


Prometheus Configuration

```
  - job_name: 'apache'
    metrics_path: /metrics
    static_configs:
    - targets: [ "http://apache1:8080", "https://apache2:311" ]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: localhost:8080  # The apache exporter
```
Replace localhost with the name of the server where apache_multi_exporter is installed.
