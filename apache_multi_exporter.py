from bottle import route, run, response, request
import urllib2, sys

@route('/metrics')
def get_metrics():
	try:	
		target = request.query['target']
		server_status_url = target + '/server-status?auto'

		res = urllib2.urlopen(server_status_url)
		lines = res.read().splitlines()
		var = dict()
		for line in lines:
			a,b=line.split(":")
			var[a]=b

		idle_workers=var["IdleWorkers"].strip()
		busy_workers=var["BusyWorkers"].strip()
		uptime=var["Uptime"].strip()
		total_accesses=var["Total Accesses"].strip()
		total_kbytes=var["Total kBytes"].strip()
		cpu_load=var["CPULoad"].strip()
		req_per_sec=var["ReqPerSec"].strip()
		bytes_per_sec=var["BytesPerSec"].strip()
		bytes_per_req=var["BytesPerReq"].strip()

		metrics = 'apache_busy_workers ' + busy_workers  + '\n'
		metrics+= 'apache_idle_workers ' + idle_workers  + '\n'
		metrics+= 'apache_uptime ' + uptime + '\n'
		metrics+= 'apache_total_accesses ' + total_accesses + '\n'
		metrics+= 'apache_total_kbytes ' + total_kbytes + '\n'
		metrics+= 'apache_cpu_load ' + cpu_load + '\n'
		metrics+= 'apache_req_per_sec ' + req_per_sec + '\n'
		metrics+= 'apache_bytes_per_sec ' + bytes_per_sec + '\n'
		metrics+= 'apache_bytes_per_req ' + total_accesses + '\n'
		metrics+= 'apache_total_accesses ' + total_accesses + '\n'
		response.content_type = 'text/plain; charset=utf-8'
		return metrics
	except IOError as e:
		response.status = 300
		return("I/O error({0}): {1}".format(e.errno, e.strerror))			
	except:
		response.status = 300
		return("Unexpected error:", sys.exc_info()[0])

run(host='localhost', port=8767)
