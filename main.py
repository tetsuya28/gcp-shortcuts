# coding: utf-8

import sys
import json
import os

baseURL = "https://console.cloud.google.com/"
services = [
    {
        "service": "AlloyDB",
        "dir": "",
        "path": "alloydb/clusters"
    },
    {
        "service": "Cloud Logging",
        "dir": "cloud_logging",
        "path": "logs/query"
    },
    {
        "service": "Cloud Load Balancing",
        "dir": "cloud_load_balancing",
        "path": "net-services/loadbalancing/list/loadBalancers"
    },
    {
        "service": "IAM",
        "dir": "identity_and_access_management",
        "path": "iam-admin/iam"
    },
    {
        "service": "Service Accounts",
        "dir": "identity_and_access_management",
        "path": "iam-admin/serviceaccounts"
    },
    {
        "service": "Cloud DNS",
        "dir": "cloud_dns",
        "path": "net-services/dns/zones"
    },
    {
        "service": "Cloud NAT",
        "dir": "cloud_nat",
        "path": "net-services/nat/list"
    },
    {
        "service": "Cloud CDN",
        "dir": "cloud_cdn",
        "path": "net-services/cdn/list"
    },
    {
        "service": "Cloud Monitoring",
        "dir": "cloud_monitoring",
        "path": "monitoring"
    },
    {
        "service": "VPC networks",
        "dir": "virtual_private_cloud",
        "path": "networking/networks/list"
    },
    {
        "service": "VPC firewall rules",
        "dir": "cloud_firewall_rules",
        "path": "networking/firewalls/list"
    },
    {
        "service": "Compute Engine: Virtual Machines",
        "dir": "compute_engine",
        "path": "compute/instances"
    },
    {
        "service": "Cloud Storage",
        "dir": "cloud_storage",
        "path": "storage/browser"
    },
    {
        "service": "Anthos Service Mesh",
        "dir": "anthos_service_mesh",
        "path": "anthos/services"
    },
    {
        "service": "Google Kubernetes Engine",
        "dir": "google_kubernetes_engine",
        "path": "kubernetes/list/overview"
    },
    {
        "service": "Cloud Run",
        "dir": "cloud_run",
        "path": "run"
    },
    {
        "service": "Cloud Functions",
        "dir": "cloud_functions",
        "path": "functions/list"
    },
    {
        "service": "Cloud Bigtable",
        "dir": "bigtable",
        "path": "bigtable/instances"
    },
    {
        "service": "Firestore",
        "dir": "firestore",
        "path": "firestore/data/panel"
    },
    {
        "service": "Cloud Memorystore",
        "dir": "memorystore",
        "path": "memorystore/redis/instances"
    },
    {
        "service": "Cloud Spanner",
        "dir": "cloud_spanner",
        "path": "spanner/instances"
    },
    {
        "service": "Cloud SQL",
        "dir": "cloud_sql",
        "path": "sql/instances"
    },
    {
        "service": "Cloud Scheduler",
        "dir": "cloud_scheduler",
        "path": "cloudscheduler"
    },
    {
        "service": "Cloud Tasks",
        "dir": "cloud_tasks",
        "path": "cloudtasks"
    },
    {
        "service": "Cloud Armor Network Security",
        "dir": "cloud_armor",
        "path": "net-security/securitypolicies/list"
    },
    {
        "service": "Cloud Profiler",
        "dir": "profiler",
        "path": "profiler"
    },
    {
        "service": "Cloud Trace",
        "dir": "trace",
        "path": "traces/list"
    },
    {
        "service": "Container Registry",
        "dir": "container_registry",
        "path": "gcr"
    },
    {
        "service": "Pub/Sub",
        "dir": "pubsub",
        "path": "cloudpubsub/topic/list"
    },
    {
        "service": "BigQuery",
        "dir": "bigquery",
        "path": "bigquery"
    },
    {
        "service": "Workload Identity Pool",
        "dir": "workload_identity_pool",
        "path": "iam-admin/workload-identity-pools"
    },
    {
        "service": "Support",
        "dir": "support",
        "path": "support/cases"
    },
    {
        "service": "Secret Manager",
        "dir": "secret_manager",
        "path": "security/secret-manager"
    },
    {
        "service": "Project",
        "dir": "project",
        "path": "home/dashboard"
    },
    {
        "service": "Billing",
        "dir": "billing",
        "path": "billing"
    },
    {
        "service": "Artifact Registry",
        "dir": "artifact_registry",
        "path": "artifacts"
    },
    {
        "service": "Vertex AI",
        "dir": "vertexai",
        "path": "vertex-ai"
    },
]

args = sys.argv

path = "./icons"
icons = os.listdir(path=path)
items = []

filters_items = filter(
    lambda item: args[1] in item["service"].lower(), services)

for i in filters_items:
    items.append(
        {
            'uid': i["service"],
            'title': i["service"],
            'subtitle': baseURL+i["service"],
            'arg': baseURL+i["path"],
            'icon': {
                'path': path+"/"+i["dir"]+"/"+i["dir"]+".png"
            }
        }
    )

result = {
    'items': items
}

sys.stdout.write(json.dumps(result, ensure_ascii=False))
