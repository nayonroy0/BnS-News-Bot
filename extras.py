def get_links(src):
	in_img_tag = False
	out = ""
	for j in src.split('\n'):
		if j:
			for i in j.split():
				if i == "<img" or in_img_tag:
					in_img_tag = True
					if i[:3] == "src":
						out += "http:" + i[5:-1] + " "
					if i[-2:] == "/>":
						in_img_tag = False
				else:
					if i == "&amp;":
						out += "& "
					else:
						out += i + " "
			out += '\n'
	return out