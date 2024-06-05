# 0x18-webstack_monitoring

# Task 0: Sign up for Datadog and install datadog-agent

### Steps:

1. Signed up for Datadog account.
2. Installed Datadog Agent on `web-01` server.
3. Created application key and added API key and application key to the Intranet user profile.
4. Verified server `XX-web-01` visibility in Datadog.

### Verification:

- Server `XX-web-01` is visible under the Hosts section in Datadog.
- Validated using Datadog API.

## Task 1: Monitor Some Metrics

### Steps:

1. **Set Up Read Requests Monitor**:
    - Created a new monitor for the metric `system.io.read_req_sec`.
    - Configured alert conditions to trigger if read requests per second exceed a specified threshold.
    - Added notification channels for alerts.
    - Named the monitor "Read Requests per Second".

2. **Set Up Write Requests Monitor**:
    - Created a new monitor for the metric `system.io.write_req_sec`.
    - Configured alert conditions to trigger if write requests per second exceed a specified threshold.
    - Added notification channels for alerts.
    - Named the monitor "Write Requests per Second".

### Verification:

- Monitors are active and visible in the Datadog dashboard.
- Alerts will trigger if the defined thresholds are exceeded.

## Task 2: Create a Dashboard

### Steps:

1. **Create Dashboard**:
    - Created a new dashboard named "Web Stack Monitoring Dashboard" in Datadog.
    - Added the following widgets:
        - Timeseries widget for CPU usage (`system.cpu.user`).
        - Query value widget for memory usage (`system.mem.used`).
        - Hostmap widget for visualizing host status.
        - Top list widget for processes by CPU usage (`system.processes.cpu.user`).

2. **Retrieve Dashboard ID**:
    - Used Datadog API to list dashboards and retrieve the ID of the newly created dashboard.

3. **Save Dashboard ID**:
    - Created the file `2-setup_datadog`.
    - Wrote the dashboard ID to the file.

### Verification:

- Dashboard is visible and functional in Datadog.
- Dashboard ID is saved in `2-setup_datadog`.
