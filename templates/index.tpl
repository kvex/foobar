%rebase base title='Главная', categories=categories

%for post in paginator.object_list():
	<div class="post">
		<h2>{{ post.title }}</h2>
		<div class="category">Категория: <a href="{{ post.category.get_absolute_url }}">{{ post.category.name }}</a></div>
		<p>{{ post.teaser }}</p>
		<div class="date">{{ post.pub_date }}</div>
		<a href="{{ post.get_absolute_url }}">Читать полностью</a>
	</div>
%end

%for page in paginator.page_list():
	<a href="?page={{ page }}">{{ page }}</a>
%end