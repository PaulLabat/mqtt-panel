#! /usr/bin/python2.7
# -*-coding:Utf-8 -*

from stringData import *
import json

if __name__ == '__main__':
	fileIn = open("sensors.json","r")
	fileOut = open("index.html","w")
	jdata = fileIn.read()
	fileIn.close()

	sensorsName = dict()
	sensorsId = dict()
	sensorsType = dict()
	sensorsValue = dict()
	i=0
#code de generation du code javascript
	try:
		decoded = json.loads(jdata)
		for cle, value in decoded.items():
			i = i+ 1
			sensorsName[i]=cle
			for subcle, subvalue in value.items():
				if(subcle == "id"):
					sensorsId[i] = subvalue
				elif(subcle == "value"):
					sensorsValue[i] = subvalue
				elif(subcle == "type"):
					sensorsType[i] = subvalue
	except (ValueError, KeyError, TypeError):
    		print("JSON format error")
	fileOut.write(head)
	fileOut.write(head2)

	j=i
	i=0
	while i != j:
		i = i+1
		if sensorsType[i] in ['temperature','gas','geiger']:
			fileOut.write("\nvar {} = new Array();".format(sensorsName[i]+str(sensorsId[i])))

	fileOut.write(head3)
	fileOut.write(switch)


	j=i
	i=0
	while i != j:
		i = i+1
		idS = sensorsName[i]+str(sensorsId[i])
		if sensorsType[i] == "temperature":
			fileOut.write("case '{}':\n".format(idS))
			fileOut.write("\t$('#Sensor{}').html('(Sensor value: ' + msg.payload + ')');\n".format(idS))
			fileOut.write("\t$('#Label{}').text(msg.payload + '°C');\n".format(idS))
			fileOut.write("\t$('#Label{}').removeClass('').addClass('label-default');\n".format(idS))
			fileOut.write("\t{}.push(parseInt(msg.payload));\n".format(idS))
			fileOut.write("\tif ({}.length >= 20) ".format(idS))
			fileOut.write("{ ")
			fileOut.write("{}.shift()".format(idS))
			fileOut.write("}\n")
			fileOut.write("\t$('.{}Sparkline').sparkline({},\n".format(idS,idS))
			fileOut.write("\t{\n")
			fileOut.write(" \t\t type: 'line',\n ")
			fileOut.write("\t \t width: '160',\n \t \t height: '40'});\n")
			fileOut.write("\tbreak;\n")
		if sensorsType[i] == "door":
			fileOut.write("case '{}': \n".format(sensorsName[i]+str(sensorsId[i])))
			fileOut.write("\t$('#value{}').html('(Switch value: ' + msg.payload + ')');\n".format(idS))
			fileOut.write("\tif (msg.payload == 'true') {\n")
			fileOut.write("\t\t$('#label{}').text('Closed');\n".format(idS))
			fileOut.write("\t\t$('#label{}').removeClass('label-danger').addClass('label-success');\n".format(idS))
			fileOut.write("\t} else {\n")
			fileOut.write("\t\t$('#label{}').text('Open');\n".format(idS))
			fileOut.write("\t\t$('#label{}').removeClass('label-success').addClass('label-danger');\n".format(idS))
			fileOut.write("\t}\n\tbreak;\n")
		if sensorsType[i] == "gas":
			fileOut.write("case '{}':\n".format(idS))
			fileOut.write("\t$('#Sensor{}').html('(Sensor value: ' + msg.payload + ')');\n".format(idS))
			fileOut.write("\t$('#Label{}').text(msg.payload + 'ppm');\n".format(idS))
			fileOut.write("\t$('#Label{}').removeClass('').addClass('label-default');\n".format(idS))
			fileOut.write("\t{}.push(parseInt(msg.payload));\n".format(idS))
			fileOut.write("\tif ({}.length >= 20) ".format(idS))
			fileOut.write("{ ")
			fileOut.write("{}.shift()".format(idS))
			fileOut.write("}\n")
			fileOut.write("\t$('.{}Sparkline').sparkline({},\n".format(idS,idS))
			fileOut.write("\t{\n")
			fileOut.write(" \t\t type: 'line',\n ")
			fileOut.write("\t \t width: '160',\n \t \t height: '40'});\n")
			fileOut.write("\tbreak;\n")
		if sensorsType[i] == "geiger":
			fileOut.write("case '{}':\n".format(idS))
			fileOut.write("\t$('#Sensor{}').html('(Sensor value: ' + msg.payload + ')');\n".format(idS))
			fileOut.write("\t$('#Label{}').text(msg.payload + 'Bq');\n".format(idS))
			fileOut.write("\t$('#Label{}').removeClass('').addClass('label-default');\n".format(idS))
			fileOut.write("\t{}.push(parseInt(msg.payload));\n".format(idS))
			fileOut.write("\tif ({}.length >= 20) ".format(idS))
			fileOut.write("{ ")
			fileOut.write("{}.shift()".format(idS))
			fileOut.write("}\n")
			fileOut.write("\t$('.{}Sparkline').sparkline({},\n".format(idS,idS))
			fileOut.write("\t{\n")
			fileOut.write(" \t\t type: 'line',\n ")
			fileOut.write("\t \t width: '160',\n \t \t height: '40'});\n")
			fileOut.write("\tbreak;\n")
                           


	fileOut.write(endSwitch)
	fileOut.write("\n</script>\n</head>\n")
	fileOut.write(body)
#code de generation du body
	i=0
	while i !=j:
		i = i+1
		idS = sensorsName[i]+str(sensorsId[i])
		if sensorsType[i] in ['temperature', 'gas', 'geiger']:
			fileOut.write("\n<tr>\n")
			fileOut.write('<td width="40%" style="vertical-align:middle;"><h3>{}</h3><small id="Sensor{}">(no value recieved)</small></td>\n'.format(sensorsName[i]+" - id: "+str(sensorsId[i]),idS))
			fileOut.write('<td style="vertical-align:middle;"><span class="{}Sparkline"></span></td>\n'.format(idS))
			fileOut.write('<td width="30%" style="vertical-align:middle;"><h4>&nbsp;<span id="Label{}" class="label">Unknown</span></h4></td>\n'.format(idS))
			fileOut.write("</tr>\n")

		else:
			fileOut.write("\n<tr>\n")
			fileOut.write('<td width="40%" style="vertical-align:middle;"><h3>{}</h3><small id="value{}">(no value recieved)</small></td>\n'.format(sensorsName[i]+" - id: "+str(sensorsId[i]),idS))
			fileOut.write('<td style="vertical-align:middle;"></td>\n')
			fileOut.write('<td width="30%" style="vertical-align:middle;"><h4>&nbsp;<span id="label{}" class="label">Unknown</span></h4></td>\n'.format(idS))
			fileOut.write('</tr>\n')
                        
                        
                        


	fileOut.write(endBody)
  	fileOut.write("</html>")
  	fileOut.close()
