# Mission 7 — How computers communicate

## 1. Task / objective

Learn basic network concepts, check network connectivity and DNS, and explain what happens when a browser opens a website.

## 2. Work completed

I used Terminal to test whether my computer could reach `example.com` and to look up the domain name. My connectivity test received replies. The DNS lookup showed an address associated with `example.com`.

### Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | A network covering a small area. | A home or school network. |
| MAN | A network covering a city or large campus area. | A network connecting buildings across a campus. |
| WAN | A network covering a large geographical area. | The internet. |
| DNS | A service that finds the network address associated with a domain name. | Looking up `example.com` so a browser can find the website. |
| Router | A device that connects networks and forwards data between them. | A home router connects devices to the internet. |
| Protocol | Rules that devices follow when communicating. | HTTPS is used to communicate securely with websites. |
| Packet switching | A way of sending data in small packets across a network. | Website data travels across the network in packets. |
| Client-server | A setup where a client requests a service and a server provides it. | A browser requests a web page from a web server. |

### Connectivity and DNS observations

A connectivity test helps check whether my computer can reach a website over the network. I used `ping -c 4 example.com`. I received replies.

A DNS lookup shows the network address associated with a domain name. I used `nslookup example.com`. DNS helps the browser find the website’s server when I enter a website name.

### What happens when I open a website?

1. I enter a website name in the browser. The browser acts as the client.
2. The client asks DNS to find the network address for the website name.
3. DNS returns an address for the website.
4. My computer sends a request through the network and router toward the server.
5. The client and server communicate using a protocol such as HTTPS.
6. The server sends the requested website data back in packets.
7. The browser receives the response and displays the page.

## 3. Commands / tools used

- `ping -c 4 example.com` — tested whether my computer could reach the example website.
- `nslookup example.com` — looked up the network address associated with the domain.
- Terminal — used to run the network commands.
- VS Code — used to write this README.

## 4. My understanding

Networks let computers exchange information. DNS helps find a website’s network address, and a router forwards data between networks. A browser acts as a client that requests information from a server, and protocols define how they communicate.

## 5. Difficulties faced

Did not know this:

ping -c 4 example.com
nslookup example.com

## 6. How I resolved them

Looked it up and understood

## 7. Evidence / files

- `mission-07-networking/README.md`

## 8. Commit details

- Commit message: `Explain networking concepts and website communication`
- Pushed to GitHub.