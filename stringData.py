# -*-coding:Utf-8 -*



head = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A web interface for MQTT">
    <meta name="author" content="Fabian Affolter">

    <title>Sensors condition</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.css" rel="stylesheet">
    <!-- jQuery -->
    <script type="text/javascript" src="js/jquery-1.10.2.min.js"></script>
    <!-- Sparkline -->
    <script type="text/javascript" src="js/jquery.sparkline.min.js"></script>
    <!-- jgPlot -->
    <link class="include" rel="stylesheet" type="text/css" href="dist/jquery.jqplot.min.css" />
    <script type="text/javascript" src="js/jquery.jqplot.min.js"></script>
    <script type="text/javascript" src="js/jqplot.canvasTextRenderer.min.js"></script>
    <script type="text/javascript" src="js/jqplot.canvasAxisLabelRenderer.min.js"></script>
    <script type="text/javascript" src="js/jqplot.dateAxisRenderer.min.js"></script>

    <!-- socket.io for communication -->
    <script type="text/javascript" src="js/socket.io.min.js"></script>\n"""


head2 = """ <script type="text/javascript">\nvar socket = io.connect('http://localhost:3000');"""

head3="""   \nsocket.on('connect', function () {
                socket.on('mqtt', function (msg) {
                    var message = msg.topic.split('/');
                    var area = message[1];
                    var state = message[2];
                    console.log(msg.topic, msg.payload);
                    var timestamp = Math.round((new Date()).getTime() / 1000);

                    $('#topic').html(msg.topic);
                    $('#message').html(msg.topic + ', ' + msg.payload); """

switch = "\nswitch(area){\n"
endSwitch = """\ndefault:\n \t console.log('Error: Data do not match the MQTT topic.');\n break;\n}\n});\nsocket.emit('subscribe', {topic : 'sensors/#'});\n});"""
body = """
    <div id="wrap">
      <div class="container">
        <div class="page-header"><h1><b>Sensors conditions</b></h1></div>

            <div class="panel panel-default">
              <div class="panel-body">
                    <table class="table table-striped"> """

endBody = """  </table>
              </div>
            </div>
          <div class="panel panel-default">
            <div class="panel-body">
                    <b>Latest MQTT message:  </b> <small id="message">no message recieved</small>
            </div>
          </div>

        <div class="footer">
        <small><p class="text-center">&copy; <a href="http://affolter-engineering.ch">Affolter Engineering</a> 2013</p></small>
    </div>
    </body>"""
