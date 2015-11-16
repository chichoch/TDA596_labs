htmlFile = open('localmulitview.html', 'w')
ports = open('localports.txt', 'r').read().split()

htmlFile.write('<html><body>')

for port in ports:
	htmlFile.write('<iframe src="http://127.0.0.1:' + port + '/" width=500 height=300> </iframe>')

htmlFile.write('</body></html>')