# Calls: Self-Hosted Deployment Guide

```{include} ../../_static/badges/allplans-selfhosted.md
```

## Overview

Mattermost Calls is an excellent option for organizations that need enhanced security and control. It's designed to run securely in self-hosted deployments, including air-gapped networks, ensuring private communication without relying on the public internet.

This guide will help you successfully set up the Calls plugin in your own infrastructure. We'll cover the necessary requirements, common deployment strategies, and key configuration options.

---

## 1. Key Concepts and Terminology

To understand how Mattermost Calls works in a self-hosted environment, here are some key terms:

- [WebRTC](https://bloggeek.me/webrtcglossary/webrtc-2/): The set of underlying protocols/specifications on top of which calls are implemented.
- **RTC (Real Time Connection)**: The real-time connection. This is the channel used to send media tracks (audio/video/screen).
- **WS (WebSocket)**: The WebSocket connection. This is the channel used to set up a connection (signaling process).
- [NAT (Network Address Translation)](https://bloggeek.me/webrtcglossary/nat/): A networking technique to map IP addresses.
- [STUN (Session Traversal Utilities for NAT)](https://bloggeek.me/webrtcglossary/stun/): A protocol/service used by WebRTC clients to help traversing NATs. On the server side it's mainly used to figure out the public IP of the instance.
- [TURN (Traversal Using Relays around NAT)](https://bloggeek.me/webrtcglossary/turn/): A protocol/service used to help WebRTC clients behind strict firewalls connect to a call through media relay.

---

## 2. Deployment Requirements

### Server Requirements

* **Secure Connection (HTTPS):** Your Mattermost server must be running on a secure HTTPS connection. This is required for clients to be able to capture devices like microphones and screens.
* **Network Requirements:**
    * **API (TCP 80/443):** Used for the main client connection to the Calls plugin. This is typically already configured.
    * **RTC (UDP/TCP 8443):** Mattermost or the `rtcd` service must be able to receive traffic on these ports for media (audio and video) to work correctly.

### Client Requirements

* Clients (web browser, desktop, mobile app) must be able to connect to your Mattermost instance on the configured UDP port. If this is not possible, a TURN server may be needed.
* Users may need to grant their application (e.g., browser) permissions to capture audio inputs or share their screen.

---

## 3. Features and Limitations

| Feature                         | Available For                 | Notes                                                                                                                              |
| ------------------------------- | ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **1:1 Calls** | All plans                     | Includes audio and optional screen sharing.                                                                                        |
| **Group Calls (up to 50 users)** | Enterprise / Professional     | This is the recommended default. For more participants, consider using the `rtcd` service.                                         |
| **Call Recording** | Enterprise                    | Requires the `calls-offloader` job service to be configured.                                                                       |
| **Live Captions** | Enterprise                    | Requires the `calls-offloader` job service to be configured.                                                                       |
| **Transcription of Recordings** | Enterprise                    | Requires the `calls-offloader` job service to be configured.                                                                       |

---

## 4. Modes of Operation

The Calls plugin can be deployed in different ways, depending on your architecture.

### **a) Single Instance**

* **Integrated (Default):** The WebRTC service runs alongside the plugin. This is the simplest option for a single Mattermost instance.
    * 
    > ![Diagram of a single instance integrated deployment.](../../images/calls-deployment-image3.png)

* **`rtcd` (External):** A separate WebRTC service (`rtcd`) handles all media routing. This is recommended for higher performance and scalability needs.
    > ![Diagram of a WebRTC deployment with an rtcd service.](../../images/calls-deployment-image7.png)

### **b) High Availability (HA) Cluster**

* **Clustered (Default):** Each cluster node runs a plugin instance. Calls are distributed across all available nodes via the load balancer.
    > ![Diagram of a clustered calls deployment.](../../images/calls-deployment-image5.png)

* **`rtcd` (External):** The `rtcd` service can also be used in HA clusters to isolate calls traffic and improve stability.
    > ![Diagram of an rtcd deployment in a cluster.](../../images/calls-deployment-image2.png)

---

## 5. How to Configure and Scale

### **Using the `rtcd` Service**

`rtcd` is an external service that isolates call traffic to improve performance and scalability. It is **recommended** for:

* **Performance:** It prevents call traffic spikes from negatively impacting the main Mattermost server.
* **Stability:** If the main server restarts, ongoing calls will not be dropped.
* **Scalability:** `rtcd` servers can be easily added to handle a higher load.
* **Kubernetes:** This is the officially supported way to run Calls in Kubernetes environments.

### **Recording, Transcription, and Live Captions**

To use these features (available for Enterprise customers), you must first configure the **`calls-offloader`** service.

* Refer to the [calls-offloader documentation](https://github.com/mattermost/calls-offloader) on GitHub for deployment instructions.
* After deployment, enable and configure the service in the **System Console**.

### **Kubernetes Deployments**

Mattermost is designed to integrate well with Kubernetes. For these environments, using the **`rtcd` service** and the official **Helm charts** is the recommended approach.

> ![Diagram of calls deployed in a Kubernetes cluster.](../../images/calls-deployment-kubernetes.png)

---

## 6. Performance and Monitoring

Call performance depends on **CPU** and **bandwidth**. Resource consumption increases with the number of participants.

* The original documentation includes a **benchmarks** table with load-testing results. Use this data to help size your infrastructure.
* You can **monitor** the performance of the Calls plugin and `rtcd` service using **Prometheus** and **Grafana**. Refer to the official documentation for setup instructions.
