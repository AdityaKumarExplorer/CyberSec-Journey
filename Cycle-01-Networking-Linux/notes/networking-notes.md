## 🌐 1. OSI Model (7 Layers)

The OSI Model explains how data travels from one system to another in **7 layers**.

| Layer | Name         | Function                         |
| ----- | ------------ | -------------------------------- |
| 7     | Application  | User interaction (browser, apps) |
| 6     | Presentation | Encryption, formatting           |
| 5     | Session      | Connection setup/termination     |
| 4     | Transport    | Reliable data transfer (TCP/UDP) |
| 3     | Network      | IP addressing, routing           |
| 2     | Data Link    | MAC address, local delivery      |
| 1     | Physical     | Cables, signals                  |

💡 Data flows **top → bottom → network → bottom → top**

---

## 🔄 2. TCP vs UDP

| Feature        | TCP                        | UDP               |
| -------------- | -------------------------- | ----------------- |
| Type           | Connection-oriented        | Connectionless    |
| Speed          | Slower                     | Faster            |
| Reliability    | High (guaranteed delivery) | Low               |
| Error checking | Yes                        | Minimal           |
| Use cases      | Web browsing, emails       | Streaming, gaming |

💡

* TCP = reliable but slower
* UDP = fast but risky

---

## 🌍 3. 10 Common Protocols with Port Numbers

| Protocol | Port  | Purpose                  |
| -------- | ----- | ------------------------ |
| HTTP     | 80    | Web communication        |
| HTTPS    | 443   | Secure web communication |
| FTP      | 21    | File transfer            |
| SSH      | 22    | Secure remote login      |
| Telnet   | 23    | Remote login (insecure)  |
| DNS      | 53    | Domain name resolution   |
| DHCP     | 67/68 | IP address assignment    |
| SMTP     | 25    | Sending emails           |
| POP3     | 110   | Receiving emails         |
| IMAP     | 143   | Email access (advanced)  |

---

## 🌐 4. How DNS Works (Step-by-Step)

DNS converts **domain names → IP addresses**

### Example: typing `google.com`

### Step-by-step flow:

1. **User enters domain**

   * Browser needs IP address

2. **Check local cache**

   * If found → use it
   * If not → continue

3. **Query DNS Resolver**

   * Usually ISP DNS server

4. **Resolver asks Root Server**

   * “Where is .com?”

5. **Root → TLD Server (.com)**

   * Points to correct server

6. **TLD → Authoritative Server**

   * Stores actual IP

7. **Authoritative server returns IP**

   * Example: `142.x.x.x`

8. **Browser connects to server**

   * Website loads

💡
DNS is like:

> “Find the phone number before making a call”

---

