function loadDevices(url) {

	var PythonShell = require('python-shell');

	PythonShell.run('test.py', function (err) {
	  if (err) throw err;
	  console.log('finished');
	});
}