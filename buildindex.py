#encoding: utf-8

import sys
import os

fbd = set(["LICENSE", "README.md", "buildindex.py", "robots.txt", "index.html"])

def handle(srcp, fbd, head, lkeep):
	def buildhead(hstr, lkeep):
		tmp = hstr[lkeep+1:].split("/")
		his = hstr[:lkeep]
		rs = ["<a href=\"", his, "/index.html\">/</a>"]
		for tmpu in tmp:
			his += "/" + tmpu
			rs.append("<a href=\"")
			rs.append(his)
			rs.append("/index.html\">")
			rs.append(tmpu)
			rs.append("</a>/")
		return "".join(rs)
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
		fwrt.write("<html>\n<head>\n<title>".encode("utf-8"))
		fwrt.write(buildhead(head, lkeep).encode("utf-8"))
		fwrt.write("</title>\n</head>\n<body>\n<p>\n".encode("utf-8"))
		for pu in rsp:
			fwrt.write("<a href=\""+pu[0]+"/index.html\">"+pu[-1]+"</a>/\n".encode("utf-8"))
		for fu in rsf:
			fwrt.write("<a href=\""+fu[0]+"\">"+fu[-1]+"</a>\n".encode("utf-8"))
		fwrt.write("</p>\n</body>\n</html>\n".encode("utf-8"))

if __name__=="__main__":
	srcp = os.path.realpath(sys.argv[1].decode("gbk"))
	hname = "http://anofs.azurewebsites.net"
	handle(srcp, fbd, hname, len(hname))
