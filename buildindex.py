#encoding: utf-8

import sys
import os

fbd = set(["LICENSE", "README.md", "buildindex.py", "robots.txt", "index.html", "trfqz_2CB7A3F4.mp3"])

def handle(srcp, fbd, head, lkeep):
	def buildhead(hstr, lkeep):
		his = hstr[:lkeep]
		rs = [" <a href=\"", his, "\">/</a> "]
		tmp = hstr[lkeep+1:].strip()
		if tmp:
			for tmpu in tmp.split("/"):
				his += "/" + tmpu
				rs.append("<a href=\"")
				rs.append(his)
				rs.append("/\">")
				rs.append(tmpu)
				rs.append("</a> / ")
		return "".join(rs).strip()
	rsp = []
	rsf = []
	for content in os.listdir(srcp):
		newsrcp = os.path.join(srcp, content)
		if head:
			newhead = head+"/"+content
		else:
			newhead = content
		if os.path.isdir(newsrcp):
			if not content.startswith("."):
				rsp.append((newhead, content, ))
				handle(newsrcp, fbd, newhead, lkeep)
		else:
			if not content in fbd:
				rsf.append((head+"/"+content, content, ))
	with open(srcp+"\\index.html", "w") as fwrt:
		fwrt.write("<html>\n<head>\n<title>anoFS</title>\n</head>\n<body>\n<p>".encode("utf-8"))
		fwrt.write(buildhead(head, lkeep).encode("utf-8"))
		fwrt.write("</p>\n".encode("utf-8"))
		for pu in rsp:
			fwrt.write("<p><a href=\""+pu[0]+"/\">"+pu[-1]+"</a>/</p>\n".encode("utf-8"))
		for fu in rsf:
			fwrt.write("<p><a href=\""+fu[0]+"\">"+fu[-1]+"</a></p>\n".encode("utf-8"))
		fwrt.write("</body>\n</html>\n".encode("utf-8"))

if __name__=="__main__":
	if len(sys.argv)>1:
		srcp = os.path.realpath(sys.argv[1].decode("gbk"))
	else:
		srcp = "."
	hname = "http://anofs.azurewebsites.net"
	handle(srcp, fbd, hname, len(hname))
