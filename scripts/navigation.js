// Menu Controller
function MenuCtrl($xhr) {
	var self = this;
	
	$xhr('GET', 'Menu', function(code, response){
		self.menu_items = response;
	});	
}	

