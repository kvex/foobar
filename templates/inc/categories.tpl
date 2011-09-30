<ul id="menu">
	<li><a href="/">Главная</a></li>
%for category in categories:
	<li><a href="{{ category.get_absolute_url }}">{{ category.name }}</a></li>
%end
</ul>