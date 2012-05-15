// Promotes Django-Angular interoperation by using (( )) 
// for angular bindings
angular.markup('(())', function(text, textNode, parentElement){ 
	if (parentElement[0].nodeName.toLowerCase() == 'script') return; 

	text = text.replace(/\(\(/g,'{{').replace(/\)\)/g, '}}'); 
	textNode.text(text); 
	return angular.markup('{{}}').call(this, text, textNode, parentElement); 
}); 

// Corrects attribute bindings to support (( )) over {{ }}
angular.attrMarkup('(())', function(value, name, element){
    value = value.replace(/\(\(/g,'{{').replace(/\)\)/, '}}');
    element[0].setAttribute(name, value);
    return angular.attrMarkup('{{}}').call(this, value, name, element);
});
