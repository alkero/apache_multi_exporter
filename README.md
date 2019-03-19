# apache_multi_exporter
Python Prometheus exporter for multiple Apache instances

It uses Python Bottle framework.



Prometheus Configuration:

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
        replacement: localhost:8767  # The apache exporter
