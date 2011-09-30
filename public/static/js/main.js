(function() {
	var util = {
		get: function(id) {
			return document.getElementById(id);
		},
		cycle: function(arr, func) {
			for (var i=0; i < arr.length; i++) {
				func(arr[i]);
			}
		}
	}
	
	var app = {};
	app.page = util.get('page');
	app.wrappers = [util.get('wrapper'), 
					util.get('wrapper-1'), 
					util.get('wrapper-2')]
	
	app.resize = function() {
		util.cycle(app.wrappers, function(item) {
			item.style.height = 'auto';
		});
		
		util.cycle(app.wrappers, function(item) {
			item.style.height = app.page.offsetHeight + 'px';
		});
	}
	
	window.onresize = function() {
		app.resize();
	}
	
	app.resize();
})();