<ul id="menu">
	<li><a href="/">Главная</a></li>
%for category in categories:
	<li \\
    %if category == active_category: 
        class="active"\\
    %end \\
    >
        <a href="{{ category.get_absolute_url }}">{{ category.name }}</a>
    </li>
%end
</ul>
