htmlFile = open('remotemulitview.html', 'w')
ips = open('ipaddresses.txt', 'r').read().split()

htmlFile.write('<html><body>')

for ip in ips:
	htmlFile.write('<iframe src="http://' + ip + ':63112/" width=500 height=300> </iframe>')

htmlFile.write('</body></html>')
